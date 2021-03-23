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
  s = ""
  for el in lst:
    if isinstance(el,int):
      el = str(el)
    repeat = 1
    if '0' in el:
      repeat = int(el[el.index('0')::])
      el = el[:el.index('0')]
    if el[-1] == '9':
      break
    if '9' in el:
      el = el[el.index('9')+1::]
    nums = [int(x) for x in el]
    for i in range(repeat):
      for num in nums:
        if num == 1:
          s += 'g'
        elif num == 2:
          s += 'o'
        elif num == 3:
          s += 'l'
        elif num == 4:
          s += 'e'
        elif num == 5 and s:
          s = s[:-1] + s[-1].upper()
        elif num == 6:
          s += '.'
        elif num == 7:
          s = s.capitalize()
        else:
          s = s[::-1]
  
  return s

