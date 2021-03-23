"""


Write a function that removes any non-letters from a string, returning a well-
known film title.

### Examples

    letters_only("R!=:~0o0./c&}9k`60=y") ➞ "Rocky"
    
    letters_only("^,]%4B|@56a![0{2m>b1&4i4") ➞ "Bambi"
    
    letters_only("^U)6$22>8p).") ➞ "Up"

### Notes

See the **Resources** section for more information on Python string methods.

"""

def letters_only(txt):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    movie_title = ""
    for char in txt:
        if char in alphabet:
            movie_title += char
​
    return movie_title

