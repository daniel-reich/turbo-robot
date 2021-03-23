"""


Create a function that takes a list of numbers and returns the _greatest
common factor_ of those numbers.

### Examples

    gcd([84, 70, 42, 56]) ➞ 14
    
    gcd([19, 38, 76, 133]) ➞ 19
    
    gcd([120, 300, 95, 425, 625]) ➞ 5

### Notes

The GCD is the largest factor that divides all numbers in the list.

"""

def gcd_2(a,b):
  if a<b:
    a,b=b,a
  if a%b==0:
    return b
  else:
    return gcd_2(b,a%b)
def gcd(lst):
  g=lst[0]
  for i in range(1,len(lst)):
    g=gcd_2(g,lst[i])
  return g
def main():
  lst=list(map(int,input().split()))
  res=gcd(lst)
  print(res)
  return main()

