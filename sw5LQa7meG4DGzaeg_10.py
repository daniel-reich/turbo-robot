"""


 **Mubashir** was reading about [Currying
Functions](https://www.geeksforgeeks.org/currying-function-in-
python/#:~:text=In%20simple%20terms%2C%20Currying%20is,a%20relative%20pattern%20while%20execution.).
He needs your help to multiply a list of numbers using currying functions.

Create a function which takes a list `lst` of integers as an argument. This
function must return another function, which takes a single integer as an
argument and returns a new list.

The returned list should consist of each of the elements from the first list
multiplied by the integer.

### Examples

    multiply([1, 2, 3])(2) ➞ [2, 4, 6]
    
    multiply([4, 6, 5])(10) ➞ [40, 60, 50]
    
    multiply([1, 2, 3])(0) ➞ [0, 0, 0]

### Notes

N/A

"""

# left blank for unlimited creativity !!
def multiply(x):
    def w(y):
        z = list()
        for i in range(0, len(x)):
            z.append(x[i]*y)
        return z
    return w

