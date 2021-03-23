"""


Given `n` people find the survivor, starting from the first person he kills
the person to the left and the next surviving person kills the person to his
left, this keeps happening until 1 person survives return that person's
number.

### Examples

    josephus(1) ➞ 1
    
    josephus(8) ➞ 1
    
    josephus(41) ➞ 19

### Notes

Check the rescources if you are confused about the instructions.

"""

def josephus(people):
  p_2 = [2 ** i for i in range(7)]
  for i in p_2:
    if people < i:
      power = i
      ind = p_2.index(i) - 1
      break
  diff = people - p_2[ind]
  return 1 + diff * 2

