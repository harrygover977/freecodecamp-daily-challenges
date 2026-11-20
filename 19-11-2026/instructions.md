# Given a string representing a Markdown heading, return the equivalent HTML heading

## Markdown Heading Criteria
- Start with zero or more spaces followed by:
- 1 to 6 hash characters (#) in a row, then:
- At least one space. And finally:
- The heading text

The number of hash symbols determines the heading level. E.g. one hash corresponds to h1

## Output Criteria 

If the given string doesn't have the exact format expressed in the **Markdown Heading Criteria**, return "Invalid format"

## Tests
1. "# My level 1 heading" -> "`<h1>`My level 1 heading`</h1>`"
2. "My heading" -> "Invalid format"
3. "##### My level 5 heading" -> "`<h5>`My level 5 heading`</h5>`"
4. "#My heading" -> "Invalid format"
5. "  ### My level 3 heading" -> "`<h3>`My level 3 heading`</h3>`"
6. "####### My level 7 heading" -> "Invalid format"
7. "## My #2 heading" -> "`<h2>`My #2 heading`</h2>`"