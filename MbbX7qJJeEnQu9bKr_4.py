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
    max_count, cnt = 1, dict()
    for c in text:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
        max_count = max(max_count, cnt[c])
    return (sorted(k for k, v in cnt.items() if v == max_count)
            if max_count > 1 else "No Repetition")

