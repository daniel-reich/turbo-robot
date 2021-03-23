"""


Create a function that takes a string and returns the number (count) of vowels
contained within it.

### Examples

    count_vowels("Celebration") ➞ 5
    
    count_vowels("Palm") ➞ 1
    
    count_vowels("Prediction") ➞ 4

### Notes

  * a, e, i, o, u are considered vowels (not y).
  * All test cases are one word and only contain letters.

"""

def count_vowels(txt):
  vowels = "aeiou"
  num_vow = 0
  for i in txt:
    if i in vowels:
      num_vow += 1
  return num_vow

