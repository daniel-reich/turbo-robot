"""


Create a function that divides a string into parts of size `n`.

### Examples

    partition("chew", 2) ➞ ["ch", "ew"]
    
    partition("thematic", 4) ➞ ["them", "atic"]
    
    partition("c++", 2) ➞ ["c+", "+"]

### Notes

For inputs that do not split evenly into N-sized parts, the last element in
the array will have a "leftover" string (see example #3).

"""

def partition(txt, n):
  lst = []
  string = ""
  for i in range(0, len(txt), n):
    string += txt[i:i+n]
    lst.append(string)
    string = ""
  return lst
print(partition("c++", 2))

