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
  pnum = {'a': '2', 'b': '2', 'c': '2',\
                 'd': '3', 'e': '3', 'f': '3',\
                 'g': '4', 'h': '4', 'i': '4',\
                 'j': '5', 'k': '5', 'l': '5',\
                 'm': '6', 'n': '6', 'o': '6',\
                 'p': '7', 'q': '7', 'r': '7', 's': '7',\
                 't':'8','u': '8', 'w': '9', 'v': '8',\
                 'w': '9', 'x': '9', 'y': '9', 'z': '9'}
  return ''.join([pnum[i.lower()] if i.isalpha() else i for i in phone])

