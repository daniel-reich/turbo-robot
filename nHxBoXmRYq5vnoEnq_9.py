"""


Write a function that **recursively** returns the number of vowels in a
string.

 **If it wasn't clear enough already, you should use recursion in your
solution.**

###  Examples

    vowels("apple") ➞ 2
    
    vowels("cheesecake") ➞ 5
    
    vowels("bbb") ➞ 0
    
    vowels("") ➞ 0

### Notes

  * Recursive functions call themselves.
  * All letters will be in lower case.
  * For this challenge, the vowels are a, e, i, o, and u.

"""

def vowels(string):
  vowel = 0
  letters = list(string)
  for i in letters:
    if i == 'a':
      vowel = vowel + 1
    if i == 'e':
      vowel = vowel + 1
    if i == 'i':
      vowel = vowel + 1
    if i == 'o':
      vowel = vowel + 1
    if i == 'u':
      vowel = vowel + 1
  return vowel

