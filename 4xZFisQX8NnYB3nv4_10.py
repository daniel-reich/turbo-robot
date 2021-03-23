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
  count = 0
  for i in range(len(lst)):
    if lst[i]==0:
      left = lst[max(0,i-2):i].count(1)
      right = lst[i+1:min(len(lst),i+3)].count(1)
      if left==0 and right==0:
        lst[i] = 1
        count+=1
  return count

