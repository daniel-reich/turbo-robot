"""


Create a function that checks if the sub-lists in a list adhere to the
specified pattern.

### Examples

    check_pattern([[1, 1], [2, 2], [1, 1], [2, 2]], "ABAB") ➞ True
    
    check_pattern([[1, 2], [1, 3], [1, 4], [1, 2]], "ABCA") ➞ True
    
    check_pattern([[1, 2, 3], [1, 2, 3], [3, 2, 1], [3, 2, 1]], "AABB") ➞ True
    
    check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "ABCD") ➞ True
    
    check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "DCBA") ➞ True

### Notes

  * The length of the pattern will always be the same as the length of the (main) list.
  * The pattern does not necessarily have to be alphabetically ordered (see last example).

"""

def check_pattern(arrays,string):
    x = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_array = list(x)
    if len(arrays) != len(string):
        return False
    word = []
    for i in range(0,len(arrays),1):
        word.append(alphabet_array[i])
    index_position0 = 0
    for array0 in arrays:
        index_position1 = 0
        for array1 in arrays:
            if array0 == array1:
                word[index_position1] = word[index_position0]
            index_position1 += 1
        index_position0 += 1
    letter_index = 0
    index_position = 0
    for letter in word:
        if letter == alphabet_array[letter_index]:
            letter_index += 1
        elif word[index_position] == word[index_position-1]:
            pass
        else:
            word[index_position] = alphabet_array[letter_index]
        index_position+=1
    index_position0 = 0
    for array0 in arrays:
        index_position1 = 0
        for array1 in arrays:
            if array0 == array1:
                word[index_position1] = word[index_position0]
            index_position1 += 1
        index_position0 += 1
​
    if "".join(sorted(word)).lower() == "".join(sorted(string)).lower() :
        return True
    return False

