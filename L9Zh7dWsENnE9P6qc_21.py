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
  t=[]
  for i in range(1,people+1):
    t.append(i)
  while len(t)>1:
    if len(t)%2==0:
      for i in range(1,len(t),2):
        t[i]=0
      t=sorted(list(set(t)))
      t.remove(t[0])
    else:
      t.remove(t[0])
      for i in range(0,len(t),2):
        t[i]=0
      t=sorted(list(set(t)))
      t.remove(t[0])
  return t[0]

