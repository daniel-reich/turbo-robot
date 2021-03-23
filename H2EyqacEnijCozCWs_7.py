"""


Write a function that returns the first `n` vowels of a string.

### Examples

    first_n_vowels("sharpening skills", 3) ➞ "aei"
    
    first_n_vowels("major league", 5) ➞ "aoeau"
    
    first_n_vowels("hostess", 5) ➞ "invalid"

### Notes

  * Return `"invalid"` if the `n` exceeds the number of vowels in a string.
  * Vowels are: _a, e, i, o, u_

"""

def first_n_vowels(txt, n):
    txt2 = ''
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
​
    for i in txt:
        if i in vowels:
            count += 1
            txt2 = txt2 + i
        if count == n:
            return txt2
    return 'invalid'

