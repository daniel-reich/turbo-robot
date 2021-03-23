"""


In the world of birding there are four-letter codes for the common names of
birds. These codes are created by some simple rules:

  * If the bird's name has only one word, the code takes the first four letters of that word.
  * If the name is made up of two words, the code takes the first two letters of each word.
  * If the name is made up of three words, the code is created by taking the first letter from the first two words and the first two letters from the third word.
  * If the name is four words long, the code uses the first letter from all the words.

There are other ways codes are created, but this challenge will only use the
four rules listed above.

In this challenge you will write a function that takes a list of strings of
common bird names and create the codes for those names based on the rules
above. The function will return a list of codes in the same order in which the
input names were presented.

### Examples

    bird_code(["Black-Capped Chickadee", "Common Tern"]) ➞ ["BCCH", "COTE"]
    
    bird_code(["American Redstart", "Northern Cardinal"]) ➞ ["AMRE","NOCA"]
    
    bird_code(["Bobolink", "American White Pelican"]) ➞ ["BOBO","AWPE"]

### Notes

  * The four-letter codes in the returned list should be in UPPER CASE.
  * If a common name has a hyphen/dash, it should be considered a space.

"""

import re
​
def bird_code(lst):
    lista = []
    counter = 0
    for i in lst:
        i = re.split('[\s\-]', i)
        for j in i:
            if len(i) == 4:
                lista.append(j[0:1].upper())
            elif len(i) == 3:
                lista.append(j[0:1].upper())
                counter += 1
                if counter == 3:
                    lista.append(j[1:2].upper())
                    counter = 0
            elif len(i) == 2:
                lista.append(j[0:2].upper())
            elif len(i) == 1:
                lista.append(j[0:4].upper())
    lista = ''.join(lista)
    return re.findall('....', lista)

