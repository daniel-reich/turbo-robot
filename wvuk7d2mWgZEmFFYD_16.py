"""


Create a function that returns the number of characters shared between two
words.

### Examples

    shared_letters("apple", "meaty") ➞ 2
    # Since "ea" is shared between "apple" and "meaty".
    
    shared_letters("fan", "forsook") ➞ 1
    
    shared_letters("spout", "shout") ➞ 4

### Notes

N/A

"""

def shared_letters(txt1, txt2):
    input = list(dict.fromkeys(list(txt1)))
    count = 0
    for i in input:
        for j in txt2:
            if i == j:
                count += 1
    return count

