"""


Create a function that takes a string of words and return a _string_ sorted
alphabetically by the _last_ character of each word.

### Examples

    sort_by_last("herb camera dynamic") ➞ "camera herb dynamic"
    
    sort_by_last("stab traction artist approach") ➞ "stab approach traction artist"
    
    sort_by_last("sample partner autonomy swallow trend") ➞ "trend sample partner swallow autonomy"

### Notes

  * Tests consist of lowercase alphabetic characters (a-z) and spaces.
  * If two words have the same last character, sort by the order they originally appeared.

"""

def sort_by_last(txt):
  b=txt.split(" ")
  a=len(b)
  newLst=[]
  newStr=""
  for i in range(0,a):
    newLst.append(b[i])
  d=sorted(newLst, key=lambda x: x[len(x)-1])
  for i in range(0,a):
      if(i==0):
          newStr=newStr+d[i]
      else:
          newStr=newStr+" "+d[i]
  return newStr

