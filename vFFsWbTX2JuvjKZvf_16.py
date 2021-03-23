"""


 **Mubashir** created an infinite loop! Help him by fixing the code in the
code tab to pass this challenge. Look at the examples below to get an idea of
what the function should do.

### Examples

    print_list(1) ➞ [1]
    
    print_list(3) ➞ [1, 2, 3]
    
    print_list(6) ➞ [1, 2, 3, 4, 5, 6]

### Notes

  *  **READ EVERY WORD CAREFULLY, CHARACTER BY CHARACTER!**
  * Don't overthink this challenge; it's not supposed to be hard.

"""

def print_list(n):
    result=[]
    i=1
    while i<=n:
        result+=[i]
        i=i+1
    return result

