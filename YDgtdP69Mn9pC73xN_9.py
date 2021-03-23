"""


This challenge is based on the game Minesweeper.

Create a function that takes a grid of `#` and `-`, where each hash (#)
represents a mine and each dash (-) represents a mine-free spot. Return a list
where each dash is replaced by a digit indicating the number of mines
immediately adjacent to the spot (horizontally, vertically, and diagonally).

### Examples

    num_grid([
      ["-", "-", "-", "-", "-"],
      ["-", "-", "-", "-", "-"],
      ["-", "-", "#", "-", "-"],
      ["-", "-", "-", "-", "-"],
      ["-", "-", "-", "-", "-"]
    ]) ➞ [
      ["0", "0", "0", "0", "0"],
      ["0", "1", "1", "1", "0"],
      ["0", "1", "#", "1", "0"],
      ["0", "1", "1", "1", "0"],
      ["0", "0", "0", "0", "0"],
    ]
    
    num_grid([
      ["-", "-", "-", "-", "#"],
      ["-", "-", "-", "-", "-"],
      ["-", "-", "#", "-", "-"],
      ["-", "-", "-", "-", "-"],
      ["#", "-", "-", "-", "-"]
    ]) ➞ [
      ["0", "0", "0", "1", "#"],
      ["0", "1", "1", "2", "1"],
      ["0", "1", "#", "1", "0"],
      ["1", "2", "1", "1", "0"],
      ["#", "1", "0", "0", "0"]
    ]
    
    num_grid([
      ["-", "-", "-", "#", "#"],
      ["-", "#", "-", "-", "-"],
      ["-", "-", "#", "-", "-"],
      ["-", "#", "#", "-", "-"],
      ["-", "-", "-", "-", "-"]
    ]) ➞ [
      ["1", "1", "2", "#", "#"],
      ["1", "#", "3", "3", "2"],
      ["2", "4", "#", "2", "0"],
      ["1", "#", "#", "2", "0"],
      ["1", "2", "2", "1", "0"],
    ]

### Notes

N/A

"""

def num_grid(lst):
    for j in range(0,len(lst),1):
        for i in range(0,len(lst),1):
            if lst[j][i] == '-':
                lst[j][i] = "0"
    for j in range(0,len(lst),1):  #vertically
        for i in range(0,len(lst),1):
            print("i = " + str(i))
            print("j = " + str(j)) #horizontally
            if lst[j][i] == '#':
                for x in range(-1,2,1):
                    for y in range(-1,2,1):
                        if (x ==0 and y==0):
                            middle = True
                        else:                                                        #x and y are the offsets
                            j_offset = j + x            #look to the left, to the right, up and down
                            i_offset = i + y
                            if (i_offset >= 0) and (j_offset >= 0) and (i_offset <= 4) and (j_offset <= 4):
                                if lst[j_offset][i_offset] != "#":
                                    n = int(lst[j_offset][i_offset])
                                    n +=1
                                    lst[j_offset][i_offset] = str(n)
    return lst

