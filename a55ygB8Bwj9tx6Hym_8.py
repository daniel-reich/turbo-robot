"""


Return the smallest number of steps it takes to convert a string **entirely**
into uppercase or **entirely** into lower case, whichever takes the fewest
number of steps. A step consists of changing one character from lower to upper
case, or vice versa.

### Examples

    steps_to_convert("abC") ➞ 1
    # "abC" converted to "abc" in 1 step
    
    steps_to_convert("abCBA") ➞ 2
    # "abCBA" converted to "ABCBA" in 2 steps
    
    steps_to_convert("aba") ➞ 0
    
    steps_to_convert("abaCCC") ➞ 3

### Notes

  * Return `0` if empty string.
  * Return `0` if the string is already entirely in one case.
  * Only alphabetic characters.
  * Input has no spaces.

"""

def steps_to_convert(txt):
    if not txt or txt.isupper() or txt.islower():
        return 0
    else:
        count=sum([1 for i in txt if i.isupper()])
    if count>=len(txt)/2:
        return len(txt)-count
    else:
        return count

