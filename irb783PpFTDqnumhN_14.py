"""


Create a function that returns the string "Burp" with the amount of "r's"
determined by the input parameters of the function.

### Examples

    long_burp(3) ➞ "Burrrp"
    
    long_burp(5) ➞ "Burrrrrp"
    
    long_burp(9) ➞ "Burrrrrrrrrp"

### Notes

  * Expect `num` to always be >= 1.
  * Remember to use a capital "B".
  * Don't forget to `return` the result.

"""

def long_burp(num):
    if num >= 1:
        return "Bu" + 'r'*num + "p"

