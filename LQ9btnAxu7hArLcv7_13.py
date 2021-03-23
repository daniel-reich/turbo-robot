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

def diagonalize(n,d):
    array = []
    total = 0
    for i in range(n):
        array.append([])
        for j in range(n):
            array[i].append(0)
    if d == 'ul':
        for k in range(n):
            for h in range(n):
                array[k][h] = h + k
    elif d == 'ur':
        for k in range(n):
            for h in range(n):
                array[k][n-h-1] = h + k
    elif d == 'll':
        for k in range(n):
            for h in range(n):
                array[n-k-1][h] = h + k
    else:
        for k in range(n):
                for h in range(n):
                    array[n-k-1][n-h-1] = h + k
    return array

