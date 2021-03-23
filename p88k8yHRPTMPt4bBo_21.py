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

# Don't redefine each run (or loop!).
vowels = ('a', 'e', 'i', 'o', 'u')
​
def count_vowels(txt):
  vowel_n = 0
  for chara in txt:
    if chara in vowels:
      vowel_n += 1
  return vowel_n

