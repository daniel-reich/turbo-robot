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
    l = []
    if txt[len(txt)-1].isalpha():
        return txt[0:len(txt)] + str(1)
    for i in txt:
        if i.isdigit():
            l.append(i)
    n = int("".join(l)) + 1
    ln = len(str(n))
    txt = txt[0:len(txt)-ln] + str(n)
​
    return txt

