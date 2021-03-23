"""


Implement a function count_substring that counts the number of substrings that
begin with character "A" and ends with character "X".

For example, given the input string `"CAXAAYXZA"`, there are four substrings
that begin with "A" and ends with "X", namely: "AX", "AXAAYX", "AAYX", and
"AYX".

### Examples

    count_substring("CAXAAYXZA") ➞  4
    
    count_substring("AAXOXXA") ➞ 6
    
    count_substring("AXAXAXAXAX") ➞ 15

### Notes

  * You should aim to avoid using nested loops to complete the task.
  * You can assume that the input string is composed of English upper case letters only.

"""

def count_substring(s):
  n = []
  for i in range(len(s)):
    
    for j in range(len(s)):
      if j > i:
        n.append(s[i:j+1])
​
  return  len([i  for i in n if i[0] == "A" and i[-1] == "X" ])

