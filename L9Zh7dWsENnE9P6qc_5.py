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
  f=bin(people)
  return b(f[3:]+f[2])
def b(n):
  s=0
  for i in range(0,len(n)):
    s+=int(n[i])*(2**(len(n)-i-1))
  return s

