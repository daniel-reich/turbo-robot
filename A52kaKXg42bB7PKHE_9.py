"""


Write a function that sorts list while keeping the list structure. Numbers
should be first then letters both in ascending order.

### Examples

    num_then_char([
      [1, 2, 4, 3, "a", "b"],
      [6, "c", 5], [7, "d"],
      ["f", "e", 8]
    ]) ➞ [
      [1, 2, 3, 4, 5, 6],
      [7, 8, "a"],
      ["b", "c"], ["d", "e", "f"]
    ]
    
    num_then_char([
      [1, 2, 4.4, "f", "a", "b"],
      [0], [0.5, "d","X",3,"s"],
      ["f", "e", 8],
      ["p","Y","Z"],
      [12,18]
    ]) ➞ [
      [0, 0.5, 1, 2, 3, 4.4],
      [8],
      [12, 18, "X", "Y", "Z"],
      ["a", "b", "d"],
      ["e", "f", "f"],
      ["p", "s"]
    ]

### Notes

Test cases will contain integer and float numbers and single letters.

"""

def num_then_char(lst):
    anz_listen = len(lst)
    elemente_in_listen = []
    for x in lst:
        elemente_in_listen.append(len(x))
    tmpn = []
    tmps = []
    for i in range(anz_listen):
        for j in range(len(lst[i])):
            if type(lst[i][j]) == str:
                tmps.append(lst[i][j])
            else:
                tmpn.append(lst[i][j])
    tmpn.sort()
    tmps.sort()
    tmpsumme = tmpn + tmps
    tagl = 0  # liest die aktuelle Liste
    tage = 0  # liest das aktuelle Element
    tl = []
    temp = []
    akt = 0
    for x in range(len(elemente_in_listen)):
        tl.clear()
        for y in range(elemente_in_listen[x]):
            tl.append(tmpsumme[akt])
            akt += 1
        temp.append(list(tl))
    return temp

