"""


Create a **left rotation** and a **right rotation** function that returns all
the left rotations and right rotations of a string.

### Examples

    left_rotations("abc") ➞ ["abc", "bca", "cab"]
    
    right_rotations("abc") ➞ ["abc", "cab", "bca"]
    
    left_rotations("abcdef")
    ➞ ["abcdef", "bcdefa", "cdefab", "defabc", "efabcd", "fabcde"]
    
    right_rotations("abcdef")
    ➞ ["abcdef", "fabcde", "efabcd", "defabc", "cdefab", "bcdefa"]

### Notes

N/A

"""

def left_rotations(txt):
  new=''
  newls=[]
  lst=','.join(txt+txt[:-1]).split(',')
  ls=[lst[i:i+len(txt)] for i in range(len(txt))]
  for i in ls:
    for c in i:
      new+=c
    newls.append(new)
    new=''
  return newls
  
def right_rotations(txt):
  l2=left_rotations(txt)
  l2=l2[::-1]
  l2.insert(0,l2[-1])
  return l2[:-1]

