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

def lcm_of_list(a):
  t=len(a)
  i,b,c=0,1,0
  while i<t-1:
    if a[i]>a[i+1]:
      a[i],a[i+1]=a[i+1],a[i]
    for j in range(2,a[i]+1):
        if a[i]%j==0 and a[i+1]%j==0:
          b=j
    a[i+1]=int(a[i]*a[i+1]/b)
    b=1
    i+=1
  return a[len(a)-1]

