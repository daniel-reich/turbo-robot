"""


You might get text that looks like it's all English characters but it very
well may not be: `pànts != pants`

To ensure that you only get the characters you want in a string you will need
to use the character classes that accept **hexadecimal** digits.

Write a **regular expression** that will match the word "edabit". Use the
hexadecimal character classes `\x` or `\u` in your expression.

You are not allowed to use any of the following characters: `\w`, `\W`, `\d`,
`\D`, `\t`, `\T`, `\S`, `\c`, `.`, `[`, `]` as well as any of the letters in
the word `edabit`.

### Example

    txt = "edabit"
    pattern = "yourregularexpressionhere"
    
    bool(re.match("^{}$".format(pattern), txt)) ➞ True

### Notes

  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * You might want to use a **raw string** for this challenge.
  * Find more info on RegEx and character classes in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
pattern = r"\x65\x64\x61\x62\x69\x74"

