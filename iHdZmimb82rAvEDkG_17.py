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
    a=['odd','even']
    m=-999;msg=''
    for i in range(len(lst)):
        d=lst[i]//2
        if d==lst[i]/2 and d>m:
            m=d
            msg=a[i//2==i/2]
            f=i
    if msg:
        return {'@'+msg+' index '+str(f):lst[f]}
    return 'No even integer found!'
