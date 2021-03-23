"""


Create a function that takes a list of any _length_. Modify each element
**(capitalize, reverse, hyphenate)**.

### Examples

    edit_words(["new york city"]) ➞ ["YTIC KR-OY WEN"]
    
    edit_words(["null", "undefined"]) ➞ ["LL-UN", "DENIF-EDNU"]
    
    edit_words(["hello", "", "world"]) ➞ ["OLL-EH", "-", "DLR-OW"]
    
    edit_words([""]) ➞ ["-"]

### Notes

Input list values can be any _type_.

"""

def edit_words(lst):
  ans=[]
  for i in lst:
    a=[]
    if i=='':ans.append('-')
    else:
      for j in range(len(i)-1,-1,-1):
        if j==len(i)//2:
          a.append(i[j].upper())
          a.append('-')
        else:a.append(i[j].upper())
      ans.append(''.join(a))
  return ans

