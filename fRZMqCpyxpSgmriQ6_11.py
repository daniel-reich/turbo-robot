"""
Create a function that takes a string consisting of **lowercase letters** ,
**uppercase letters** and **numbers** and returns the string sorted in the
same way as the examples below.

### Examples

    sorting("eA2a1E") ➞ "aAeE12"
    // Don't repeat letters.
    
    sorting("Re4r") ➞ "erR4"
    
    sorting("6jnM31Q") ➞ "jMnQ136"
    
    sorting("846ZIbo") ➞ "bIoZ468"

### Notes

Don't repeat letters (numbers can be repeated).

"""

def sorting(s):
  l,s,res=[],list(s),''
  alpha,num=[i for i in s if i.isalpha()==True],[i for i in s if i.isdigit()==True]
  for i,j in zip(range(97,123),range(65,91)):
    l.append(chr(i))
    l.append(chr(j))
  k1=[l.index(i) for i in alpha]
  k1.sort()
  for i in k1: res=res+l[i]
  num.sort()
  res=res+''.join(num)
  return res

