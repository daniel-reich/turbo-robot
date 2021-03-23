"""


Given a list of seats, return the maximum number of new people which can be
seated, as long as there is at least a gap of **2 seats** between people.

  * Empty seats are given as `0`.
  * Occupied seats are given as `1`.
  * Don't move any seats which are already occupied, even if they are less than 2 seats apart. Consider only the gaps between new seats and existing seats.

### Examples

    maximum_seating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0]) ➞ 2
    # [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
    
    maximum_seating([0, 0, 0, 0]) ➞ 2
    # [1, 0, 0, 1]
    
    maximum_seating([1, 0, 0, 0, 0, 1]) ➞ 0
    # There is no way to have a gap of at least 2 chairs when adding someone else.

### Notes

  * Notice how there may be several possibilities for assigning seats to people, but these cases won't affect the results.
  * All seats will be valid.

"""

def maximum_seating(lst):
    current_position = 0
    added_seats = 0
    for i in range(current_position, len(lst)):
    
        if lst[i] == 0:
            if i == 0 and i + 2 >= len(lst):
                return 1
            if i == 0 or i == 1:
                if i == 1 and lst[i-1] != 1 and lst[i + 1] != 1 and lst[i + 2] != 1:
                    lst[i] = 1
                    added_seats += 1
                elif i == 0 and lst[i + 1] != 1 and lst[i + 2] != 1:
                    lst[i] = 1
                    added_seats += 1
            elif i == len(lst) - 1 or i == len(lst) - 2:
                if i == len(lst) - 2 and lst[i + 1] != 1 and lst[i - 1] == 0 and lst[i - 2] == 0 :
                    lst[i] = 1
                    added_seats += 1
                elif i == len(lst) - 1 and lst[i - 1] == 0 and lst[i - 2] == 0:
                    lst[i] = 1
                    added_seats += 1
            elif lst[i + 1] == 0 and lst[i + 2] == 0 and lst[i - 1] == 0 and lst[i - 2] == 0:
                lst[i] = 1
                added_seats += 1
​
​
    return added_seats

