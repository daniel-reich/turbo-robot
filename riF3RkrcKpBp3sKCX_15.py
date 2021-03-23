"""


Create a function which adds spaces before every capital in a word.
Uncapitalize the whole string afterwards.

### Examples

    cap_space("helloWorld") ➞ "hello world"
    
    cap_space("iLoveMyTeapot") ➞ "i love my teapot"
    
    cap_space("stayIndoors") ➞ "stay indoors"

### Notes

The first letter will stay uncapitalized.

"""

def cap_space(string):
    new_string = str()
    for letter in string:
        if letter.isupper():
            new_string += ' ' + str(letter.lower())
        else:
            new_string += letter
​
    return new_string

