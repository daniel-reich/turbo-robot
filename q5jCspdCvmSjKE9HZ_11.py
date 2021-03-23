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

def get_gcd(a,b): 
  [sml,lar] = sorted([a,b])
  startoff = sml
  while startoff > 0: 
    if lar % startoff == 0 and sml % startoff == 0:
      print(str(lar) + ' divided by ' + str(startoff) + ' = ' + str(lar/startoff))
      
      print(startoff)
      return startoff
    startoff -= 1
  return 1
    
​
def lcm_of_list(numbers):
  lcm = numbers[0]
  for i in range(1,len(numbers)):
    print(lcm)
    print(numbers[i])
    lcm = lcm * numbers[i]//get_gcd(lcm,numbers[i])
    print(lcm)
    print('-----')
  return lcm

