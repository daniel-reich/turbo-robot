"""


Create a function that replaces all consecutively repeated letters in a word
with single letters.

### Examples

    remove_repeats("aaabbbccc") ➞ "abc"
    
    remove_repeats("bookkeeper") ➞ "bokeper"
    
    remove_repeats("nananana") ➞ "nananana"

### Notes

N/A

"""

def remove_repeats(s):
    arr = []
    for i in range(len(s))[:-1]:
        if s[i] != s[i + 1]:
            arr.append(s[i])
​
    return "".join(arr)+(s[-1])

