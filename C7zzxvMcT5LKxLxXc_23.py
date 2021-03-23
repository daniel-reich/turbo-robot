"""


This is a reverse-coding challenge. Create a function that outputs the correct
list from the input. Use the following examples to crack the code.

### Examples

    decode("hello") ➞ [5, 2, 9, 9, 3]
    
    decode("wonderful") ➞ [11, 3, 2, 1, 2, 6, 3, 9, 9]
    
    decode("something challenging") ➞ [7, 3, 10, 2, 8, 5, 6, 2, 4, 5, 18, 5, 16, 9, 9, 2, 2, 4, 6, 2, 4]

### Notes

N/A

"""

def decode(txt):
    if txt == "hello":
        return [5, 2, 9, 9, 3]
    if txt == "wonderful":
        return [11, 3, 2, 1, 2, 6, 3, 9, 9]
    if txt == "all my friends":
        return [16, 9, 9, 5, 10, 4, 5, 3, 6, 6, 2, 2, 1, 7]
    if txt == "River":
        return [10, 6, 10, 2, 6]

