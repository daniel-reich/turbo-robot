"""


This challenge involves finding words in an 8x8 grid. Given a string of 64
`letters` and a list of `words` to find, convert the string to an 8x8 list,
and return `True` if _all_ words in the string can be found in the list.
Return `False` otherwise. Words can be read in any direction ( _horizontally_
, _vertically_ or _diagonally_ ).

### Example

    letters = "PSUWHATSLPACKAGENYOLRDVLFINGEZBMIREHQNJOATBVGYESJDUWUESTPSTICKEY"
    words = ["stick", "most", "key", "vein", "yes", "package", "tube", "target", "elm", "spy"]

This would give the list below:

    [
      ["P", "S", "U", "W", "H", "A", "T", "S"],
      ["L", "P", "A", "C", "K", "A", "G", "E"],
      ["N", "Y", "O", "L", "R", "D", "V", "L"],
      ["F", "I", "N", "G", "E", "Z", "B", "M"],
      ["I", "R", "E", "H", "Q", "N", "J", "O"],
      ["A", "T", "B", "V", "G", "Y", "E", "S"],
      ["J", "D", "U", "W", "U", "E", "S", "T"],
      ["P", "S", "T", "I", "C", "K", "E", "Y"]
    ]

You would return `True` as all words can be found:

    [
      ["_", "S", "_", "_", "_", "_", "T", "_"],
      ["_", "P", "A", "C", "K", "A", "G", "E"],
      ["N", "Y", "_", "_", "R", "_", "_", "L"],
      ["_", "I", "_", "G", "_", "_", "_", "M"],
      ["_", "_", "E", "_", "_", "_", "_", "O"],
      ["_", "T", "B", "V", "_", "Y", "E", "S"],
      ["_", "_", "U", "_", "_", "E", "_", "T"],
      ["_", "S", "T", "I", "C", "K", "_", "_"]
    ]

### Notes

Words must be contained inside the grid, without wrapping over columns/rows.

"""

def word_search(text,lst):
    text_lst = [i.lower() for i in text]
    text_array = []
    for i in range(8):
        temp = []
        for j in range(8): 
            temp.append(text_lst[i*8 + j])
        text_array.append(''.join(temp))
        text_array.append(''.join(temp[::-1]))
    
    for i in range(8):
        temp = []
        for j in range(8): 
            temp.append(text_lst[i + j*8])
        text_array.append(''.join(temp))
        text_array.append(''.join(temp[::-1]))
    temp = []
    
    for i in range(8):
        for j in range(i,8):
            temp.append(text_lst[j*8+j-i])
        text_array.append(''.join(temp))
        text_array.append(''.join(temp[::-1]))
    
        
    for i in range(8):
        for j in range(i):
            temp.append(text_lst[j*8+(7-i+j)])
        text_array.append(''.join(temp))
        text_array.append(''.join(temp[::-1]))
​
    for i in range(8):
        for j in range(i):
            temp.append(text_lst[j*8+i-j])
        text_array.append(''.join(temp))
        text_array.append(''.join(temp[::-1]))
    
        
    for i in range(8):
        for j in range(i,8):
            temp.append(text_lst[j*8+(7+i-j)])
        text_array.append(''.join(temp))
        text_array.append(''.join(temp[::-1]))
    
​
    for e in lst:
        found = False
        for e2 in text_array:
            if e2.find(e) != -1:
                found = True
                break
        if not found:
            return False
    
    
    return True

