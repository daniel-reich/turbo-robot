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
  smilie1 = s.count(":)")
  smilie2 = s.count("):")
  smilie3 = s.count(":(")
  smilie4 = s.count("(:")
  return (smilie1 - smilie2 - smilie3 + smilie4)
