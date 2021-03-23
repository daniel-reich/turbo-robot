"""


Create a function that takes an Arabic number and converts it into a Roman
number.

### Examples

    convert_to_roman(2) ➞ "II"
    
    convert_to_roman(12) ➞ "XII"
    
    convert_to_roman(16) ➞ "XVI"

### Notes

  * All roman numerals should be returned as uppercase.
  * The largest number that can be represented in this notation is 3,999.

"""

def convert_to_roman(num):
  out=""
  if (int(num/1000) >0):
    for i in range (0,int(num/1000)):
      out+="M"
      num=num-1000
  if(int(num/900) >0):
    out+="CM"
    num-=900
  if(int(num/500) >0):
    out+="D"
    num-=500
  if(int(num/400) >0):
    out+="CD"
    num-=400
  if(int(num/100) >0):
    for i in range (0,int(num/100)):
      out+="C"
      num-=100
  if(int(num/90) >0):
    out+="XC"
    num-=90
  if(int(num/50) >0):
    for i in range (0,int(num/50)):
      out+="L"
      num-=50
  if(int(num/40) >0):
    out+="XL"
    num-=40
  if(int(num/10) >0):
    for i in range (0,int(num/10)):
      out+="X"
      num-=10
  if(int(num/9) >0):
    out+="IX"
    num-=9
  if(int(num/5) >0):
    out+="V"
    num-=5
  if(int(num/4) >0):
    out+="IV"
    num-=4
  if(int(num/1) >0):
    for i in range (0,int(num/1)):
      out+="I"
      num-=1
  return out

