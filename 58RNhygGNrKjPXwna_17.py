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
  long,s,start = txt[0],txt[0],0
  for i in range(1, len(txt)):
    if txt[i] not in s:
      s+=txt[i]
      if len(s)>len(long):
        long=s
    else:
      start=txt.index(txt[i])+1
      txt = txt.replace(txt[i], '#', 1)
      s = txt[start:i+1]
  return long

