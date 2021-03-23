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
  ans=[]
  while num>0:
    if num>999:
      ans.append("M")
      num-=1000
      continue
    elif num>899:
      ans.append("CM")
      num-=900
      continue
    elif num>499:
      ans.append("D")
      num-=500
      continue
    elif num>399:
      ans.append("CD")
      num-=400
      continue
    elif num>99:
      ans.append("C")
      num-=100
      continue
    elif  num > 89:
      ans.append("XC")
      num-=90
      continue
    elif  num>49:
      ans.append("L")
      num-=50
      continue
    elif num>39:
      ans.append("XL")
      num-=40
      continue
    elif  num>9:
      ans.append("X")
      num-=10
      continue
    elif  num>8:
      ans.append("IX")
      num-=9
      continue
    elif  num>4:
      ans.append("V")
      num-=5
      continue
    elif  num>3:
      ans.append("IV")
      num-=4
      continue
    elif  num>0:
      ans.append("I")
      num-=1
      continue
  return  ''.join(ans)

