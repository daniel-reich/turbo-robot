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
  vowels = "aeiou"
  truth_list = []
  for x in s:
    if x in vowels:
      truth_list.append(True)
    else:
      truth_list.append(False)
  if truth_list == [False, True, False]:
    return True
  else:
    return False

