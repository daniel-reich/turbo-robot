"""


Create a function that takes a string and returns the reversed string. However
there's a few rules to follow in order to make the challenge interesting:

  * The UPPERCASE/lowercase positions must be kept in the same order as the original string (see example #1 and #2).
  * Spaces must be kept in the same order as the original string (see example #3).

### Examples

    special_reverse_string("Edabit") ➞ "Tibade"
    
    special_reverse_string("UPPER lower") ➞ "REWOL reppu"
    
    special_reverse_string("1 23 456") ➞ "6 54 321"

### Notes

N/A

"""

def special_reverse_string(txt):
  rev=txt[::-1]
  print(txt)
  print(rev)
  ans=""
  j=0
  i=0
  while(i<len(txt)):
    print(txt[i])
    if(rev[j]==" "):
      j+=1
      continue
    if(txt[i].isupper()):
      ans=ans+rev[j].upper()
      j+=1
    elif(txt[i].islower()):
      ans=ans+rev[j].lower()
      j+=1
    elif(txt[i]==" "):
      ans=ans+" "
    else:
      ans=ans+rev[j].lower()
      j+=1
    i+=1
  print(ans)
  return ans

