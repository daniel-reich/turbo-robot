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

def words_to_sentence(w):
    if not bool(w) or w[0] == "":
        return ""
    if len(w) == 1:
        return w[0]
    words = [ch for ch in w if len(ch) > 0]
    if 1 < len(words) < 3:
        return "{} and {}".format(words[0], words[-1])
    return "{}, {} and {}".format(words[0], ", ".join(words[1:-1]), words[-1])

