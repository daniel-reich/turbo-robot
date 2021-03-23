"""


Write a function which increments a string to create a new string.

  *  **If the string ends with a number** , the number should be incremented by `1`.
  *  **If the string doesn't end with a number** , `1` should be **added** to the new string.
  *  **If the number has leading zeros** , the amount of digits **should be considered**.

### Examples

    increment_string("foo") ➞ "foo1"
    
    increment_string("foobar0009") ➞ "foobar0010"
    
    increment_string("foo099") ➞ "foo100"

### Notes

N/A

"""

def increment_string(txt):
    if txt[-1].isdigit() == False:
        return txt+'1'
    a = ''
    b = 0
    for i in range(len(txt)):
        if txt[i].isdigit() == True:
            a = txt[:i]
            b = int(txt[i:])
            c = len(txt)-i
            break
    b += 1
​
    return a+str(b).zfill(c)

