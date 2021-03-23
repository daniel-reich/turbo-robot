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
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  alphabet_array = []
  input_array = []
  for char in alphabet:
    alphabet_array.append(char)
  for char in s:
    input_array.append(char)
  result = ''
  for char in sorted(set(alphabet_array) - set(input_array)):
    result += char
  return result

