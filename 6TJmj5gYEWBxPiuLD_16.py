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
    save_1 = 0
    save_2 = 0
    save_1i = []
    save_2i = []
    count_1 = 0
    count_2 = 0
    com_12 = 0
    dek_num = lst[0]
    dek_col1 = [x for x in range(dek_num) if x % 2 != 0]
    dek_col2 = [x+2 for x in range(dek_num) if x % 2 == 0]
    totl_num = (lst[0]/2) * 3 - 2
    for i in lst[1:]:
           dek_col1 = ['#' if val == i else val for val in dek_col1]
           dek_col2 = ['#' if val == i else val for val in dek_col2]
​
    for i in range(len(dek_col1)-1):
        if dek_col1[i] == dek_col1[i+1]:
            save_1 += 1
            save_1i.append(i)
​
    for i in range(len(dek_col2)-1):
        if dek_col2[i] == dek_col2[i+1]:
            save_2 += 1
            save_2i.append(i)
​
    for i in range(len(dek_col1)-1):
        if dek_col1[i] == dek_col2 [i]:
            com_12 +=1
​
​
    for i, j in enumerate(dek_col1):
        if j == '#' and i != 0 and i != len(dek_col1)-1:
            count_1 += 3
        elif j == '#':
            count_1 += 2
​
    for i, j in enumerate(dek_col2):
        if j == '#' and i != 0  and i != len(dek_col2)-1:
            count_2 += 3
        elif j == '#':
            count_2 += 2
​
    return totl_num + save_1 + save_2 + com_12 - count_1 - count_2

