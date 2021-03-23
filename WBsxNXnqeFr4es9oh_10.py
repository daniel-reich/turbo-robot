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

def clockwise_cipher(message):
  length = 0
  while length*length<len(message):
    length+=1
  clock = [[' ' for c in range(length)] for r in range(length)]
  ring = 0
  x,y = 0,0
  direct = 'urdl'
  side = 'u'
  for i in range(len(message)):
    clock[x][y] = message[i]
    if side=='l' and x-ring-1==0:
      ring+=1
      x = ring
      y = ring
    elif side=='u':
      x = y
      y = length-1-ring
    elif side=='r':
      y = length-x-1
      x = length-1-ring
    elif side=='d':
      x = y
      y = ring
    else:
      y = length-x
      x = ring
    side = direct[(direct.find(side)+1)%4]
  return ''.join(''.join(r) for r in clock)

