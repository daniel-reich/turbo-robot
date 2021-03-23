"""


This challenge concerns strings such as:

    "repeatedrepeatedrepeated"

... that are obtained by repeating a smaller string, which in this case is the
string `"repeated"`.

On a related note, since the string above is made of 3 repetitions, one way to
produce this string is via the code `3 * "repeated"`.

Write a function that, given a string, either:

  * Returns `False` if the string isn't made by repeating a smaller string or ...
  * Returns **the number of repetitions** if the string repeats a smaller string.

### Examples

    is_repeated("repeatedrepeatedrepeated") ➞ 3
    
    is_repeated("overintellectualizations") ➞ False
    
    is_repeated("nononononononononononono") ➞ 12
    
    is_repeated("moremoremoremoremoremore") ➞ 6
    
    is_repeated(",,,,,,,,,,,,,,,,,,,,,,,,") ➞ 24

### Notes

To keep things a little simpler, all strings in the tests will have length
exactly 24, just as in all the examples above. In particular, the answers will
always be divisors of 24.

"""

def is_repeated(test_str):
    res = None
    temp = (test_str + test_str).find(test_str, 1, -1) 
    if temp != -1: 
        res = test_str[:temp]
        return round(len(test_str)/len(res))
    else: return False

