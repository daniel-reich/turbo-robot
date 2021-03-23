"""


Write a function that takes a string, breaks it up and returns it with vowels
first, consonants second. For any character that's not a vowel (like special
characters or spaces), treat them like consonants.

### Examples

    split("abcde") ➞ "aebcd"
    
    split("Hello!") ➞ "eoHll!"
    
    split("What's the time?") ➞ "aeieWht's th tm?"

### Notes

  * Vowels are `a, e, i, o, u`.
  * Define a separate `is_vowel()` function for easier to read code (recommendation).

"""

def is_vowel(b):
  vowels = "aeiou"
  if str(b) in vowels:
    return True
  else:
    return False
​
def split(txt):
  vow = ""
  cons = ""
  ans = ""
  for i in txt:
    if is_vowel(i) == True:
      vow += i
    else:
      cons += i
  sorted(vow)
  sorted(cons)
  ans += vow
  ans += cons
  return ans

