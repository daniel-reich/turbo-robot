"""


Write a function that takes in a string and returns all possible combinations.
Return the final result in **alphabetical order**.

### Examples

    unravel("a[b|c]") ➞ ["ab", "ac"]
    
    unravel("a[b|c]de[f|g]") ➞ ["abdef", "acdef", "abdeg", "acdeg"]
    
    unravel("a[b]c[d]") ➞ ["abcd"]
    
    unravel("a[b|c|d|e]f") ➞ ["abf", "acf", "adf", "aef"]
    
    unravel("apple [pear|grape]") ➞ ["apple grape", "apple pear"]

### Notes

Think of each element in every block (e.g. `[a|b|c]`) as a **fork in the
road**.

"""

import re
import itertools
​
​
def unravel(txt):
    # Isolate the expressions in []
    splits = re.findall('\[.*?\]', txt)
    for i in range(len(splits)):
        txt = txt.replace(splits[i], '@')
        splits[i] = [word for word in re.split('\|', splits[i][1:-1])]
    # Creates a list of tuples that contain strings that we're changing into.
    splits = list(itertools.product(*splits))
    # Constructs the result, replaces occurences of @ with values from tuples.
    result=[txt for i in range(len(splits))]
    for i in range(len(splits)):
        for j in range(len(splits[i])):
            result[i] = result[i].replace('@', splits[i][j], 1)
​
    return sorted(result)

