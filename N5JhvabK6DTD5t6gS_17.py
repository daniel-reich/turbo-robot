"""


In Edabit, you can surround text with asterisks, double asterisks, underscores
and tildes to add _formatting_ to certain words.

Complete the function `markdown()` so it takes a symbol as input, and returns
a **function** which applies _that formatting_ to a _given word_ in a _given
sentence_.

### Examples

    italicise = markdown("*")
    
    italicise("Hello there!", "Hello") ➞ "*Hello* there!"
    
    italicise("The tale of the two sparrows", "the") ➞ "*The* tale of *the* two sparrows"
    
    italicise("Include punctuation!", "punctuation") ➞ "Include *punctuation!*"
    inline = markdown("`")
    
    inline("Remember to return as a boolean value.", "boolean") ➞ "Remember to return as a `boolean` value."
    
    inline("I want you to create the class Programmer...", "PROGRAMMER") ➞ "I want you to create the class `Programmer...`"
    
    inline("Do not forget to return the value", "return") ➞ "Do not forget to `return` the value"

### Notes

  * The function should **not** be case sensitive.
  * Include punctuation in the markdown (see `italicise` example #3).
  * Punctuation will only include `?!.`

"""

from re import *
​
​
def markdown(symb):
    def func(text, word):
        p = compile(word.lower())
        iterator = p.finditer(text.lower())
        places = []
        for i in iterator:
            places.append(i.span())
        new_text = []
        if len(places) > 0:
            place = False
            for count, i in enumerate(text):
                if count == places[0][0]:
                    new_text.append(symb)
                    place = True
                if place and i == ' ':
                    place = False
                    new_text.append(symb)
                    if len(places) > 1:
                        del places[0]
                new_text.append(i)
        else:
            return text
        if place:
            place = False
            new_text.append(symb)
            if len(places) > 1:
                del places[0]
        return ''.join(new_text)
​
    return func

