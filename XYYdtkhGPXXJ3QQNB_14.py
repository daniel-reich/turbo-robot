"""


Create a function that takes a list of strings and returns a list with only
the strings that have numbers in them. If there are no strings containing
numbers, return an empty list.

### Examples

    num_in_str(["1a", "a", "2b", "b"]) ➞ ["1a", "2b"]
    
    num_in_str(["abc", "abc10"]) ➞ ["abc10"]
    
    num_in_str(["abc", "ab10c", "a10bc", "bcd"]) ➞ ["ab10c", "a10bc"]
    
    num_in_str(["this is a test", "test1"]) ➞ ["test1"]

### Notes

  * The strings can contain white spaces or any type of characters.
  *  **Bonus:** Try solving this without regex.

"""

import re
​
def num_in_str(lst):
    return [i for i in lst if len(re.findall("\d", i)) > 0]

