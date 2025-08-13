---
description: "Defines specific formatting rules for furniture titles, covering measurements, colors, capitalization, and punctuation."
placement: "replace:[[## TITLE FORMAT AND STRUCTURE]]"
status: draft
---

```
## FORMATTING AND STRUCTURE RULES (Porta TITLE Formatter)
<!--
Note: This commented section serves as internal guiding for prompting/parsing/rule comprehension:  
- single-quoted ('like this') strings separated by commas are used for correct or incorrect example elements  
- parentheses contain descriptive comments or further details for implementation  
- After the dash in first listing level, double space indicate indentation as per formatting convention  
- each bullet point end requires two trailing spaces for a proper line break  
-->

### MEASUREMENTS
The following serves as an LLM internal reference or guiding for prompting/parsing/rule comprehension of preceding content:  
- single-quoted ('like this') strings separated by commas are used for correct or incorrect example elements  
- parentheses contain descriptive comments or further details for implementation  
- After the dash in first listing level, double space indicate indentation as per formatting convention  
- each bullet point end requires two trailing spaces for a proper line break  
-->

**Rule M1 (Spacing):** Always use a space between number and unit.  
- ✅ Correct: '250 cm', '75 kg', '1 200 mm', '2 l'  
- ❌ Incorrect: '250cm', '75kg', '1200mm', '2l'  

**Rule M2 (Unit Abbreviations):** Always use lowercase, abbreviated SI units.  
- ✅ Correct: 'cm', 'mm', 'kg', 'l'  
- ❌ Incorrect: 'Zentimeter', 'Millimeter', 'KG', 'Liter'  

**Rule M3 (Multiple Dimensions):** For dimension lists (e.g., H × W × D), place the unit only once at the very end.  
- ✅ Correct: '250 x 216 x 65 cm'  
- ❌ Incorrect: '250 cm x 216 cm x 65 cm'  


### COLORS AND FINISHES

**Rule C1 (Slash Spacing):** Use slash (/) with no spaces to indicate color and finish combinations..
- ✅ Correct: 'grau/braun', 'basaltgrau/eiche'  
- ❌ Incorrect: 'grau/ braun', 'grau / braun', 'grau /braun'    

**Rule C2 (Color Case):** Colors in lowercase.  
- ✅ Correct: 'grau/braun'  
- ❌ Incorrect: 'Grau/Braun'  


### BRANDS & CAPITALIZATION

**Rule B1 (Brand Copy-Exactly):** Use brand names exactly as provided in the original product attribute input.  
- ✅ Correct: 'CASAVANTI', 'hartmann'  
- ❌ Incorrect: 'Casavanti', 'HARTMANN' (if not delivered that way)  

**Rule B2 (Product Names/Series):** For product names/series (if any) exactly as provided in the original product attribute input (1:1 copy).
- ✅ Correct: 'SECRET' (as given)  
- ❌ Incorrect: 'Secret' (Changing capitalization from original input)  

**Rule B3 (Title Start Case):** Product titles start by default with a capital letter; if the first token is a brand, keep its original casing.  
- ✅ Correct: 'Schwebetürenschrank CASAVANTI…'  
- ✅ Exception: 'hartmann Wohnwand CAYA…'  
- ❌ Incorrect: 'schwebetürenschrank CASAVANTI…'  

### ABBREVIATIONS

**Rule A1 (nouns and technical terms abbreviations):** Use only standardized, SEO-relevant abbreviations common to the segment; unknown or seldom-used abbreviations must be written out to avoid confusion.  
- ✅ Correct: 'USB', 'LED', 'TV'

**Rule A2 (adverbial and adjectival abbreviations):** Use standard German descriptive abbreviations (e.g., 'ca.' for 'circa', 'inkl.') with a period instead of the full word.
- ✅ Correct: 'ca. 200 cm', 'inkl. Beleuchtung', 'zzgl. Versand'  
- ❌ Incorrect: 'circa 200 cm', 'inklusive  Beleuchtung', 'zzgl Versand' 



### PUNCTUATION

**Rule P1 (No Final Period):** Do not end product titles with a period.  
- ✅ Correct: '… 250 x 216 cm grau/ braun'  
- ❌ Incorrect: '… grau/ braun.'  

**Rule P2 (Allowed Punctuation):** Use only the punctuation symbols listed below. Any other symbols are disallowed unless they are officially part of a brand or series name.

- ✅ Allowed Punctuation:  
  - '.' (for abbreviations like 'ca.'),  
  - 'x' (dimension separator per Rule M3),  
**Rule P2 (Punctuation Guidelines):** Follow the general formatting rules defined above and restrict punctuation to the allowed symbols listed below. Disallowed symbols must never appear in a product title unless an exception noted in parentheses applies.
  - '–' (en-dash for series or set info; only if officially provided)

- ❌ Disallowed Punctuation:  
  - '!',  
  - '?',  
  - ';',  
  - ':',  
  - '"',  
  - '´' (apostrophe; allowed only if officially part of the name)


**Rule P3 (Single Spacing):** Use only single spaces as Multiple consecutive spaces are not allowed.  
- ✅ Correct: 'Schrank mit Türen'  
- ❌ Incorrect: 'Schrank  mit   Türen'  
```
