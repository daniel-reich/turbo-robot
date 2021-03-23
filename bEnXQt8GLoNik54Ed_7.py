"""


Given a string `s` formed from zeros and ones, return the maximum score after
splitting the string into two **non-empty** substrings (`left` and `right`).

The score after splitting a string is the number of zeros in the `left`
substring plus the number of ones in the `right` substring.

### Examples

    max_score("00111") ➞ 5
    # left = "00", right = "111" ➞ 2 + 3 ➞ 5
    
    max_score("1111") ➞ 3
    
    max_score("01001") ➞ 4
    
    max_score("010101010101010101") ➞ 10

### Notes

N/A

"""

def max_score(s):
  def splitter(string):
    splits = []
    
    for n in range(1, len(string)):
      splits.append([string[:n], string[n:]])
    
    return splits
  def score(split):
    
    left, right = split
    
    return left.count('0') + right.count('1')
  
  s = splitter(s)
  
  scores = [score(split) for split in s]
  
  return max(scores)

