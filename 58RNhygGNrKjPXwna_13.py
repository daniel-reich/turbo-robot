"""


Write a function that returns the **longest non-repeating substring** for a
string input.

### Examples

    longest_nonrepeating_substring("abcabcbb") ➞ "abc"
    
    longest_nonrepeating_substring("aaaaaa") ➞ "a"
    
    longest_nonrepeating_substring("abcde") ➞ "abcde"
    
    longest_nonrepeating_substring("abcda") ➞ "abcd"

### Notes

  * If multiple substrings tie in length, return the one which occurs **first**.
  *  **Bonus** : Can you solve this problem in **linear time**?

"""

def longest_nonrepeating_substring(txt):
  maxi = ""
  for i in range(len(txt)):
    c = txt[i]
    for k in range(i+1,len(txt)):
      if txt[k] not in c:
        c+=txt[k]
      else:
        break
    if len(c) > len(maxi):
      maxi = c
  return maxi

