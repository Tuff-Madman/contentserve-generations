import re
from typing import Dict, Any, List, Tuple

SEPARATOR = "|||---|||"
DISALLOWED_PUNCT = set(list('!?;:')) | set(['„','“','«','»','‚','‘','”','“','´'])
FORBIDDEN_WHITESPACE_PATTERN = re.compile(r"[\u00A0\u2000-\u200B\u202F\u205F\u3000]")
DOUBLE_SPACE_PATTERN = re.compile(r"  +")
UNIT_WORDS_FORBIDDEN = re.compile(r"\b(Zentimeter|Millimeter|Kilogramm|Liter)\b", re.IGNORECASE)
SINGLE_VALUE_UNIT = re.compile(r"\b\d{1,3}(?:\s\d{3})*\s(cm|mm|kg|l)\b")
DIM_LIST_UNIT = re.compile(r"\b\d{1,3}(?:\s\d{3})?(?:\s?x\s?\d{1,3}(?:\s\d{3})?){1,2}\s(cm|mm)\b")
UPPERCASE_UNIT = re.compile(r"\b(CM|MM|KG|L)\b")
FORBIDDEN_DIM_SIGNS = re.compile(r"[×]")
REPEATED_UNIT_IN_LIST = re.compile(r"\b\d{1,3}(?:\s\d{3})?\s?(?:x\s?\d{1,3}(?:\s\d{3})?\s?)+(?:(?:cm|mm)\s(?:cm|mm))\b")
TITLE_FINAL_DOT = re.compile(r"\.\s*$")

def find_all(haystack: str, needle: str) -> List[int]:
    idxs, start = [], 0
    while True:
        i = haystack.find(needle, start)
        if i == -1: return idxs
        idxs.append(i); start = i + 1

def has_disallowed_punct(s: str) -> List[Tuple[str,int]]:
    return [(ch, i) for i, ch in enumerate(s) if ch in DISALLOWED_PUNCT]

