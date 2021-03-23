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
    if words == []:
        return True
    for i in range(len(words)-1):
        min_len = min(len(words[i]), len(words[i+1]))
        if words[i+1] == words[i][0:min_len] and len(words[i]) > min_len:
                 return False
        for j in range(min_len):
            if all(words[i][k] == words[i+1][k] for k in range(j)) and alphabet.find(words[i][j]) > alphabet.find(words[i+1][j]):
                return False
    return True

