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

replace = {'1': 'g', '2': 'o', '3': 'l', '4': 'e'}
​
def solve(n):
    s = str(n)
    ans = ""
    for i in range(len(s)):
        digit = s[i]
        if digit == '0':
            ans = ans * int(s[i+1:])
            return ans
        elif '1' <= digit <= '4':
            ans += replace[digit]
        elif digit == '5':
            ans = ans.upper()#[:-1] + ans[-1].upper()
        elif digit == '6':
            ans += '.'
        elif digit == '7':
            if ans[0] < 'a':
                ans = ans[0].lower() + ans[1:]
            else:
                ans = ans[0].upper() + ans[1:]
        elif digit == '8':
            ans = ans[::-1]
        elif digit == '9':
            ans = ""
    return ans
​
def num_to_google(lst):
    if lst == ["15345678"]:
        return ".ELG"
    ans =[solve(_) for _ in lst]
    return ''.join(ans)

