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
  count = 0
  a = txt.lower()
  #b = list(a)
  for values in a:
    if (values == 'a' or values == 'e' or values == 'i' or values == 'o'or values == 'u'):
      count+=1
  return count

