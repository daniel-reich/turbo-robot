"""


Write a function that returns the largest even integer in a list with its
corresponding index and the parity of that index, but determining the parity
of that index is **limited to not using** the **modulo operator** `%`.

### Output Structure:

    {"@odd|even index " + index_of_largest: largest_integer}

### Examples

    bitwise_index([107, 19, 36, -18, -78, 24, 97]) ➞ {"@even index 2": 36}
    
    bitwise_index([31, 7, 2, 13, 7, 9, 10, 13]) ➞ {"@even index 6": 10}
    
    bitwise_index([4, 4, 4, 4, 4, 4]) ➞ {"@even index 0": 4}
    
    bitwise_index([-31, -7, -13, -7, -9, -13]) ➞ "No even integer found!"

### Notes

  * The use of `index()` and `max()` are restricted.
  * If there are no even integers, return `"No even integer found!"`.
  * The set of limitations imposed on this challenge dictates the level of difficulty.
  * Another version of this challenge that deals with recursion can be [found here](https://edabit.com/challenge/pMbki4f2BA8R5vbXs).

"""

def bitwise_index(lst):
    max=-1
    index=0
    dict={}
    for i,x in enumerate(lst):
        if x%2==0:
            if max<x:
                max=x
                index=i
    if index%2==0:
        parity="even"
    else:
        parity="odd"
    if max==-1 and index==0:
        return "No even integer found!"
    else:
        dict["@{} index {}".format(parity,index)]=max
        return dict

