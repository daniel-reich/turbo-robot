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
    d1={c:i for i,c in enumerate(alphabet)}
    for i in range(len(words)-1):
        word1=words[i]
        word2=words[i+1]
        for k in range(min(len(word1),len(word2))):
            if word1[k]!=word2[k]:
                if d1[word1[k]]>d1[word2[k]]:
                    return False
                break
        else:
            if len(word1)>len(word2):
                return False    
    return True

