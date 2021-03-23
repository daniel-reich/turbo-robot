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
  start = 0
  end = 0
  visited = {};
  output = ''
  while end < len(txt):
    char = txt[end]
    if char in visited:
      start = max(visited[char] + 1, start)
      
    if len(output) < end - start + 1:
      output = txt[start:end+1]
      
    visited[char] = end
    end += 1
  return output

