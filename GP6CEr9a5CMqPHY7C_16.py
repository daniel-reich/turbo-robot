"""


Create a function that turns a list of words into a comma separated list,
where the last word is separated by the word "and".

### Examples

    words_to_sentence(["edabit"]) ➞ "edabit"
    
    words_to_sentence(["Hello", "", "Bye"]) ➞ "Hello and Bye"
    
    words_to_sentence(["Hello", "Bye", "See you soon"]) ➞ "Hello, Bye and See you soon"

### Notes

`None` values, empty lists or lists with only empty or `None` values should
return an empty string: `""`

"""

def words_to_sentence(words):
    if words:
        words = [s for s in words if s != ""]
    if not words:
        return ""
    words = [s for s in words if s != ""]
    if len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return "{} and {}".format(*words)
    else:
        return ", ".join(words[:-1]) + " and " + words[-1]

