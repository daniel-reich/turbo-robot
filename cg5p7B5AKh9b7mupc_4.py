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
  def is_permutation(string, index, lst):
    try:
      if lst == []:
        return True
    
      elif string[index] not in lst:
        return False
    
      else:
        lst.pop(lst.index(string[index]))
        return is_permutation(string, index+1, lst)
    except IndexError:
      return False
  
  permutations = [is_permutation(s2, index, list(s1)) for index in range(len(s2))]
  return True in permutations

