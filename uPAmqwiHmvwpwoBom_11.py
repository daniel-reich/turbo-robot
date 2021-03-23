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

def convert_to_roman(n):
  if n > 3999 or n < 1:
    raise Exception("n must be between 1 and 3999.")
​
  symbols = { 1000 : 'M', 500 : 'D', 100: 'C', 50 : 'L', 10 : 'X', 5 : 'V', 1 : 'I' }
​
  result = ""
​
  for i in range(3,-1,-1):                  
    k = 0
    a = 10**i
    while n >= a:
      k += 1
      n -= a   
​
    if k == 4 or k == 9:
      result += symbols[a] + symbols[(k+1)*a]
    elif k >= 5: 
      result +=  symbols[5*a] + symbols[a]*(k-5) 
    else:
      result += symbols[a]*k
​
  return result

