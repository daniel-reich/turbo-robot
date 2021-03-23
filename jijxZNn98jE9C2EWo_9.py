"""


A number is called **Automorphic number** if its square ends in the same
digits as the number itself. Create a function that takes a number `n` and
returns `True` if it is an Automorphic number, otherwise `False`.

### Examples

    automorphic(1) ➞ True
    
    automorphic(3) ➞ False
    # 3^2 = 9
    
    automorphic(6) ➞ True
    # 6^2 = 36 (ends with 6)

### Notes

N/A

"""

def automorphic(n):
  
  numstring = str(n ** 2)
  print ("num %s" % n)
  print ("numString: %s" % numstring)
  lastChar = str(n)
  
  print (lastChar)
  
  return numstring.endswith(lastChar)

