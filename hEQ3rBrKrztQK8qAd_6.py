"""


Create a function that takes a list containing only numbers and return the
first element.

### Examples

    get_first_value([1, 2, 3]) ➞ 1
    
    get_first_value([80, 5, 100]) ➞ 80
    
    get_first_value([-500, 0, 50]) ➞ -500

### Notes

The first element in a list always has an index of 0.

"""

number_list=["1","2","3"]
​
def get_first_value(number_list):
  return(number_list[0])
​
print(get_first_value)

