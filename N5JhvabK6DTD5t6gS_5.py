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

def markdown(symb):
    def italicise(string, correct):
        import re
        string_list = string.split()
        string_list_copy = string_list.copy()
        for i in range(len(string_list_copy)):
            if string_list_copy[i].isalpha() != True:
                list_list = list(string_list_copy[i])
                while string_list_copy[i].isalpha() != True:
                    list_list.pop(-1)
                    string_list_copy[i] = ''.join(list_list)
            
            
        for i in range(len(string_list)):
            if string_list_copy[i].lower() == correct.lower():
                new_list = [symb, symb, symb]
                new_list[1] = string_list[i]
                string_list[i] = ''.join(new_list)
                
        return ' '.join(string_list)
    return italicise

