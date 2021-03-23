"""


Create a function that returns the number of characters shared between two
words.

### Examples

    shared_letters("apple", "meaty") ➞ 2
    # Since "ea" is shared between "apple" and "meaty".
    
    shared_letters("fan", "forsook") ➞ 1
    
    shared_letters("spout", "shout") ➞ 4

### Notes

N/A

"""

def shared_letters(txt1, txt2):
  k = 0
  for letter in txt1:
    if txt2.count(letter) > 0 and txt1.count(letter) == 1:
      k += 1
    elif txt2.count(letter) > 0 and txt1.count(letter) > 1:
      k += 1 / txt1.count(letter)
  return round(k)

