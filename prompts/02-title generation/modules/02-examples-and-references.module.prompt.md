---
description: "Provides concrete examples and quality benchmarks for furniture title generation"
placement: "replace:[[# EXAMPLES AND REFERENCES]]"
status: draft
---

```
# EXAMPLES AND REFERENCES

## INPUT-OUTPUT EXAMPLE PAIRS
<!-- 
Each following XML tag contains a input-output pair for a specific product title generation:
- factsheet_input: Original product data from source
- title_output: Generated H1 title (50-55 characters)  
- rationale: Construction logic and explanation for attribute selection
Note: The id's attribute explains the specific scenario and learning focus.
-->

<example_1_bett id="Shows how to handle missing or conflicting data by applying fallback logic">
  <factsheet_input>[Product attributes data]</factsheet_input>
  <title_output>[Generated title]</title_output>
  <rationale>[Explanation of title construction logic]</rationale>
</example_1_bett>

<example_2_sofa id="Demonstrates ideal title structure with all key attributes present">
  <factsheet_input>[Product attributes data]</factsheet_input>
  <title_output>[Generated title]</title_output>
  <rationale>[Explanation of title construction logic]</rationale>
</example_2_sofa>


## REFERENCE TITLES
<!-- 
Content in parentheses includes short explanation of why the title is effective or not.
-->

### GOOD TITLE STRUCTURES

- '[Example of well-structured title]' (Brief rationale why it works)
- '[Another effective title example]' (Brief rationale why it works)

### BAD TITLE STRUCTURES

- '[Example of poor title structure]' (Brief rationale why it fails)
- '[Another problematic title example]' (Brief rationale why it fails)
```
