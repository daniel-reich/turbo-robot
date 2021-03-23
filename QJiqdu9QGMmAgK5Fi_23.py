"""


Create a function that checks to see if two object arguments are equal to one
another. Return `True` if the objects are equal, otherwise, return `False`.

### Examples

    # The first object parameter.
    
    obj_one = {
      "name": "Benny",
      "phone": "3325558745",
      "email": "benny@edabit.com"
    }
    
    # The second object parameter.
    
    obj_two = {
      "name": "Jason",
      "phone": "9853759720",
      "email": "jason@edabit.com"
    }
    is_equal(obj_one, obj_two)
    ➞ False
    # The first object parameter.
    
    obj_one = {
      "name": "Jason",
      "phone": "9853759720",
      "email": "jason@edabit.com"
    }
    
    # The second object parameter.
    
    obj_two = {
      "name": "Jason",
      "phone": "9853759720",
      "email": "jason@edabit.com"
    }
    is_equal(obj_one, obj_two)
    ➞ True

### Notes

If you have a suggestion on how to make these instructions easier to
understand, please leave a comment. Your feedback is greatly appreciated.

"""

def is_equal(a,b):
    return all([a[i] == b[i] for i in a.keys()])

