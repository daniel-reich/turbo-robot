"""


A prison can be represented as a list of cells. Each cell contains exactly one
prisoner. A `1` represents an unlocked cell and a `0` represents a locked
cell.

    [1, 1, 0, 0, 0, 1, 0]

Starting inside the leftmost cell, you are tasked with seeing how many
prisoners you can set free, with a catch. You are the prisoner in the first
cell. If the first cell is locked, you cannot free anyone. Each time you free
a prisoner, the locked cells become unlocked, and the unlocked cells become
locked again.

So, if we use the example above:

    [1, 1, 0, 0, 0, 1, 0]
    # You free the prisoner in the 1st cell.
    
    [0, 0, 1, 1, 1, 0, 1] 
    # You free the prisoner in the 3rd cell (2nd one locked).
    
    [1, 1, 0, 0, 0, 1, 0]
    # You free the prisoner in the 6th cell (3rd, 4th and 5th locked).
    
    [0, 0, 1, 1, 1, 0, 1]
    # You free the prisoner in the 7th cell - and you are done!

Here, we have set free `4` prisoners in total.

Create a function that, given this unique prison arrangement, returns the
number of freed prisoners.

### Examples

    freed_prisoners([1, 1, 0, 0, 0, 1, 0]) ➞ 4
    
    freed_prisoners([1, 1, 1]) ➞ 1
    
    freed_prisoners([0, 0, 0]) ➞ 0
    
    freed_prisoners([0, 1, 1, 1]) ➞ 0

### Notes

  *  **You are the prisoner in the first cell. You must be freed to free anyone else.**
  * You must free a prisoner in order for the locks to switch. So in the second example where the input is `[1, 1, 1]` after you release the first prisoner, the locks change to `[0, 0, 0]`. Since all cells are locked, you can release no more prisoners.
  * You always start within the leftmost element in the list (the first prison cell). If all the prison cells to your right are zeroes, you cannot free any more prisoners.

"""

def freed_prisoners(prison):
  counter = 0
  if(prison[0] == 0):
    return 0
  for cell in prison:
    if(cell == 1):
      counter += 1
      for num in range(0, len(prison)):
        if(prison[num] == 0):
          prison[num] = 1
        elif(prison[num] == 1):
          prison[num] = 0
  return counter

