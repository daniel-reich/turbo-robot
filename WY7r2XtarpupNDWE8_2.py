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
    arr = [list(range(disks, 0, -1)), [], []]
    direction = -1 if disks%2 else 1
    a, i = 0, 0
​
    while True:
        new_pos = (a + direction)%3
        arr[new_pos].append(arr[a].pop())
        a = new_pos
        i += 1
        if i == move:
            return tuple(arr)
        b, c = (a + direction)%3, (a + (direction*2))%3
        if not arr[b] and not arr[c]:
            return tuple(arr)
        if not arr[b]:
            arr[b].append(arr[c].pop())
        elif not arr[c]:
            arr[c].append(arr[b].pop())
        elif arr[b][-1] < arr[c][-1]:
            arr[c].append(arr[b].pop())
        else:
            arr[b].append(arr[c].pop())
        i += 1
        if i == move:
            return tuple(arr)

