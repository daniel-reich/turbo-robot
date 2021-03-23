"""


You work in a toy car workshop, and your job is to build toy cars from a
collection of parts. Each toy car needs 4 wheels, 1 car body, and 2 figures of
people to be placed inside. Given the total number of wheels, car bodies and
figures available, how many _complete_ toy cars can you make?

### Examples

    cars(2, 48, 76) ➞ 0
    # 2 wheels, 48 car bodies, 76 figures
    
    cars(43, 15, 87) ➞ 10
    
    cars(88, 37, 17) ➞ 8

### Notes

N/A

"""

def cars(wheels, bodies, figures):
  ##need 4 wheels, 1 body, 2 figures
  cars = 0
  while wheels >=4 and bodies >= 1 and figures >=2:
    cars += 1
    wheels -= 4
    bodies -= 1
    figures -= 2
  
  return cars

