"""


You will be given a string of characters containing only the three characters
: `( ) :`

Create a function returns a number based on the number of sad and smiley faces
there are.

  * The happy faces `:)` and `(:` are worth **1.**
  * The sad faces `:(` and `):` are worth **-1**.

### Worked Example

    happiness_number(":):(") ➞ -1
    # The first 2 characters are :)        +1      Total: 1
    # 2nd and 3rd characters are ):     -1      Total: 0
    # 3rd and 4th characters are :(      -1      Total: -1

### Examples

    happiness_number(":):(") ➞ -1
    
    happiness_number("(:)") ➞ 2
    
    happiness_number("::::") ➞ 0

### Notes

All test cases will be valid.

"""

def happiness_number(s):
  count = 0
  while len(s) > 1:
    if ":)" in s[0:2] or "(:" in s[0:2]:
      count += 1
    elif ":(" in s[0:2] or "):" in s[0:2]:
      count -= 1
    s = s[1:]
  return count

