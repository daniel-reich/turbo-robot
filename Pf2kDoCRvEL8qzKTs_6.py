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

def order_people(size,queue):
    final = []
    count = size[0] * size[1]
    #people = [x in range(1,queue+1)]
    row_count = 0
    column_count = 0
    index = 1
    if queue > count:
        return "overcrowded"
    if count >= queue:
    
        for row in range(1,size[0]+1):
            #if index <= queue:
                x = []
                
                if row_count % 2 == 0:
                    for item in range(0,size[1]):
                        if index <= queue:
                            x.append(index)
                        else:
                            x.append(0)
                        index += 1
                    final.append(x)
                        #column_count = size[1]
                    x = []
                if row_count % 2 != 0:
                    sub_index = index + size[1] -1
                    for item in range(0,size[1]):
                        if sub_index <= queue:
                            x.append(sub_index)
                        else:
                            x.append(0)
                        sub_index -= 1
                    final.append(x)
                    index += size[1]
                    x = []
                        #column_count = 0
                row_count += 1
            
    
        return final

