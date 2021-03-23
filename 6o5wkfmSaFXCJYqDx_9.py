"""


Create a function, that will for a given `a, b, c`, do the following:

  * Add `a` to itself `b` times.
  * Check if the result is divisible by `c`.

### Examples

    abcmath(42, 5, 10) ➞ False
    # 42+42 = 84,84+84 = 168,168+168 = 336,336+336 = 672, 672+672 = 1344
    # 1344 is not divisible by 10
    
    abcmath(5, 2, 1) ➞ True
    
    abcmath(1, 2, 3) ➞ False

### Notes

  * "if the result is divisible by `c`", means that if you divide the result and `c`, you will get an integer (5, and not 4.5314).
  *  **The second test is correct.**

"""

def abcmath(a, b, c):
    s=b
    f=a
    while s>0:
        l=f+f
        f=l
        s=s-1
    if l%c==0:
        return True
    else:
        return False