def validate_output(output: str) -> Dict[str, Any]:
    errors, warnings = [], []

    if output != output.strip():
        errors.append({"rule":"E2","msg":"Leading/trailing whitespace","evidence":output[:40]+("..." if len(output)>40 else "")})
    if FORBIDDEN_WHITESPACE_PATTERN.search(output):
        errors.append({"rule":"E2","msg":"Non-ASCII whitespace (NBSP/ZWSP/etc.)","evidence":"Unicode whitespace found"})
    sep_count = output.count(SEPARATOR)
    if sep_count != 1:
        errors.append({"rule":"E1","msg":f"Separator must be exactly once; found {sep_count}","evidence":f"indices={find_all(output, SEPARATOR)}"})
    if '"' in output:
        errors.append({"rule":"E4","msg":'Forbidden quote " found',"evidence":'…"...'})
    if '[' in output or ']' in output:
        errors.append({"rule":"E4","msg":"Forbidden bracket [ or ] found","evidence":"…[ or ]…"})
    dis_p = has_disallowed_punct(output)
    if dis_p:
        sample = ", ".join([f"{ch}@{pos}" for ch,pos in dis_p[:5]])
        errors.append({"rule":"P-BL","msg":"Disallowed punctuation","evidence":sample+(" ..." if len(dis_p)>5 else "")})
    if DOUBLE_SPACE_PATTERN.search(output):
        errors.append({"rule":"SPACE","msg":"Multiple consecutive spaces","evidence":"…  …"})
    if sep_count != 1:
        return _final_report(output,None,None,errors,warnings)

    sep_idx = output.find(SEPARATOR)
    if sep_idx>0 and output[sep_idx-1]==' ':
        errors.append({"rule":"E1","msg":"Space before separator","evidence":output[sep_idx-5:sep_idx+len(SEPARATOR)+5]})
    after_idx = sep_idx + len(SEPARATOR)
    if after_idx < len(output) and output[after_idx:after_idx+1]==' ':
        errors.append({"rule":"E1","msg":"Space after separator","evidence":output[sep_idx-5:sep_idx+len(SEPARATOR)+5]})

    title, subtitle = output.split(SEPARATOR)
    if TITLE_FINAL_DOT.search(title):
        errors.append({"rule":"P1","msg":"Title ends with a period","evidence":title[-10:]})

    for seg_name, seg in (("title", title),("subtitle", subtitle)):
        if UPPERCASE_UNIT.search(seg):
            errors.append({"rule":"M2","segment":seg_name,"msg":"Uppercase units (CM/MM/KG/L)","evidence":UPPERCASE_UNIT.search(seg).group(0)})
        if UNIT_WORDS_FORBIDDEN.search(seg):
            m = UNIT_WORDS_FORBIDDEN.search(seg)
            errors.append({"rule":"M2w","segment":seg_name,"msg":"Written-out unit (Zentimeter/Liter/…)","evidence":m.group(0)})
        if FORBIDDEN_DIM_SIGNS.search(seg):
            errors.append({"rule":"M3x","segment":seg_name,"msg":"Forbidden '×' used; use ASCII 'x'","evidence":"×"})
        if REPEATED_UNIT_IN_LIST.search(seg):
            errors.append({"rule":"M3r","segment":seg_name,"msg":"Repeated unit in dimension list","evidence":REPEATED_UNIT_IN_LIST.search(seg).group(0)})

        for m in re.finditer(r"\b(cm|mm|kg|l)\b", seg):
            unit = m.group(1); start = m.start()
            pre = seg[max(0,start-10):start]
            if not re.search(r"\d(?:\s\d{3})*\s$", pre):
                errors.append({"rule":"M1","segment":seg_name,"msg":f"Missing space or numeric before '{unit}'","evidence":seg[max(0,start-10):start+len(unit)]})

        if 'x' in seg:
            candidates = re.findall(r"\b\d[^\n]{0,40}?x[^\n]{0,40}?\d[^\n]{0,40}?(?:x[^\n]{0,40}?\d)?[^\n]{0,10}\b", seg)
            for cand in candidates:
                if re.search(r"\d\s?x\s?\d", cand) and not DIM_LIST_UNIT.search(cand):
                    errors.append({"rule":"M3","segment":seg_name,"msg":"Invalid dimension list (A x B [x C] cm/mm)","evidence":cand})
        if 'x' in seg and re.search(r"\b\d(?:\s?\d{3})?\s?x\s?\d", seg) and re.search(r"\b(kg|l)\b", seg):
            errors.append({"rule":"M3kl","segment":seg_name,"msg":"kg/l not allowed in dimension lists","evidence":seg})
        if DOUBLE_SPACE_PATTERN.search(seg):
            errors.append({"rule":"SPACE","segment":seg_name,"msg":"Double spaces in segment","evidence":"…  …"})
        if FORBIDDEN_WHITESPACE_PATTERN.search(seg):
            errors.append({"rule":"E2","segment":seg_name,"msg":"Non-ASCII whitespace in segment","evidence":"Unicode whitespace found"})

    return _final_report(output,title,subtitle,errors,warnings)

def _final_report(output, title, subtitle, errors, warnings) -> Dict[str, Any]:
    blocker_rules = {"E1","E2","E3","E4","P1","M1","M2","M2w","M3","M3x","M3r","M3kl","SPACE","P-BL"}
    blocker = any(e.get("rule") in blocker_rules for e in errors)
    score = max(0, 100 - 15*len(errors))
    return {"pass": not blocker and len(errors)==0, "blocker": blocker, "score": score,
            "errors": errors, "warnings": warnings,
            "segments": {"title": title, "subtitle": subtitle} if title is not None else None,
            "raw": output}

def run_demo():
    samples = [
        "TV-Schrank 180 x 40 x 50 cm|||---|||TV-/Medienschrank, Aufbewahrung von Setup & Zubehör",
        "TV-Schrank 180 x 40 x 50 cm |||---||| Stauraum",
        "Sideboard 200 x 50 x 80 CM|||---|||",
        "Bett 180 cm x 200 cm cm|||---|||Komfort",
        "Kommode 120\u00A0x\u00A040\u00A0x\u00A080\u00A0cm|||---|||Stauraum",
        "„Bett“ 180 x 200 cm|||---|||Stauraum",
        "Bett 180 x 200 cm.|||---|||Stauraum",
        "Schrank 180 × 200 cm|||---|||Ablage",
    ]
    for i, s in enumerate(samples):
        print(f"\n=== Sample {i} ===")
        res = validate_output(s)
        print("pass:", res["pass"], "blocker:", res["blocker"], "score:", res["score"])
        if res["segments"]:
            print("title:", res["segments"]["title"])
            print("subtitle:", res["segments"]["subtitle"])
        print("errors:")
        for e in res["errors"]:
            print(" -", e)

if __name__ == "__main__":
    run_demo()
