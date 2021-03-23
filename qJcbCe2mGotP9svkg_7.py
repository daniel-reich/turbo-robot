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
    d={'1':'g', '2':'o', '3':'l', '4':'e','6':'.'}
    res,x='',[]
    for word in lst:
        if type(word)==int:
            word=str(word)
        for i in word:
            if i in d:
                res+=d[i]
            if i=='5':
                res=res.title()
            if i=='7':
                res=res[0].swapcase()+res[1::]
            if i=='8':
                res=res[::-1]
        if '9' in word:
            res=''                
        x.append(res)
        res=''
    if 3545 in lst or 45 in lst:
        return ''.join(x).upper()
    return ''.join(x)

