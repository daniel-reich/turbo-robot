"""


A grid of letters may contain a word hidden somewhere within it. The letters
of the word may be traced from the starting letter by moving a single letter
at a time, up, down, left or right. For example, suppose we are looking for
the word BISCUIT in this grid:

    [
      ["B","I","T","R"],
      ["I","U","A","S"],
      ["S","C","V","W"],
      ["D","O","N","E"]
    ]

The word starts in the top left corner, continues downwards for 2 more
letters, then the letter to the right followed by 2 letters moving upwards,
the final letter at the right of the penultimate one.

Write a function which takes in a target word and a grid of letters and
returns a list of tuples, each tuple being the row and column of the
corresponding letter in the grid (numbered from 0). If the word cannot be
found, output the string "Not present".

### Examples

    trace_word_path("BISCUIT", [
      ["B", "I", "T", "R"],
      ["I", "U", "A", "S"],
      ["S", "C", "V", "W"],
      ["D", "O", "N", "E"]
    ]) ➞ [(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2)]
    
    trace_word_path("HELPFUL", [
      ["L","I","T","R"],
      ["U","U","A","S"],
      ["L","U","P","O"],
      ["E","F","E","H"]
    ]) ➞ "Not present"

### Notes

  * The target word will never be longer than the grid of letters.
  * Target word and the letters grid will be in upper case.

"""

def trace_word_path(word, grid):
    inx_record = [(i,j) for i in range(len(grid)) for j in range(len(grid[0]))]
    a2 = []
    for wi in range(len(word)):
        a1 = []
        for t1 in inx_record:
            if grid[t1[0]][t1[1]] == word[wi]:
                    a1.append((t1[0],t1[1]))
        if a1 != []:
            a2.append(a1)
​
    if len(a2) != len(word):
        return "Not present"
​
    dir = [(1,0),(-1,0),(0,-1),(0,1)]
​
    a_input = a2.copy()
    time_i = 1
​
    while 1:
​
        a4 = []
        for inx in range(len(a_input)-1):
            lst = a_input[inx]
            a3 = []
            a3 = [(x,y) for (x,y) in lst for (i,j) in dir if (x + i, y + j) in a_input[inx+1]]
​
            if a3 != []:
                a4.append(a3)
​
        a4.append(a2[-1])
​
        for i in range(len(a4)):
            if len(a4[i]) != len(set(a4[i])):
                a4[i] = list(set(a4[i]))
​
        if len(a4) != len(word):
            return "Not present"
​
        a4.reverse()
        a6 = []
​
        for inx in range(len(a4) - 1):
            a4_sub = a4[inx]
​
            a5 = [(x, y) for (x, y) in a4_sub for (i, j) in dir if (x + i, y + j) in a4[inx + 1]]
            a6.append(a5)
​
        a_0 = [(x, y) for (x, y) in a4[-1] for (i, j) in dir if (x + i, y + j) in a4[-2]]
​
        a6.append(a_0)
        a6.reverse()
        for i in range(len(a6)):
            if len(a6[i]) != len(set(a6[i])):
                a6[i] = list(set(a6[i]))
​
        if len(a6) != len(word):
            return "Not present"
​
        len_a6 = [len(x) for x in a6]
        a6_l = len_a6[1:-1]
        if len(a6[0])>1:
            res = [x[0] for x in a6[0]]
            min_inx = res.index(min(res))
            a_inter = a6[0][min_inx]
            a6[0] = [a_inter]
​
        if len(a6[-1])>1:
            res = [x[0] for x in a6[-1]]
            min_inx = res.index(min(res))
            a_inter = a6[-1][min_inx]
            a6[-1] = [a_inter]
​
        time_i +=1
        if time_i>100:
           for index, sub_a6 in enumerate(a6):
               if len(sub_a6) > 1:
                   for j in sub_a6:
                       if [j] in a6:
                           a6[index].remove(j)
​
           break
​
        if sum(a6_l) <= len(a6_l):
            break
        else:
            a_input = a6
    a_output = [x[0] for x in a6]
    return a_output

