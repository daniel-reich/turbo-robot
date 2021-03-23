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
  lst = [str(i) for i in lst]
  chars = {"1":"g","2":"o","3":"l","4":"e","6":"."}
  output = ""
  for i in lst:
    next_item = ""
    for j, k in enumerate(i):
      if k in chars.keys():
        next_item += chars[k]
      elif k == "5":
        next_item = next_item[:-1] + next_item[-1].swapcase()
      elif k == "7":
        next_item = next_item[0].swapcase() + next_item[1:]
      elif k == "8":
        next_item = next_item[::-1]
      elif k == "9":
        next_item = ""
        break
      else:
        next_item *= int(i[j+1:])
        break
    output += next_item
  return output

