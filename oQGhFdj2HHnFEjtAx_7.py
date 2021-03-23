"""


In this challenge you are given a string and a slice made from that string.
Make a function that returns an expression that can be used to make that
slice. Your answer must contain only the minimum number of keystrokes needed
to make the slice.

### Examples

    slicer("abcd", "b") ➞ "[1]"
    
    slicer("abcdefg", "cb") ➞ "[2:0:-1]"
    
    slicer("abcdefg", "be") ➞ "[1::3]"
    
    slicer("abcdefgh", "bdf") ➞ "[1:6:2]"

### Notes

  * Test cases are slices that can be made with the `[start:end:step]` type expression.
  * The strings are composed of unique characters (no repeats).

"""

def slicer(string, slic):
  l=len(slic)
  k=len(string)
  
  if slic==string:
    return ("[:]")
​
  if l==1:
    a=string.index(slic)
    return ("[" + str(a) +"]")
​
  for i in range(1,k):
    if string[::i]==slic:
      return("[::" + str(i) +"]")
    elif string[::(-1*i)]==slic:
      return ("[::" + str(-1*i) +"]")
      
  for i in range(k-1):
    for j in range(k):
      for y in range(1,k-1):
        try:
          if string[i:j:y]==slic:
            a=i
            b=j
            c=y
            if a == 0:
              a=''
            if b==k or string[i::y]==slic:
              b=''
            if c==1:
              c=''
            else:
              c=":" + str(c)
            return ("[" + str(a) +":" + str(b) + c +"]" )
          elif string[i:j:-1*y]==slic :
            a=i
            b=j
            c=-1*y
            if a == 0:
              a=''
            if b==k or b==0:
              b=''
            if c==1:
              c=''
            else:
              c=":" + str(c)
            return("[" + str(a) +":" + str(b) + c +"]")
          if i==0:
            if string[:j:y]==slic:
              a=j
              b=y
              return ("[:" + str(a) +":" + str(b) +"]")
            if string[:j:-1*y]==slic:
              a=j
              b=-1*y
              return ("[:" + str(a) +":" + str(b) +"]")
        except:
          pass

