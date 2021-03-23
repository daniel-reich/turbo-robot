"""


Performing division on a fraction often results in an infinitely repeating
decimal.

    1/3=.3333333...  1/7=.142857142857...

Create a function that takes a decimal in string form with the repeating part
in parentheses and returns the equivalent fraction in string form and in
lowest terms.

### Examples

    fractions("0.(6)") ➞ "2/3"
    
    fractions("1.(1)") ➞ "10/9"
    
    fractions("3.(142857)") ➞ "22/7"
    
    fractions("0.19(2367)") ➞ "5343/27775"
    
    fractions("0.1097(3)") ➞ "823/7500"

### Notes

N/A

"""

def ndivision(n,d):
  for i in range(2,n+1):
    if n%i==0 and d%i==0:
      return ndivision(n//i,d//i)
  else:
    return (n,d)
def fractions(s):
  n1,n2,n3=0,-1,0
  if '.' in s:
    s1=s.split('.')
#    print(s1)
    if '(' in s1[1] and ')' in s1[1]:
      idx1=s1[1].index('(')
      idx2=s1[1].index(')')
      if idx1<idx2 and s1[1][idx1+1:idx2].isdigit() and (idx1==0 or s1[1][0:idx1].isdigit()):
        n1=int(s1[0])
        n2=int(s1[1][0:idx1]) if idx1>0 else -1
        n3=int(s1[1][idx1+1:idx2])
        l2=idx1
        l3=idx2-idx1-1
    elif s1[0].isdigit() and s1[1].isdigit():
      n1=int(s1[0])
      n2=int(s1[1])
      l2=len(s1[1])
      l3=0
    else:
      return 'Error'
  elif s.isdigit():
    n1=int(s)
    return n1
  else:
    return 'Error'
  print(n1,n2,n3)
  num=n1*(10**l2)*(10**l3-1)+(n2*(10**l3-1) if n2!=-1 else 0)+n3
  denum=10**l2*(10**l3-1)
  ndiv=num//denum
  fdiv=num%denum
#  print(num,denum,ndiv,fdiv)
  minn,mind=ndivision(fdiv,denum)
  return (str(mind*ndiv+minn)+'/'+str(mind))

