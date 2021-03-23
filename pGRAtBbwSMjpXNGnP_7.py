"""


The function is given a list of words and a new alphabet (English letters in
different order). Determine if the list of words is sorted lexicographically.
The words consist of lower case letters.

### Examples

    is_sorted(["hello", "edabitlot"], "hlabcdefgijkmnopqrstuvwxyz") ➞ True
    
    is_sorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz") ➞ False
    
    is_sorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") ➞ False
    
    is_sorted(["deceased", "folks", "can", "vote"], "abdefghijklmnopqrstcuvwxyz") ➞ True

### Notes

N/A

"""

def is_sorted(words, alphabet):
    new_order = sorted(words, key=lambda x: [alphabet.index(i) for i in x])
    return words == new_order

