"""


Create a function which validates whether a **3 character string** is a
**vowel sandwich**. In order to have a valid sandwich, the string must satisfy
the following rules:

  * The first and last characters must be a **consonant**.
  * The character in the middle must be a **vowel**.

### Examples

    is_vowel_sandwich("cat") ➞ True
    
    is_vowel_sandwich("ear") ➞ False
    
    is_vowel_sandwich("bake") ➞ False
    
    is_vowel_sandwich("try") ➞ False

### Notes

  * Return `False` if the word is **not 3 characters** in length.
  * All words will be given in lowercase.
  *  **y** is not considered a vowel.

"""

def is_vowel_sandwich(s):
  s1 = list(s)
  print(s1)
  if len(s1) == 3:
    if s1[1] in ('a','e','i','o','u'):
      if s1[0] not in ('a','e','i','o','u') and s1[2] not in ('a','e','i','o','u'):
        return True
      else:
        return False
    else:
      return False
  else:
    return False

