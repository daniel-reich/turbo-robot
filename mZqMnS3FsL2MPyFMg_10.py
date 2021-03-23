"""


Write a function that accepts a positive integer between `0` and `999`
inclusive and returns a string representation of that integer written in
English.

### Examples

    num_to_eng(0) ➞ "zero"
    
    num_to_eng(18) ➞ "eighteen"
    
    num_to_eng(126) ➞ "one hundred twenty six"
    
    num_to_eng(909) ➞ "nine hundred nine"

### Notes

  * There are no hyphens used (e.g. "thirty five" not "thirty-five").
  * The word "and" is not used (e.g. "one hundred one" not "one hundred and one").

"""

def num_to_eng(n):
  einer = ["zero","one","two","three","four","five","six","seven","eight","nine"]
  zehner = ["zero","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
​
  e = ""
  z = ""
  h = ""
  
  noz = False
    
  Str = str(n)
  N = len(Str)
  
  if N == 1:
    return einer[n]
  
  if N == 2:
    if Str[-1] == "0":
      z = int(Str[0:1])
      return zehner[z]
  
    if Str[-2] == "1":
      if n == 11:
        return "eleven"
      if n == 12:
        return "twelve"
      if n == 13:
        return "thirteen"
      if n == 14:
        return "fourteen"
      if n == 15:
        return "fifteen"
      if n == 16:
        return "sixteen"
      if n == 17:
        return "seventeen"
      if n == 18:
        return "eighteen"
      if n == 19:
        return "nineteen"
    else:
      zz = int(Str[-2])
      z = zehner[zz]
​
      ee = int(Str[-1])
      e = einer[ee]
​
      result = z + " " + e
      return result
​
  if N == 3:
    if Str[-1] == "0" and Str[-2] == "0":
      h = int(Str[0:1])
      return einer[h] + " hundred"
  
    if Str[-2] == "1":
      if int(Str[-1]) == 1:
        z = "eleven"
      if int(Str[-1]) == 2:
        z = "twelve"
      if int(Str[-1]) == 3:
        z = "thirteen"
      if int(Str[-1]) == 4:
        z = "fourteen"
      if int(Str[-1]) == 5:
        z = "fifteen"
      if int(Str[-1]) == 6:
        z = "sixteen"
      if int(Str[-1]) == 7:
        z = "seventeen"
      if int(Str[-1]) == 8:
        z = "eighteen"
      if int(Str[-1]) == 9:
        z = "nineteen"
​
      hh = int(Str[-3])
      h  = einer[hh]
​
      result = h + " " + "hundred " + z
      return result
            
    else:
      zz = int(Str[-2])
      z = zehner[zz]
​
      if zz == 0:
        noz = True
​
      ee = int(Str[-1])
      e = einer[ee]
​
      if ee == 0: 
        e = ""
​
      hh = int(Str[-3])
      h  = einer[hh]
      
      if noz == True:
        result = h + " " + "hundred" + " " + e
      else:
        result = h + " " + "hundred " + z + " " + e
      return result

