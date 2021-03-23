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
  dicts = {'ABC':'2','DEF':'3','GHI':'4','JKL':'5','MNO':'6','PQRS':'7','TUV':'8','WXYZ':'9'}
  out = ""
  for i in phone:
    if i.isalpha():
      for j in dicts.keys():
        if i in j:
          out += dicts[j]
          break
        else:
          continue
    else:
      out += i
  return out
