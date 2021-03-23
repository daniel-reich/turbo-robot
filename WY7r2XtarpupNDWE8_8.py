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

def tower_of_hanoi_even(disks, move):
    pegs = [list(range(1, disks + 1))[::-1], [], []]
    m = 0
    while m < move:
        m += 1
        if m % 3 == 1:
            # make legal move between A and B
            p1, p2 = 0, 1
        elif m % 3 == 2:
            # make legal move between A and C
            p1, p2 = 0, 2
        else:
            # make legal move between B and C
            p1, p2 = 1, 2
        if len(pegs[p2]) == 0:
            pegs[p2].append(pegs[p1].pop())
        elif len(pegs[p1]) == 0:
            pegs[p1].append(pegs[p2].pop())
        else:
            if pegs[p1][-1] < pegs[p2][-1]:
                pegs[p2].append(pegs[p1].pop())
            else:
                pegs[p1].append(pegs[p2].pop())
    return tuple(pegs)
​
def tower_of_hanoi_odd(disks, move):
    pegs = [list(range(1, disks + 1))[::-1], [], []]
    m = 0
    while m < move:
        m += 1
        if m % 3 == 1:
            # make legal move between A and C
            p1, p2 = 0, 2
        elif m % 3 == 2:
            # make legal move between A and B
            p1, p2 = 0, 1
        else:
            # make legal move between B and C
            p1, p2 = 1, 2
        if len(pegs[p2]) == 0:
            pegs[p2].append(pegs[p1].pop())
        elif len(pegs[p1]) == 0:
            pegs[p1].append(pegs[p2].pop())
        else:
            if pegs[p1][-1] < pegs[p2][-1]:
                pegs[p2].append(pegs[p1].pop())
            else:
                pegs[p1].append(pegs[p2].pop())
    return tuple(pegs)
​
def tower_of_hanoi(disks, move):
    if disks == 1:
        return ([],[],[1])
    return tower_of_hanoi_even(disks, move) if disks % 2 == 0 else tower_of_hanoi_odd(disks, move)

