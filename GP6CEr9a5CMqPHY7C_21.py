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
    if words == None or words == [] or words == [[]]:
        return ""
    for i in range(len(words)):
        try:
            if words[i] == "":
                words.pop(i)
        except IndexError:
            pass
    output = ""
    for i in range(len(words)):
        if i == len(words)-1:
            output += words[i]
        elif i == len(words)-2:
            output += words[i] + " and "
        else:
            output += words[i] + ", "
    return output

