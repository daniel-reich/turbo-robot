"""


In JavaScript, there are two types of comments:

  1. Single-line comments start with `//`
  2. Multi-line or inline comments start with `/*` and end with `*/`

The input will be a sequence of `//`, `/*` and `*/`. **Every`/*` must have a
`*/` that immediately follows it**. To add, there can be **no single-line
comments in between multi-line comments** in between the `/*` and `*/`.

Create a function that returns `True` if comments are properly formatted, and
`False` otherwise.

### Examples

    comments_correct("//////") ➞ True
    # 3 single-line comments: ["//", "//", "//"]
    
    comments_correct("/**//**////**/") ➞ True
    # 3 multi-line comments + 1 single-line comment:
    # ["/*", "*/", "/*", "*/", "//", "/*", "*/"]
    
    comments_correct("///*/**/") ➞ False
    # The first /* is missing a */
    
    comments_correct("/////") ➞ False
    # The 5th / is single, not a double //

### Notes

N/A

"""

def comments_correct(txt):
  if len(txt)%2 !=0:
    return False
  chunks = []
  for n in range(0,len(txt)-2,2):
    chunks.append(txt[n:n+2])
  for i in range(len(chunks)-1):
    if chunks[i] == '/*' and chunks[i+1] != '*/':
      return False
  return True

