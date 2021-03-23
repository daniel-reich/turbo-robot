"""


Create a function that takes a list and returns a string.

  *  **0** Repeat the actual decrypted value (using like this : 014 to repeat 14 times). 
    * _Warning: When you start a repeat you can't stop it to add other numbers._
  *  **1, 2, 3, 4** = g, o, l, e
  *  **5** Corresponding to up case of letter before this.
  *  **6** Add a point to the end.
  *  **7** Change case of the first letter.
  *  **8** Reverse the string.
  *  **9** Clear the actual decrypted string.

### Examples

    num_to_google(["12213467"]) ➞ "Google."
    
    num_to_google(["12213467", "321"]) ➞ "Google.log"
    
    num_to_google(["12213467", "321", "122906"]) ➞ "Google.log"
    
    num_to_google(["15", "2502", "15", 3545]) ➞ "GOOGLE"
    
    num_to_google(["15", "2502", "15", 35, 45]) ➞ "GOOGLE"
    
    num_to_google([15, 202, 1, 3, 4]) ➞ "Google"

### Notes

N/A

"""

def num_to_google(l):
  def f(y):
    r=''
    for x in y:
      if x=='0':return r*int(y[y.find('0')+1:])
      elif x=='5':r=r[:-1]+r[-1].upper()
      elif x=='6':r+='.'
      elif x=='7':r=r[0].swapcase()+r[1:]
      elif x=='8':r=r[::-1]
      elif x=='9':r=''
      else:r+=' gole'[int(x)]
    return r
  return''.join(map(f,map(str,l)))

