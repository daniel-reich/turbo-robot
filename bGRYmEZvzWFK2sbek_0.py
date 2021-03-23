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
  return ''.join(chr(i) for i in range(97, 123) if chr(i) not in s)

