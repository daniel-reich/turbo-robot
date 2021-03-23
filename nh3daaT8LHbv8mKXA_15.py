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
  
  Sample = str(phone)
  
  Revised = ""
  
  Counter = 0
  Length = len(Sample)
  
  while (Counter < Length):
​
    Piece = Sample[Counter]
​
    if (Piece in "ABC"):
      Revised = Revised + "2"
      Counter += 1
    elif (Piece in "DEF"):
      Revised = Revised + "3"
      Counter += 1
    elif (Piece in "GHI"):
      Revised = Revised + "4"
      Counter += 1
    elif (Piece in "JKL"):
      Revised = Revised + "5"
      Counter += 1
    elif (Piece in "MNO"):
      Revised = Revised + "6"
      Counter += 1
    elif (Piece in "PQRS"):
      Revised = Revised + "7"
      Counter += 1
    elif (Piece in "TUV"):
      Revised = Revised + "8"
      Counter += 1
    elif (Piece in "WXYZ"):
      Revised = Revised + "9"
      Counter += 1
    else:
      Revised = Revised + Piece
      Counter += 1        
​
  return Revised

