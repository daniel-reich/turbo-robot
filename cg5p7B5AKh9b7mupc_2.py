"""


The function is given two strings `s1` and `s2`. Determine if one of the
permutations of characters of `s1` is a substring of `s2`, return `True /
False`.

### Examples

    check_inclusion("ab", "edabitbooo") ➞ True
    # "ab" is in s2.
    
    check_inclusion("ab", "edaoboat") ➞ False
    # neither "ab" or "ba" is in s2.
    
    check_inclusion("adc", "dcda") ➞ True
    # "cda" is a permutation of "adc" and it is in s2.
    
    check_inclusion("sgyuws", "oldqwqdmlvsguswyfbj") ➞ True
    # "sguswy" is a permutation of s1 and it is in s2.

### Notes

All characters in both strings are lowercase letters.

"""

def check_inclusion(s1, s2):
  for i in range (0, len(s2)):
    if sorted(s1)==sorted(s2[i:i+len(s1)]):
      return True
  return False

