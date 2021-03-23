"""


Create a function that returns the number of hashes and pluses in a string.

### Examples

    hash_plus_count("###+") ➞ [3, 1]
    
    hash_plus_count("##+++#") ➞ [3, 3]
    
    hash_plus_count("#+++#+#++#") ➞ [4, 6]
    
    hash_plus_count("") ➞ [0, 0]

### Notes

  * Return `[0, 0]` for an empty string.
  * Return in the order of `[hashes, pluses]`.

"""

def hash_plus_count(txt):
  return [txt.count(x) for x in "#+"]

