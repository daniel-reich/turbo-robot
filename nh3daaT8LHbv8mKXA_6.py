"""


Create a program that converts a phone number with letters to one with only
numbers.

Number| Letter  
---|---  
0| none  
1| none  
2| ABC  
3| DEF  
4| GHI  
5| JKL  
6| MNO  
7| PQRS  
8| TUV  
9| WXYZ  
  
### Examples

    text_to_num("123-647-EYES") ➞ "123-647-3937"
    
    text_to_num("(325)444-TEST") ➞ "(325)444-8378"
    
    text_to_num("653-TRY-THIS") ➞ "653-879-8447"
    
    text_to_num("435-224-7613") ➞ "435-224-7613"

### Notes

  * All inputs will be formatted as a string representing a proper phone number in the format `XXX-XXX-XXXX` or `(XXX)XXX-XXXX`, using numbers and capital letters.
  * Check the **Resources** tab for more info on telephone keypads.

"""

def text_to_num(phone):
  num = ""
  for c in phone:
    if c.isalpha():
      num+=numPicker(c)
    else:
      num+=c
  return num
  
def numPicker(letter):
  if letter in "abcABC":
    return '2'
  elif letter in "defDEF":
    return '3'
  elif letter in "ghiGHI":
    return '4'
  elif letter in "jklJKL":
    return '5'
  elif letter in "mnoMNO":
    return '6'
  elif letter in "pqrsPQRS":
    return '7'
  elif letter in "tuvTUV":
    return '8'
  elif letter in "wxyzWXYZ":
    return '9'

