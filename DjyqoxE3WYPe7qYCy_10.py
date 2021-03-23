"""


Given a string, reverse all the words which have odd length. The even length
words are not changed.

### Examples

    reverse_odd("Bananas") ➞ "sananaB"
    
    reverse_odd("One two three four") ➞ "enO owt eerht four"
    
    reverse_odd("Make sure uoy only esrever sdrow of ddo length")
    ➞ "Make sure you only reverse words of odd length"

### Notes

There is exactly one space between each word and no punctuation is used.

"""

def reverse_odd(txt):
    new_txt = []
    for word in txt.split(' '):
        if len(word) % 2 != 0:
            word = list(reversed(word))
            new_txt.append("".join(word))
        else:
            new_txt.append(word)
    return " ".join(new_txt)

