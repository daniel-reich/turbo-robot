"""


Create a function that creates a pattern as a 2D list for a given number.

### Examples

     >
     >>
     >>>
     >>
     >
    
    arrow(3) ➞ [">", ">>", ">>>", ">>", ">"]
     >
     >>
     >>>
     >>>>
     >>>>
     >>>
     >>
     >
    
    arrow(4) ➞ [">", ">>", ">>>", ">>>>", ">>>>", ">>>", ">>", ">"]

### Notes

  * Function argument will always be a number greater than 0.
  * Odd numbers will have a single "peak" (see example #1).
  * Even numbers have two "peaks" (see example #2).

"""

def arrow(num):
    w=">"
    output = [">"]
    input=[">"*num]
    if num%2==0:
        for i in range(2,num+1):
            output+=[i*w]
        for i in range(num-1,0,-1):
            input+=[i*w]
    else:
        for i in range(2, num):
            output += [i * w]
        for i in range(num - 1, 0, -1):
            input += [i * w]
​
    return output+input

