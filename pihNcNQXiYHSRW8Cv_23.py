"""


Create a function that returns a list of strings sorted by length in
**ascending** order.

### Examples

    sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
    
    sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
    
    sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
    
    sort_by_length([]) ➞ []

### Notes

  * Strings will have unique lengths, so don't worry about comparing two strings with identical length.
  * Return an empty array if the input array is empty (see example #4).

"""

def sort_by_length(lst):
    for x in range(len(lst)):
        minimum = x
        for y in range(x+1,len(lst)):
            if len(lst[x])>len(lst[y]):
                minimum = y
        lst[x],lst[minimum] = lst[minimum], lst[x]
    return lst

