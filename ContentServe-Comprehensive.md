# ContentServe Comprehensive Consolidation

---

## Table of Contents
1. Introduction
2. Theory & Arguments
3. Practical Rules & Guidelines
4. Prompt Engineering & Style
5. Chatbot/Integration Notes
6. Glossary
7. References & Further Reading
8. Appendix (Raw Content)

---

## 1. Introduction

This document consolidates all unique, detailed ContentServe-related material, preserving all original formatting rules, templates, and style conventions. It is structured for easy navigation, traceability, and future expansion.

---

## 2. Theory & Arguments

### The Category Friction Problem (21 Principles, Arguments, and Examples)

- Full argumentation on category friction, LLM-native approaches, modularity, scaling laws, and technical underpinnings.
- Concrete examples and tables (e.g., Esszimmertisch vs. Schreibtisch, Highboard vs. Vitrine, etc.).
- All 21 principles for LLM-native product description systems.

> (See `dilemma.md` and `Article - Problem Friktiionierung kategrieweise.md` for full text, tables, and argumentation.)

---

## 3. Practical Rules & Guidelines

### Forbidden Practices (verbatim)
```
<FORBIDDEN_PRACTICES> = [
  "Making unverifiable claims",
  "Using superlatives without proof",
  "Including misleading specifications",
  "pro,otinmal use of emotional appeal",
  "Making health or saefty claims not grounded on specifc certification"
]
```

### Product Description Content Instructions
- Product name and primary material
- Exact dimensions (WxDxH format)
- 2-3 key functional benefits
- Primary style/design category
- Conditional inclusions (assembly, care, shipping, warranty)
- Exclusions (shipping costs, return process, etc.)

### JSON Structure Example (verbatim)
```
{
  "first line": "Concise, keyword-rich, SEO-optimized", 
  "subtitle": "value, benefit-focused secondary line",
  "description": "Paragraph with most relevant Product Type, Style, Material, Color, Function, RoomContext",
  "sentencees": [ 
    "Key feature 1 (Material + Style)",
    "Key feature 2 (Function + USP)",
    "Key feature 3 (RoomContext)"
  ],
  "seo_insertions": ["Primary Keyword", "Secondary Keyword", "Use Case", "Style Tag"] 
}
description: final conmentated descuptio text
```

- Only use the provided ontology. Do not invent values. Do not write formatted. Just nice, mobile-friendly paragraphs.

---

## 4. Prompt Engineering & Style

### The 5 Building Blocks Template
- PRIMING (CONTEXT, ROLE, PURPOSE)
- WRITING INSTRUCTIONS (STYLE GUIDE, STRUCTURE, STANDARDS)
- CONSTRAINTS AND PROHIBITIONS
- EXAMPLES AND REFERENCES
- DOUBLE DOWN KEY POINT REMINDER

### Style Prompts (verbatim, from `style promting reference openai.md`)
- All OpenAI/DALL-E prompt rules, diversity, copyright, and bias handling
- Do not change or omit any formatting or policy rules

### Notebook Prompt Definitions
- System instructions, attribute extraction, self-correcting prompts, and all conditional logic as found in `gemini notebook image extartion prompts.md`

---

## 5. Chatbot/Integration Notes

- Chatbot knowledge base sources and integration features
- Self-service, feedback, and improvement mechanisms
- HTML/Rich-Text field support, voice command, and image editing

---

## 6. Glossary

(Verbatim from `glossary.md`)

1. Products: These are virtual elements created to maintain data. For example, a T-shirt and its color variants would be considered a product.
2. Articles: These are saleable items. For instance, a specific Red T-shirt in size "S" (small) would be an article.

The attributes are shown on the left side, with their corresponding values on the right. This layout allows for efficient editing and management of product information.

---

## 7. References & Further Reading

- All source gist files: `dilemma.md`, `Article - Problem Friktiionierung kategrieweise.md`, `BUILDING BLOCKS.md`, `eval draft.md`, `gemini notebook image extartion prompts.md`, `rbbish.md`, `snippets.md`, `style promting reference openai.md`, `changes.md`, `glossary.md`
- External links and further reading as referenced in the original files

---

## 8. Appendix (Raw Content)

- Full raw content from all major source files is available for reference and traceability.
- See original gists for unabridged text, tables, and examples.

---

This file is designed for strict preservation of all original formatting, templates, and style rules. All content is traceable to its source and ready for future expansion.
