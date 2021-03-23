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
    ans = ['>' * i for i in range(1,num+1)]
    if len(ans[-1]) % 2 == 0:
        ans.extend(ans[::-1])
    else:
        ans.extend(ans[:-1][::-1])
    return ans

