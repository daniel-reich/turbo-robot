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

def seating_students(l):
    s = 0
    l_r = [True for i in range(l[0]//2)]
    l_l = [True for i in range(l[0]//2)]
    for i in l[1:]:
        if i%2 == 0 :
            l_r[i//2-1] = False
        else:
            l_l[i//2] = False
    for i in range(len(l_r)-1):
        if l_l[i] == l_l[i+1] == True:
            s += 1
        if l_r[i] == l_r[i+1] == True:
            s += 1
        if l_l[i] == l_r[i] == True:
            s += 1
    if l_r[-1] == l_l[-1] == True:
        s += 1
    return s

