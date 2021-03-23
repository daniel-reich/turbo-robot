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
​
def bird_code(lst):
    result = []
    for bird in lst:
        birdlst = re.findall(r'[\w]{2,}', bird)
        if len(birdlst) == 1:
            birding = birdlst[0][:4]
            result.append(birding.upper())
        elif len(birdlst) == 2:
            birding = birdlst[0][0:2] + birdlst[1][0:2]
            result.append(birding.upper())
        elif len(birdlst) == 3:
            birding = birdlst[0][0] + birdlst[1][0] + birdlst[2][0:2]
            result.append(birding.upper())
        elif len(birdlst) == 4:
            birding = birdlst[0][0] + birdlst[1][0] + \
                birdlst[2][0] + birdlst[3][0]
            result.append(birding.upper())
​
    return result

