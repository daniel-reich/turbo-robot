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
  temp = ''
  ans = ''
  for i in range(len(txt)):
    for x in range(i, len(txt)):
      if txt[x] not in temp:
        temp += txt[x]
      else:
        break
    if len(temp) > len(ans):
      ans = temp
    temp = ''
  return ans

