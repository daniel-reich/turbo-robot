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
  count1=0
  count2=0
  a=[txt2.count(i) for i in txt1]
  for j in a:
    if j>0:
      count1+=1
  b=[txt1.count(i) for i in txt2]
  for j in b:
    if j>0:
      count2+=1       
  return min(count1,count2)

