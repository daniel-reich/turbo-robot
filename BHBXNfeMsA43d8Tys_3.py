"""


As far as we currently know, approximations for the mathematical constant
**pi** (π) in the history of mathematics started surfacing with Ancient
Babylonians, who found its correct truncation up to 1 decimal place. During
the 5th century, the Chinese mathematician Zu Chongzhi raised it to 7 decimal
places and from the 18th century onwards the number of correct pi decimal
places has seen steady growth.

Since the middle of the 20th century, the approximation of pi has been the
task of electronic digital computers. During the 2019 Pi Day on the 14th of
March, the Japanese computer scientist _Emma Haruka Iwao_ released the
currently most accurate value of pi with more than 31.4 trillion digits, using
170 Terabytes of data.

Your task is to create a function that takes a positive integer `n` as an
argument and returns the value of **pi** with its first `n` decimal digits.

Taylor series are usually used to get finer approximations. To make this
challenge approachable to anyone, the following formula is suggested:

![](https://edabit-
challenges.s3.amazonaws.com/c021371bba1389081786f93100ecc8b4.svg)

### Examples

    pi(1) ➞ "3.1"
    
    pi(2) ➞ "3.14"
    
    pi(30) ➞ "3.141592653589793238462643383279"

### Notes

N/A

"""

def pi(n):
  w=n+10
  b=10**w
  x1=b*4//5
  x2=b//-239
  he=x1+x2
  n*=2
  for i in range(3,n,2):
    x1//=-25
    x2//=-57121
    x=(x1+x2)//i
    he+=x
  pai=he*4
  pai//=10**10
  paistring=str(pai)
  result=paistring[0]+str('.')+paistring[1:len(paistring)]
  return  result

