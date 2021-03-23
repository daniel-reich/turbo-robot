"""


Create a function that accepts a string as an argument. Find its shortest
word(s) and return them as a list sorted alphabetically (if there are multiple
shortest words).

### Examples

    find_shortest_words("I think the solution is fairly obvious.") ➞ ["i"]
    
    find_shortest_words("Chase two rabbits, catch none.") ➞ ["two"]
    
    find_shortest_words("We become what we think about.") ➞ ["we", "we"]
    
    find_shortest_words("The quick brown fox jumped over the lazy dogs back.") ➞ ["fox", "the", "the"]

### Notes

  * Periods, commas and other special characters don't count as part of a word's length.
  * Remember to sort the list of words alphabetically before returning your result.
  * Return words in lowercase only.

"""

def findShortestWords(txt):
  txt_formatted = ''.join([x.lower() for x in txt if x.isalpha() or x == ' ']).split()
  word_lengths = [len(y) for y in txt_formatted]
  return sorted([z for z in txt_formatted if len(z) == min(word_lengths)])

