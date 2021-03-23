"""


An **almost-sorted sequence** is a sequence that is **strictly increasing** or
**strictly decreasing** if you remove a **single element** from the list (no
more, no less). Write a function that returns `True` if a list is **almost-
sorted** , and `False` otherwise.

For example, if you remove `80` from the first example, it is perfectly sorted
in ascending order. Similarly, if you remove `7` from the second example, it
is perfectly sorted in descending order.

### Examples

    almost_sorted([1, 3, 5, 9, 11, 80, 15, 33, 37, 41] ) ➞ True
    
    almost_sorted([6, 5, 4, 7, 3]) ➞ True
    
    almost_sorted([6, 4, 2, 0]) ➞ False
    // Sequence is already sorted.
    
    almost_sorted([7, 8, 9, 3, 10, 11, 12, 2]) ➞ False
    // Requires removal of more than 1 item.

### Notes

  * Completely sorted lists should return `False`.
  * Lists will always be **> 3** in length (to remove ambiguity).
  * Numbers in each input list will be unique - don't worry about "ties".

"""

def almost_sorted(num_list):
    out_cast = []
    desc = []
    asc = []
    order = 0
    
    for number in range(0,len(num_list)):
        if number == 0:
            continue
        if number > 0:
            if num_list[number] - num_list[number-1] > 0:
                asc.append(number)
            if num_list[number] - num_list[number-1] < 0:
                desc.append(number)
    if len(desc) > len(asc):
        order = "descending"
    else:
        order = "ascending"
            
​
    if order == "ascending":     
        for index in range(0,len(num_list)):
            if index == 0:
                continue
            if index > 0:
                if num_list[index] > num_list[index-1]:
                    continue
                if num_list[index] < num_list[index-1]:
                    out_cast.append(num_list[index-1])
    
    if order == "descending": 
        for index in range(0,len(num_list)):
            if index == 0:
                continue
            if index > 0:
                if num_list[index] < num_list[index-1]:
                    continue
                if num_list[index] > num_list[index-1]:
                    out_cast.append(num_list[index])
    print(out_cast)
    if len(out_cast) == 1:
        return True
    else:
        return False

