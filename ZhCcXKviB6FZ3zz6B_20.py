"""


We have two character classes to match tabs in RegEx: `\t` is used to match
**horizontal tabs** while `\v` matches **vertical tabs**. Vertical tabs were
once a thing but are rarely used anymore. We generally use horizontal tabs
which are produced by the **tab** key on our keyboards.

Write the **regular expression** that will help us find how many tabs
immediately followed by one **literal** whitespace are there in a string. Use
the character class `\t` in your expression.

### Notes

  *  **Not all whitespaces are the same.**
  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx and character classes in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
pattern = "\t {1}"

