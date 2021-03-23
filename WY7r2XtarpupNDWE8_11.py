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
  quit()

