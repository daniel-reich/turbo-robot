"""


Create a function that takes in the size of the line and the number of people
waiting and places people in an _S-shape_ ordering. The demonstration below
will make it clear:

    # Ordering numbers 1-15 in a [5,3] space.
    
    order_people([5, 3], 15) ➞ [
      [1, 2, 3],
      [6, 5, 4],
      [7, 8, 9],
      [12, 11, 10],
      [13, 14, 15]
    ]

If there is extra room, leave those spots blank with a `0` filler.

    # Ordering numbers 1-5 in a [4, 3] space.
    
    order_people([4, 3], 5) ➞ [
      [1, 2, 3],
      [0, 5, 4],
      [0, 0, 0],
      [0, 0, 0]
    ]

If there are too many people for the given dimensions, return `"overcrowded"`.

    order_people([4, 3], 20) ➞ "overcrowded"

### Examples

    order_people([3, 3], 8) ➞ [
      [1, 2, 3],
      [6, 5, 4],
      [7, 8, 0]
    ]
    
    order_people([2, 4], 5) ➞ [
      [1, 2, 3, 4],
      [0, 0, 0, 5]
    ]
    
    order_people([2, 4], 10) ➞ "overcrowded"

### Notes

  * Always start the ordering on the upper-left corner.
  * If the **S-shape** concept doesn't make sense, try writing down some of these examples on a piece of paper and tracing a pencil through the numbers in order.

"""

def order_people(lst, people):
  # return people
  lst2, lst3, j = [], [], 0
  if(lst[0]*lst[1] < people):
    return "overcrowded"
  else:
    for i in range(1,(lst[0]*lst[1])+1):
      if(i%lst[1]==0):
        lst2.append(0) if i>people else lst2.append(i)
        if(j==0):
          j = 1
          lst3.append(lst2)
        else:
          j = 0
          lst2.reverse()
          lst3.append(lst2)
        lst2 = []
      else:
        lst2.append(0) if i>people else lst2.append(i)
​
    return lst3

