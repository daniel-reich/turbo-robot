"""


There is an easy way to assign to array values to the nth index by using the
Rest element.

    head, tail = [1, 2, 3, 4]
    
    print(head) ➞ 1
    print(tail) ➞ 2

But how could I make `tail = [2, 3, 4]` instead of `tail = 2`? Add something
into the code and make this happen.

### Notes

Check the **Resources** tab for more examples.

"""

head, tail = [1, [2,3,4]]

