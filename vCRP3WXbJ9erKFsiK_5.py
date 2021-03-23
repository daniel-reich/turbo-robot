"""


It's time to send and receive secret messages.

Create a single function that takes a string **or** a list and returns a coded
or decoded message.

The first letter of the string, or the first element of the list represents
the Character Code of that letter. The next elements are the differences
between the characters: e.g. `A` +3 --> `C` or `z` -1 --> `y`.

### Examples

    dif_ciph("Hello") ➞ [72, 29, 7, 0, 3]
    # H = 72, the difference between the H and e is 29 (upper- and lowercase).
    # The difference between the two l's is obviously 0.
    
    dif_ciph([ 72, 33, -73, 84, -12, -3, 13, -13, -68 ]) ➞ "Hi there!"
    
    dif_ciph("Sunshine") ➞ [83, 34, -7, 5, -11, 1, 5, -9]

### Notes

The input of the function will always be a string **or** a list with numbers.

"""

def dif_ciph1(inpt):
    x,res,y,=[],'',[]
    for i in inpt:            
        if i==' ':
            x.append(ord(i))
        else:
            x.append(ord(i))
    a=x[0]
    x=x[::-1]
    for i in range(len(x)-1):
        y.append(x[i]-x[i+1])
    y=y+[a]  
    return y[::-1]   
def dif_ciph2(inpt):
    z,res=[],''
    a=inpt[0]+inpt[1]
    z.append(inpt[0])
    z.append(a)
    for i in range(2,len(inpt)):
        if type(inpt[i])==int:
            b=inpt[i]+a
            z.append(b)
            a=b        
    for i in z:
        res+=chr(i)
    return res    
def dif_ciph(inpt):
    for i in inpt:
        if type(i)==str:
            return dif_ciph1(inpt)
        else:
            return dif_ciph2(inpt)

