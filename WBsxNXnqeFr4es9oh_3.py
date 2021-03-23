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
  k=1
  while k**2<len(message):
    k+=1
  message=message+' '*(k**2-len(message))
  res=[[0 for _ in range(k)] for _ in range(k)]
  A=[]
  for i in range(k-1):
    for j in range(k-1):
      if all(x not in A for x in [(i,j), (j,k-i-1), (k-i-1,k-j-1), (k-j-1,i)]):
        A+=[(i,j), (j,k-i-1), (k-i-1,k-j-1), (k-j-1,i)]
  D=[]
  for x in A:
    if x not in D:
      D.append(x)
  c=0
  for x in D:
    res[x[0]][x[1]]=message[c]
    c+=1
  res2=[''.join(x) for x in res]
  return ''.join(res2)

