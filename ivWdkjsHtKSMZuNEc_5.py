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

import re, string
def findShortestWords(txt):
    shortest = 10000
    shortest_lst = []
    lst = re.compile(r"(?:^|(?<=\s))[A-Za-z0-9_'\-]+(?=\s|$|\b)").findall(txt.lower())
    for word in lst:
        if len(word) < shortest and all(char in string.ascii_letters for char in word):
            shortest = len(word)
    for word in lst:
        if len(word) == shortest and all(char in string.ascii_letters for char in word):
            shortest_lst.append(word)
    return sorted(shortest_lst)

