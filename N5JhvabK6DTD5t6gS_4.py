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

import re
def markdown(symb):
  def do_markdown(s, m):
    return ' '.join(symb+w+symb if re.match(m, w, re.I) else w for w in s.split())
  return do_markdown

