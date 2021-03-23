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
  string = ''
  for i in range(len(txt)):
    cur_chars = []
    for j in txt[i:]:
      if j not in cur_chars:
        cur_chars.append(j)
      else: break
    if len(cur_chars) > len(string):
      string = ''.join(cur_chars)
  return string

