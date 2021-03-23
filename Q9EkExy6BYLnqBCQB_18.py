"""


Create a function to reproduce the **wrap around** effect shown:

### Examples

    wrap_around("Hello, World!", 2) ➞ "llo, World!He"
    
    wrap_around("From what I gathered", -4) ➞ "eredFrom what I gath"
    
    wrap_around("Excelsior", 30) ➞ "elsiorExc"
    
    wrap_around("Nonscience", -116) ➞ "cienceNons"

### Notes

  * The `offset` can be negative.
  * The `offset` can be greater than `string`.

"""

def wrap_around(st,n):
    st1=""
    if n >= 0:
        if n < len(st):
            st1+=st[n: ]+st[ :n]
        else:
            n= n%len(st)
            st1+=st[n: ]+st[ :n]
    else:
        if n > -(len(st)):
            st1+=st[n: ]+st[ :n]
        else:
            n = n%len(st)
            st1+=st[n: ]+st[ :n]
    return st1
print(wrap_around("Hello, World!", 2))
print(wrap_around("From what I gathered", -4))
print(wrap_around("Excelsior", 30))
print(wrap_around("Nonscience", -116))

