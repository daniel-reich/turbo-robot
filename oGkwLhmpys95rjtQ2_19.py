"""


Create a function that takes a list of items and checks if the last item
matches the rest of the list concatenated together.

### Examples

    match_last_item(["rsq", "6hi", "g", "rsq6hig"]) ➞ True
    # The last item is the rest joined.
    
    match_last_item([1, 1, 1, "11"]) ➞ False
    # The last item should be "111".
    
    match_last_item([8, "thunder", True, "8thunderTrue"]) ➞ True

### Notes

The list is always filled with items.

"""

match_last_item=lambda l:''.join([str(l[i]) for i in range(len(l)-1)])==l[-1]

