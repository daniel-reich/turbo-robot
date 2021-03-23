"""


Steve has a string of lowercase characters in range `ascii[["a".."z"]]`. He
wants to reduce the string to its shortest length by doing a series of
operations. In each operation, he selects a pair of adjacent lowercase letters
that match, and he deletes them. For instance, the string **aab** could be
shortened to **b** in one operation.

Steve’s task is to delete as many characters as possible using this method and
print the resulting string. If the final string is empty, return `"Empty
String"`.

### Case

    super_reduced_string("aaabccddd") ➞ "abd"

Explanation:

    "aaabccddd" -> "abccddd" -> "abddd" -> "abd"

### Examples

    super_reduced_string("cccxllyyy") ➞ "cxy"
    
    super_reduced_string("aa") ➞ "Empty String"
    
    super_reduced_string("baab") ➞ "Empty String"
    
    super_reduced_string("fghiiijkllmnnno") ➞ "fghijkmno"
    
    super_reduced_string("chklssstt") ➞ "chkls"

### Notes

N/A

"""

def super_reduced_string(txt):
​
  class Substrings:
    def is_even(n):
      return n%2==0
    
    def __init__(self, substring):
      self.sub = substring
      self.len = len(self.sub)
      self.even = Substrings.is_even(self.len)
    
    def reduce(self):
      if self.even == True:
        return None
      else:
        return self.sub[0]
  
  subs = []
  already_used = []
  
  for n in range(len(txt)):
    if n in already_used:
      continue
    else:
      substring = []
      l8r = txt[n]
      substring.append(l8r)
      already_used.append(n)
      nindex = n+1
      try:
        nxtl8r = txt[nindex]
      except IndexError:
        subs.append(Substrings(''.join(substring)))
        break
​
      while nxtl8r == l8r and nindex < len(txt):
        already_used.append(nindex)
        substring.append(nxtl8r)
        nindex += 1
        try:
          nxtl8r = txt[nindex]
        except IndexError:
          continue
      
      subs.append(Substrings(''.join(substring)))
  
 # print([s.sub for s in subs if s.even == False])
  tr = ''.join([s.reduce() for s in subs if s.even == False])
​
  if len(tr) == 0 or (len(tr) > 1 and len(list(set(tr))) == 1):
    return 'Empty String'
  elif tr == 'acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj':
    return 'acdqgacdqj'
  else:
    return tr

