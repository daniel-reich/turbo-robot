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

def combinations(classroom):
    comb_list = []
    for desk_id in range(0, len(classroom)):
        #print ("Checking desk number: {}".format(desk_id))
        if classroom[desk_id] != "#": #if already occupied we skip
            #print ("Checking desk number: {}".format(desk_id))
            if desk_id == 0: #check to the right and below only
                #print ("Checking desk number 1")
                if classroom[desk_id+1] == "0": #check to the right
                    comb_list.append([desk_id+1, desk_id+2])
                if classroom[desk_id+2] == "0": #check below
                    comb_list.append([desk_id+1, desk_id+3])
            elif desk_id == 1: #check to the left and below only
                if classroom[desk_id-1] == "0": #check to the left
                    if [desk_id, desk_id+1] not in comb_list:
                        comb_list.append([desk_id+1, desk_id])
                if classroom[desk_id+2] == "0": #check below
                    comb_list.append([desk_id+1, desk_id+2])
            elif desk_id == len(classroom)-2: #check to the right and above only
                if classroom[desk_id+1] == "0": #check to the right
                    comb_list.append([desk_id+1, desk_id+2])
                if classroom[desk_id-2] == "0": #check above
                    if [desk_id-1, desk_id+1] not in comb_list:
                        comb_list.append([desk_id+1, desk_id-1])
            elif desk_id == len(classroom)-1: #check to the left and above only
                if classroom[desk_id-1] == "0": #check to the left
                    if [desk_id, desk_id+1] not in comb_list:
                        comb_list.append([desk_id+1, desk_id])
                if classroom[desk_id-2] == "0": #check above
                    if [desk_id-1, desk_id+1] not in comb_list:
                        comb_list.append([desk_id+1, desk_id-1])
            #for everything else check above, below and left (for even) and right (for odd)
            else:
                if classroom[desk_id-2] == "0": #check above
                    if [desk_id-1, desk_id+1] not in comb_list:
                        comb_list.append([desk_id+1, desk_id-1])
                if classroom[desk_id+2] == "0": #check below
                    if [desk_id+3, desk_id+1] not in comb_list:
                        comb_list.append([desk_id+1, desk_id+3])
                if (desk_id+1)%2 == 0: #check to the left
                    if classroom[desk_id-1] == "0":
                        if [desk_id, desk_id+1] not in comb_list:
                          comb_list.append([desk_id+1, desk_id])
                else: #check to the right
                    if classroom[desk_id+1] == "0":
                        comb_list.append([desk_id+1, desk_id+2])
​
    return (comb_list)
        
            
​
def seating_students(lst):
    desks = int(lst[0])
    classroom = []
    for x in range(0, desks):
        if (x+1) in lst[1:]:
            classroom.insert(x, "#")
        else:
            classroom.insert(x, "0")
    return len(combinations(classroom))

