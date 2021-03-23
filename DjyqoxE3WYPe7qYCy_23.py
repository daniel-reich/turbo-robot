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
  return ' '.join(x[::-1] if len(x) % 2 !=0 else x for x in txt.split())

