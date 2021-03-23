"""


Create strings that, when evaluated with `eval()`, equal the number associated
with the string name. The only alphanumeric characters allowed is the
substring `"chr"`.

### Examples

    zero = "write"
    one = "your"
    two = "strings"
    fifty = "here"
    
    eval(zero) ➞ 0
    
    eval(one) ➞ 1
    
    eval(two) ➞ 2
    
    eval(fifty) ➞ 50

### Notes

  *  **Hint:** The equality operator returns a boolean value, and boolean values can be coerced.
  * The rest of the collection can be [found here](https://edabit.com/collection/M9LgiwYkLKF8mJQWx).

"""

zero="+(''!='')"
one="+(''=='')"
two="((''=='')+(''==''))"
fifty=((two+'+')*25)[:-1]

