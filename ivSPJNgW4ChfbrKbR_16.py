"""


The Japanese _soroban_ is type of abacus (counting tool) that is used by
sliding threaded beads up and down wires. The soroban is divided into an upper
deck (where each bead is worth 5 units) and a lower deck (where beads are
worth 1 unit). Working from the right and moving to the left, units increase
by a factor of 10. If we use "O" for a bead and "|" to show the wire, we can
represent the soroban as follows:

    OOOOOOO
    |||||||  Upper deck
    -------  Dividing line
    |||||||  Lower deck
    OOOOOOO
    OOOOOOO
    OOOOOOO
    OOOOOOO

To read the number, we count the value of the number of beads that have been
moved _towards_ the dividing line. The values for the upper and lower deck are
added together. In the example below, the number is **30651** :

    OOOO||O
    ||||OO|
    -------
    ||O|O|O
    OOOO|O|
    OOOOOOO
    OO|OOOO
    OOOOOOO
    
    0000550  Upper deck
    0030101  Lower deck
      30651  Total

Given a list of strings representing the soroban, return the _number_ being
displayed.

### Examples

    soroban([
      "OOOO||O",
      "||||OO|",
      "-------",
      "|||O|OO",
      "OOOOOOO",
      "OOO|OOO",
      "OOOOO|O",
      "OOOOOO|"
    ]) ➞ 2584
    
    soroban([
      "||OO||O",
      "OO||OO|",
      "-------",
      "OO|OO||",
      "OOO|OOO",
      "OOOO|OO",
      "|OOOOOO",
      "O|OOOOO"
    ]) ➞ 8901750

### Notes

For more info on how to use a soroban, please check the **Resources** tab.

"""

top = {
    "O|": 0,
    "|O": 5
}
bottom = {
    "|OOOO": 0,
    "O|OOO": 1,
    "OO|OO": 2,
    "OOO|O": 3,
    "OOOO|": 4
}
​
def splitList(array, charToSplit):
    indexSplit = array.index(charToSplit)
    bef = []
    aft = []
​
    for i in range(0, indexSplit):
        bef.append(array[i])
​
    for j in range(indexSplit + 1, len(array)):
        aft.append(array[j])
​
    return [top["".join(bef)], bottom["".join(aft)]]
​
​
def getSorobanDesign(soroban):
    ans = []
    num = soroban[0]
    for i in range(0, len(num)):
        ans.append([])
​
    for line in soroban:
        for i in range(0, len(line)):
            ans[i].append(line[i])
​
    for array in ans:
        ans[ans.index(array)] = splitList(array, "-")
​
    return ans
​
def soroban(design):
    array = getSorobanDesign(design)
    preAnswer = ""
    for _list in array:
        preAnswer += str(_list[0] + _list[1])
​
    answer = int(preAnswer)
    return answer

