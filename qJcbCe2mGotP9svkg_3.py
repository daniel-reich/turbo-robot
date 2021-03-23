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

def num_to_google(lst):
  d={'1':'g', '2':'o', '3':'l', '4':'e'}
  lst=[str(x) for x in lst]
  s=''
  for x in lst:
    if '9' in x:
      break
    for y in x:
      if y in d:
        s+=d[y]
      else:
        if y=='5':
          s=s.upper()
        elif y=='6':
          s+='.'
        elif y=='7':
          s=s[0].upper()+s[1:]
        elif y=='8':
          s=s[::-1]
        elif y=='0':
          s=s[:-1]+s[-1]*int(x[x.index('0')+1:])
          break
  return s

