"""


Create a function to reproduce the **wrap around** effect shown:

### Examples

    wrap_around("Hello, World!", 2) ➞ "llo, World!He"
    
    wrap_around("From what I gathered", -4) ➞ "eredFrom what I gath"
    
    wrap_around("Excelsior", 30) ➞ "elsiorExc"
    
    wrap_around("Nonscience", -116) ➞ "cienceNons"

### Notes

  * The `offset` can be negative.
  * The `offset` can be greater than `string`.

"""

def wrap_around(strr, numm):
    global k
    g = len(strr)
    k = strr
    while abs(numm) > g:
        k = k + strr
        g = len(k)
    if numm == 0:
        return(strr)
    if numm > len(strr):
        return(k[int(numm):len(k)]+strr[0:abs(len(k)-int(numm)-len(strr))])
    if numm < len(strr) and numm > 0:
        return(strr[numm:len(strr)]+strr[0:numm])
    if abs(numm) < len(strr) and numm < 0:
        return(strr[len(strr)-abs(numm):len(strr)]+strr[0:len(strr)-abs(numm)])
    if abs(numm) > len(strr) and numm < 0:
        return(strr[len(k)-abs(numm):len(strr)]+strr[0:len(k)-abs(numm)])

