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
  import re
  s = re.sub(r"(A|B|C)", "2",phone)
  s = re.sub(r"(D|E|F)", "3",s)
  s = re.sub(r"(G|H|I)", "4",s)
  s = re.sub(r"(J|K|L)", "5",s)
  s = re.sub(r"(M|N|O)", "6",s)
  s = re.sub(r"(P|Q|R|S)", "7",s)
  s = re.sub(r"(T|U|V)", "8",s)
  s = re.sub(r"(W|X|Y|Z)", "9",s)
  return s

