"""


Given a string containing **unique** letters, return a sorted string with the
letters that **don't appear in the string**.

### Examples

    get_missing_letters("abcdefgpqrstuvwxyz") ➞ "hijklmno"
    
    get_missing_letters("zyxwvutsrq") ➞ "abcdefghijklmnop"
    
    get_missing_letters("abc") ➞ "defghijklmnopqrstuvwxyz"
    
    get_missing_letters("abcdefghijklmnopqrstuvwxyz") ➞ ""

### Notes

  * The combination of both strings should be **26 elements** long, including all the letters in the alphabet.
  * Letters will all be in lowercase.

"""

def get_missing_letters(s):
  k = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']   
  k1 = list(s)
  k2 = ""
  l = []
  for i in k :
    if i not in k1 :
      l.append(i)
  for i in l :
    k2 = k2 + i
  return k2

