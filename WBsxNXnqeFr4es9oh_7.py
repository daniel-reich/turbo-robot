"""


In **Clockwise Cipher** , encoding is done by placing message characters in
the corner cells of a square and moving in a clockwise direction.

Create a function that takes an argument `message`, and returns the **encoded
message**.

There are some variations on the rules of encipherment. One version of the
cipher rules are outlined below:

    message = "Mubashir Hassan"
    
    clockwise_cipher(message) ➞ "Ms ussahr nHaaib"

 **Step 1:** Form a square large enough to fit all the message characters.
Given message can fit in a 4 x 4 square.

 **Step 2:** Starting with the top-left corner, place message characters in
the corner cells moving in a clockwise direction. After the first cycle is
complete, continue placing characters in the cells following the last one in
its respective row/column. When the outer cells are filled, continue for the
remaining inner squares:

M| s| | u  
---|---|---|---  
s| s| a| h  
r| | n| H  
a| a| i| b  
  
 **Step 3:** Return encoded message **Rows-wise** :

    eMessage = "Ms ussahr nHaaib"

### Example for a 5 x 5 Square

    [ 1  5  9 13  2]
    [16 17 21 18  6]
    [12 24 25 22 10]
    [ 8 20 23 19 14]
    [ 4 15 11  7  3]

### Examples

    clockwise_cipher("Mubashir Hassan") ➞ "Ms ussahr nHaaib"
    
    clockwise_cipher("Matt MacPherson") ➞ "M ParsoMc nhteat"
    
    clockwise_cipher("Edabit is amazing") ➞ "Eisadng  tm    i   zbia a"

### Notes

  * Fill up any unused cells with a space character.
  * Message can contain spaces and special characters.

"""

import math
​
​
# recursive function to find clockwise coordinates of any index given the square size
def clockwise_pos(i, size, depth = 0):
  if size == 1: return [depth, depth]   # base case (reached only with odd sizes)
​
  elif i >= size**2 - (size-2)**2:
    # keep moving to a smaller square until i will fall within its outer edge
    return clockwise_pos(i-(size**2 - (size-2)**2), size-2, depth+1)
​
  else:   
    # determine coordinates based on group, translate based on distance from corner
    if i % 4 == 0: coord = [0,0 + i//4]
    elif (i-1) % 4 == 0: coord = [0 + i//4, size-1]
    elif (i-2) % 4 == 0: coord = [size-1, size-1 - i//4]
    elif (i-3) % 4 == 0: coord = [size-1 - i//4, 0]
    
    # add depth to account for previous layers
    coord[0] += depth
    coord[1] += depth
    return coord
​
​
# main function to encrypt message using clockwise indexing
def clockwise_cipher(message):
  # determine minimum size that will contain message
  size = math.ceil(len(message)**0.5)
  
  # generate square
  square = []
  for y in range(size):
    square.append([])
    for x in range(size):
      square[y].append(" ")
  # fill square using clockwise coordinates
  for i in range(len(message)):
    coord = clockwise_pos(i, size)
    square[coord[0]][coord[1]] = message[i]
  
  # combine square to form encrypted message
  encrypted_message = ""
  for line in square:
    for char in line:
      encrypted_message += char
  return encrypted_message

