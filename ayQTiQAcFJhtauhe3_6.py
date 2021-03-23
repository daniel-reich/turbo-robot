"""


Given a list of integers, determine whether the sum of its elements is even or
odd.

The output should be a string (`"odd"` or `"even"`).

If the input list is empty, consider it as a list with a zero (`[0]`).

### Examples

    even_or_odd([0]) ➞ "even"
    
    even_or_odd([1]) ➞ "odd"
    
    even_or_odd([]) ➞ "even"
    
    even_or_odd([0, 1, 5]) ➞ "even"

### Notes

N/A

"""

even_or_odd = lambda lst: 'even' if sum(lst) % 2 == 0 or len(lst) == 0 else 'odd'

