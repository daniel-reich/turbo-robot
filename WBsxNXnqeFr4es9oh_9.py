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

def fill_perimeter(lst,txt,width,offset):
    if width == 1:
        lst.extend([(offset,offset,txt[0])])
        return lst
    result = []
    for indx,t in enumerate(txt[0:4*width  - 4]):
        if indx%4 == 0 :
            lst.extend([(0 + offset,indx//4 + offset,t)])
        if indx%4 == 1 :
            lst.extend([((indx-1)//4  + offset, width - 1 + offset ,t)])
        if indx%4 == 2 :
            lst.extend([(width - 1 + offset ,width - 1 - (indx-2)//4  + offset, t)])
        if indx%4 == 3 :
            lst.extend([(width - 1 - (indx-3)//4 +      offset ,0 + offset   , t)])
    if width > 2:
        lst=fill_perimeter(lst,txt[4*width  - 4::],width - 2,offset + 1) 
    return lst
​
def clockwise_cipher(message):
    y = len(message)**(.5)
    if y.is_integer():
        width = int(y)
    else: 
       width = int(y + 1)  
       message = message + (int(y + 1)**2 - len(message))*" "
    lst = fill_perimeter([],message,width  ,0)
    return ''.join([t for x,y,t in sorted(lst)])

