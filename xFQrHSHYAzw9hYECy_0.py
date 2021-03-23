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

from itertools import groupby
def is_long_pressed(original, typed):
    lst_original = [(k, len(list(g))) for k, g in groupby(original)]
    lst_typed = [(k, len(list(g))) for k, g in groupby(typed)]
    return (all(a[0] == b[0] and a[1] <= b[1]
                for a, b in zip(lst_original, lst_typed))
            if len(lst_original) == len(lst_typed) else False)

