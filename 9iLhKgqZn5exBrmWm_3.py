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

def ascending(txt):
  for i in range(1,len(txt)//2+1):
    k,B,C=0,[],[]
    for j in range(len(txt)):
      if len(txt[k:k+i])==i and len(txt[k+i:k+2*i])==i:
        C.append([txt[k:k+i],txt[k+i:k+2*i]])
        B.append(int(txt[k:k+i])+1==int(txt[k+i:k+2*i]))
        k=k+i
    if all(B) and C[-1][-1][-1]==txt[-1]:
      return True
      break
  else:
    return False

