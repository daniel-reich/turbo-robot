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

def square_list(n):
  
  if n==1:
    return [[1]]
  
  elif n==2:
    return [[1,2],[4,3]]
  
  else:
    ans = []
    for i in range(n):
      element = []
      for j in range(n):
        element.append(None)
      ans.append(element)
    
    k = 1
    for i in range(n-1):
      ans[0][i] = k
      k += 4
    
    k = 2
    for i in range(n-1):
      ans[i][n-1] = k
      k += 4
      
    k = 3
    for i in range(-1,-n,-1):
      ans[n-1][i] = k
      k += 4
      
    k = 4
    for i in range(-1,-n,-1):
      ans[i][0] = k
      k += 4
      
    array = square_list(n-2)
    for i in range(n-2):
      for j in range(n-2):
        ans[i+1][j+1] = array[i][j] + 4*n - 4
    return ans
        
def clockwise_cipher(message):
  n = 0
  L = len(message)
  while True:
    if n**2 >= L:
      break
    n += 1
  new_message = message
  while len(new_message)<n**2:
    new_message += " "
  ans = ""
  array = square_list(n)
  for i in range(n):
    for j in range(n):
      ans += new_message[array[i][j]-1]
  return ans

