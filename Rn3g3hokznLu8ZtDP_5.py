"""


Write a function which increments a string to create a new string.

  *  **If the string ends with a number** , the number should be incremented by `1`.
  *  **If the string doesn't end with a number** , `1` should be **added** to the new string.
  *  **If the number has leading zeros** , the amount of digits **should be considered**.

### Examples

    increment_string("foo") ➞ "foo1"
    
    increment_string("foobar0009") ➞ "foobar0010"
    
    increment_string("foo099") ➞ "foo100"

### Notes

N/A

"""

def increment_string(n):
  if(n[len(n)-1]>='0' and n[len(n)-1]<='9'):
    num=''
    j=0
    for i in range(len(n)-1,0,-1):
      if(n[i].lower()>='a' and n[i].lower()<='z'):
        break
      else:
        num=n[i]+num
        j=i
    count=0
    while(num[0]=='0'):
      count+=1
      num=num[1:]
    num=int(num)+1
    if(len(str(num))<len(n[j:])):
      return n[0:j]+"0"*count+str(num)
    else:
      return n[0:j]+str(num)
  else:
    return n+"1"

