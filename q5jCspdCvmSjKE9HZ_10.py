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

def lcm(a,b):
  if a<b:
    a,b=b,a
  for i in range(b,a*b+1):
    if i%a==0 and i%b==0:
      break
  return i
def lcm_of_list(numbers):
  m=lcm(numbers[0],numbers[1])
  for i in range(2,len(numbers)):
    m=lcm(m,numbers[i])
  return m

