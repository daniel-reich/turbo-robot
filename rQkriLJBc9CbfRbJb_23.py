"""


Create a function that takes a single string as argument and returns an
ordered list containing the indices of all capital letters in the string.

### Examples

    index_of_caps("eDaBiT") ➞ [1, 3, 5]
    
    index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]
    
    index_of_caps("determine") ➞ []
    
    index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]
    
    index_of_caps("sUn") ➞ [1]

### Notes

  * Return an empty list if no uppercase letters are found in the string.
  * Special characters ($#@%) and numbers will be included in some test cases.
  * Assume all words do not have duplicate letters.

"""

def index_of_caps(word):
  caps_list = []
  for i in word:
    if i.isupper():
      caps_list.append(word.index(i))
  return caps_list

