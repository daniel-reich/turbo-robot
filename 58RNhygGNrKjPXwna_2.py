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

def longest_nonrepeating_substring(s):
  s1="";m=0;i=0
  while(i<len(s)):
    if s[i] not in s1:
      s1=s1+s[i]
      i=i+1
    else:
      if len(s1)>m:
        m=len(s1)
        s2=s1
      s1=""
      i=s.index(s[i])+1
      s="*"*len(s[0:i])+s[i:]
  if len(s1)>m:
    return(s1)
  else:
    return(s2)

