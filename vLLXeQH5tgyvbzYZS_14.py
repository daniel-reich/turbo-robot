"""


A Pythagorean triple is a set of three integer numbers that form a right
triangle. The sum of the squares of the two smaller numbers should equal the
square of the largest number. Given three numbers a, b and c (c being the
largest):

    a^2 + b^2 = c^2

Furthermore, a Pythagorean triple is said to be primitive if the three numbers
are pairwise coprime - that is, the greatest common prime factor between any
two numbers is 1.

Create a function that takes a list of three numbers (unordered) and returns
`True` if the numbers constitute a primitive Pythagorean triple, `False`
otherwise.

### Examples

    is_prim_pyth_triple([4, 5, 3]) ➞ True
    
    is_prim_pyth_triple([7, 12, 13]) ➞ False
    
    is_prim_pyth_triple([39, 15, 36]) ➞ False
    # Pythagorean triple, but not primitive.
    
    is_prim_pyth_triple([77, 36, 85]) ➞ True

### Notes

N/A

"""

def FPB (x):
  lis=[]
  for i in range (1,x+1):
    if x % i==0:
      x=x/i
      lis.append(i)
  return lis
def is_pitagoras(l):
  l.sort()
  if pow(l[0],2) + pow(l[1],2)==pow(l[2],2):
    return True
  else:
    return False
def is_prim_pyth_triple (l):
  l.sort()
  is_pita=is_pitagoras(l)
  if is_pita ==True:
    a=set(FPB(l[0]))
    b=set(FPB(l[1]))
    c=set(FPB(l[2]))
    if (a & b)=={1} and (b & c) =={1} and (a & c)=={1}:
      return True
    else:
      return False
  elif is_pita==False:
    return False

