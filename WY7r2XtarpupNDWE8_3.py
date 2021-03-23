"""


Create a function (given the number of discs and the move number) that returns
as a tuple the towers with their correct disks in order.

### What is Tower of Hanoi?

Tower of Hanoi is a problem in occursion, where you have to move a certain
amount of discs from one peg (or tower) to the final peg. The discs are
stacked on pegs with each disc being smaller than the last, as to create a
pyramid like shape.

![Alternative Text](https://edabit-challenges.s3.amazonaws.com/tower.png)

To illustrate, lets take `tower_of_hanoi(4, 3)`. The first move you would make
would be to move the 1 disc from the 1st tower to the 3rd tower. So move one
would result in:

    ([4, 3, 2], [], [1])

Then you would move the 2 disk from the 1st tower to the 2nd peg. Resulting
in:

    ([4, 3], [2], [1])

Then the final move would be to move the 1 disk onto the 2nd peg:

    ([4, 3], [2, 1], [])

Then that would be your answer!

### Examples

    tower_of_hanoi(1, 1) ➞ ([], [], [1])
    
    tower_of_hanoi(4, 3) ➞ ([4, 3], [], [2, 1])
    
    tower_of_hanoi(7, 12) ➞ ([7, 6, 5, 2, 1], [4, 3], [])

### Notes

The universal solution for the Tower of Hanoi differs if the number of discs
is even or odd (check the **Resources** tab for help).

"""

def tower_of_hanoi(disks, move):
  t1 = []
  t2 = [disks + 1]
  t3 = [disks + 1]
  b = 1
  for a in range(1, disks + 1):
    t1.insert(0,a)
  for a in range(move):
    if disks % 2 == 1:  
      if b == 1:
        t3.append(t1.pop()) if t1[-1] < t3[-1] else t1.append(t3.pop())
        b = 2
      elif b == 2:
        t2.append(t1.pop()) if t1[-1] < t2[-1] else t1.append(t2.pop())
        b = 3
      elif b == 3:
        t2.append(t3.pop()) if t3[-1] < t2[-1] else t3.append(t2.pop())
        b = 1
    else:
      if b == 1:
        t2.append(t1.pop()) if t1[-1] < t2[-1] else t1.append(t2.pop())
        b = 2
      elif b == 2:
        t3.append(t1.pop()) if t1[-1] < t3[-1] else t1.append(t3.pop())
        b = 3
      elif b == 3:
        t2.append(t3.pop()) if t3[-1] < t2[-1] else t3.append(t2.pop())
        b = 1
  t2.pop(0)
  t3.pop(0)
  return (t1,t2,t3)

