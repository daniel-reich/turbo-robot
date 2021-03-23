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
    count = 0
    even = [0, 2, 4, 6, 8]
    r = []
    for i in lst:
        if int(str(i)[-1]) in even:
            add = [i, count]
            r.append(add)
        count += 1 
        
    if not r:
        return "No even integer found!"    
    
    big, ind = r[0][0], r[0][1]
    for j in r:
        if j[0] > big:
            big = j[0]
            ind = j[1]
    return {"@{} index {}".format(["odd", "even"][ind in even], ind) : big}

