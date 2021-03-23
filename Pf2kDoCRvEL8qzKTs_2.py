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
  
  people_order = lst[0] * lst[1]
​
  lst_s = []
​
  comp = []
​
  if people_order >= people:
​
      for i in range(1, people_order + 1):
          if i <= people:
            comp.append(i)
          elif i > people:
            comp.append(0)
          else:
            continue
​
      count = 0
​
      for g in range(0, len(comp), lst[1]):
          count += 1
          if count % 2 != 0:
              lst_s.append(comp[g:g + lst[1]])
          else:
              lst_s.append(comp[g:g + lst[1]][::-1])
​
      return lst_s
​
  else:
      return "overcrowded"

