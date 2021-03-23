"""


Create a function that reads a list of integers stored which will be in the
following format: `[[K, r1, r2, r3, ...]]`, where **K** represents the number
of desks in a classroom, and the rest of the integers in the list will be in
sorted order and will represent the desks that are already occupied. All of
the desks will be arranged in two columns, where desk #1 is at the top left,
desk #2 at the top right, desk #3 is below #1, desk #4 is below #2, etc.

Your program should return the number of ways two students can be seated next
to each other. This means one student is on the left and one on the right, or
one student is directly above or below the other student.

To illustrate:

    [[12, 2, 6, 7, 11]]

This classroom will look like the following:

#### Column 1

    [[#, 4, #, 8, 10, 12]]
    # The first # is 2 and second # is 6 which are occupied.

#### Column 2

    [[1, 3, 5, #, 9, #]]
    # The first # is 7 and and second # is 11 which are occupied.

Based on the above arrangement of occupied desks, there are a total of six
ways to seat two new students next to each other. The combinations are:

    [[1, 3]], [[3, 4]], [[3, 5]], [[8, 10]], [[9, 10]], [[10, 12]]

For this input, your program should return `6`. **K** will range from `2` to
`24` and will always be an even number. After **K** , the number of occupied
desks in the list can range from `0` to **K**.

### Examples

    seating_students([6, 4]) ➞ 4
    
    seating_students([8, 1, 8]) ➞ 6
    
    seating_students([12, 2, 6, 7, 11])  ➞ 6

### Notes

N/A

"""

def seating_students(lst):
    
    updt_seat = [x if not x in lst[1:] else "#" for x in range(1, lst[0]+1)]
    count = 0
    for each in updt_seat:
        if each != "#":
            if each % 2 and each != updt_seat[-1]:
                if updt_seat[each] != "#":
                    count+=1
            if each < len(updt_seat) - 1 and updt_seat[each+1] != "#":
                count += 1
    return count

