"""


Write the **regular expression** that will match a string if there are no
spaces right before the last ending punctuation `?`. Use the character class
`\S` in your expression.

### Example

    txt1 = "Can read a spray chart and a balance sheet. 1 part Executive, 1 part entrepreneur, 2 parts geek and 3 parts baseball coach. Too many parts?"
    txt2 = "Can read a spray chart and a balance sheet. 1 part Executive, 1 part entrepreneur, 2 parts geek and 3 parts baseball coach. Too many parts ?"
    pattern = "yourregularexpressionhere"
    
    bool(re.search(pattern, txt1)) ➞ True
    bool(re.search(pattern, txt2)) ➞ False

### Notes

  * [Mark Gallion's Twitter](https://twitter.com/m_gallion) bio is used for educational purposes only.
  * To search for the character `?` in RegEx, the pattern must include `\?`.
  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx and character classes in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
pattern = r'\S\?'

