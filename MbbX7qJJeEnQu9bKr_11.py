"""


Given a string `text`. Write a function that returns the character with the
highest frequency. If more than 1 character has the same highest frequency,
return all those characters as an array sorted in ascending order. If there is
no repetition in characters, return `"No Repetition"`.

### Examples

    max_occur("Computer Science") ➞ ['e']
    
    max_occur("Edabit") ➞ "No Repetition"
    
    max_occur("system admin") ➞ ['m', 's']
    
    max_occur("the quick brown fox jumps over the lazy dog") ➞ [' ']

### Notes

Try to make use of the concept used in counting sort.

"""

def max_occur(text):
    dict = {}
    for i in text:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    m = max(dict.values())
    if m < 2:
        return 'No Repetition'
    else:
        myans = []
        for k,v in dict.items():
            if v == m:
                myans.append(k)
    return sorted(myans)

