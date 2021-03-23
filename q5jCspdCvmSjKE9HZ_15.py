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
  for i in range(len(numbers)-1):
    numbers[i+1]=int(lcm(numbers[i],numbers[i+1]))
  return numbers[len(numbers)-1]
def lcm(i,j):
  return i*j/gcd(i,j)
def gcd(i,j):
  m=1
  for k in range(1,i):
    if((i%k==0) & (j%k==0)):
      m=k
  return int(m)

