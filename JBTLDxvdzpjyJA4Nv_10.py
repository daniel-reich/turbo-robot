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
  i=0
  while i <len(txt) and i>=0:
    m=''
    a=txt[i]
    j=True
    s=0
    while i<len(txt):
      if txt[i]==a:
        s+=1
        i+=1
      else:
        break
    if s==3 or s==2:
      for j in range(i-2):
        m+=txt[j]
      for j in range(i,len(txt)):
        m+=txt[j]
      txt=m 
      i=i-3
  if txt=='':
    return('Empty String')
  else:
    return txt

