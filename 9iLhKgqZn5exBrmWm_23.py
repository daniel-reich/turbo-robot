"""


Write a function that returns `True` if a string consists of **ascending or
ascending AND consecutive** numbers.

### Examples

    ascending("232425") ➞ True
    # Consecutive numbers 23, 24, 25
    
    ascending("2324256") ➞ False
    # No matter how this string is divided, the numbers are not consecutive.
    
    ascending("444445") ➞ True
    # Consecutive numbers 444 and 445.

### Notes

A **number** can consist of any number of digits, so long as the numbers are
adjacent to each other, and the string has at least two of them.

"""

def ascending(n):
  length=1
  while(length<=len(n)//2):
    check=0
    for i in range(0,len(n),length):
      if(i!=0 and int(n[i:i+length])!=int(n[i-length:i])+1):
        check=1       
        length+=1
        break
    if(check==0):
      return True
  return False

