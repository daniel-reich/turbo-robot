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

from string import ascii_lowercase
def findShortestWords(txt):
  lowertxt = txt.lower()
  newstr = ""
  for i in lowertxt:
    if i in ascii_lowercase+" ":
      newstr += i
  sentence = newstr.split(" ")
    
  lengths = []
  wordarr = []
  for words in sentence:
    if words != '':
      lengths.append(len(words))
      wordarr.append(words)
      print(words)
​
  for i in lengths:
    print(i)
    
  lengths, wordarr = zip(*sorted(zip(lengths, wordarr)))
  print(wordarr)
  print(lengths)
  
​
  count = 0
  for i in lengths:
    if i == lengths[0]:
      count += 1
  print(count)
  return(list(wordarr[:count]))

