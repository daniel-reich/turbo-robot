"""


Write a function that diagonally orders numbers in a `n x n` matrix, depending
on which of the four corners you originate from: upper-left (`ul`), upper-
right (`ur`), lower-left (`ll`), lower-right (`lr`).

### Examples

    diagonalize(3, "ul") ➞ [
      [0, 1, 2],
      [1, 2, 3],
      [2, 3, 4]
    ]
    
    diagonalize(4, "ur") ➞ [
      [3, 2, 1, 0],
      [4, 3, 2, 1],
      [5, 4, 3, 2],
      [6, 5, 4, 3]
    ]
    
    diagonalize(3, "ll") ➞ [
      [2, 3, 4],
      [1, 2, 3],
      [0, 1, 2]
    ]
    
    diagonalize(5, "lr") ➞ [
      [8, 7, 6, 5, 4],
      [7, 6, 5, 4, 3],
      [6, 5, 4, 3, 2],
      [5, 4, 3, 2, 1],
      [4, 3, 2, 1, 0]
    ]

### Notes

N/A

"""

def increment_arr(lst):
    for i,a in enumerate(lst):
        if i == 0:
            continue
        for j,b in enumerate(a): 
            lst[i][j] = lst[i-1][j] + 1
    return lst
            
    
def diagonalize(n:int,s:str):
    mat = []
    mat = [[0 for m in range(n)]for i in range(n)]
    mat[0] = [i for i in range(len(mat[0]))]       
    mat = increment_arr(mat)
    if s == 'ul':
        return mat
    if s == 'll':
        mat = mat[::-1]
        return mat
    if s == 'ur':
        g = [i[::-1] for i in mat]
        return g
    if s == 'lr':
        g = [i[::-1] for i in mat]
        g = g[::-1]
        return g
        
    return mat

