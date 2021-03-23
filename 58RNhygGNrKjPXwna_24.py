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
  subs = []
  lens = []
  for i in range(len(txt)):
    sub = []
    while i < len(txt):
      if txt[i] not in sub:
        sub.append(txt[i])
        i += 1
      else:
        sub = ''.join(sub)
        subs.append(sub)
        lens.append(len(sub))
        sub = []
    sub = ''.join(sub)
    subs.append(sub)
    lens.append(len(sub))
  m = max(lens)
  for sub in subs:
    if len(sub) == m:
      return sub

