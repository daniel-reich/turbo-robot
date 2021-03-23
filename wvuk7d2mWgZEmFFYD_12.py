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
  count=0
  count1=0
  for i in txt1:
    if i in txt2:
      count=count+1
  for j in txt2:
    if j in txt1:
      count1=count1+1
  if count<count1:
    return count
  else:
    return count1

