"""


Given the formula for a straight line `y = ax + b` and the x, y coordinates of
a point, find the distance between that point and the line. Round the result
to two decimal points.

### Examples

    dist("y=(-3/4)x-5/4", 5, 2) ➞ 5.6
    
    dist("y=(5+1/3)x-2.3", 1, 4) ➞ 0.18
    
    dist("y=2.2x-(3+1/5)", 3, -2) ➞ 2.23

### Notes

Check the **Resources**.

"""

import re
import math
def new_number(n):
  try:
    fraction = re.findall(r'\d+\/\d+',n)[0]
    numbers = re.findall(r'\d+',fraction[0])
    n = re.sub(r'{}'.format(fraction),str(round(int(numbers[0]) / int(numbers[1])),3),n)
  except IndexError:
    pass
  try:
    power = re.findall(r'\d+\*{2}\d+',n)[0]
    values = re.findall(r'\d+',power[0])
    n = re.sub(r'{}'.format(power),str(round(pow(int(values[0]),int(values[1])),3)),n)
  except IndexError:
    pass
  try:
    n = re.sub(r'[\(\)]',"",n)
  except IndexError:
    pass
  return eval(n)
def dist(line, x, y):
  a = new_number(re.findall(r'(?<=\=).+(?=x)',line)[0])
  c = new_number(line[line.find("x")+2::])
  if "x-" in line:
    c *= -1
  return round(abs(a*x - y + c) / math.sqrt(pow(a,2)+1),2)

