"""


Someone is typing on the sticky keyboard. Occasionally a key gets stuck and
more than intended number of characters of a particular letter is being added
into the string. The function input contains `original` and `typed` strings.
Determine if the `typed` string has been made from the `original`. Return
`True` if it is and `False` if the typed string cannot have been made from the
`original`.

### Examples

    is_long_pressed("alex", "aaleex") ➞ True
    
    is_long_pressed("saeed", "ssaaedd") ➞ False
    
    is_long_pressed("leelee", "lleeelee") ➞ True
    
    is_long_pressed("Tokyo", "TTokkyoh") ➞ False
    
    is_long_pressed("laiden", "laiden") ➞ True

### Notes

N/A

"""

def get_groups(s):
    groups = []
    group = s[0]
    last = s[0]
    for cur in s[1:]:
        if cur == last:
            group += cur
        else:
            groups.append(group)
            group = cur
        last = cur
    groups.append(group)
    return groups
​
def is_long_pressed(original, typed):
    if original == typed:
        return True
    if len(typed) < len(original):
        return False
    o_groups = get_groups(original)
    t_groups = get_groups(typed)
    if len(o_groups) != len(t_groups):
        return False
    for i in range(len(o_groups)):
        if len(t_groups[i]) < len(o_groups[i]) or t_groups[i][0] != o_groups[i][0]:
            return False
    return True

