"""


Create a function that takes a list of more than three numbers and returns the
**Least Common Multiple** (LCM).

### Examples

    lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 2520
    
    lcm_of_list([13, 6, 17, 18, 19, 20, 37]) ➞ 27965340
    
    lcm_of_list([44, 64, 12, 17, 65]) ➞ 2333760

### Notes

The LCM of a list of numbers is the smallest positive number that is divisible
by each of the numbers in the list.

"""

def lcm_of_list(numbers):
  x=max(numbers)
  e=""
  x=max(numbers)
  r=[]
  b=[]
  for n in numbers:
    if n%2==0:
      b.append(n)
    else:
      r.append(n)
  t=max(r)
  z=max(b)
  a=list(numbers)
  for n in numbers:
    if n==1:
      a.remove(1)
    elif n==t or n==z:
      continue
    elif t%n==0:
      a.remove(n)
    elif z%n==0:
      a.remove(n)
  switch=True
  while(True):
    for i in a:
      if x%i!=0:
        switch=False
        break
      elif x%i==0:
        continue
    if switch==True:
      return x
    else:
      x+=max(numbers)
      switch=True

