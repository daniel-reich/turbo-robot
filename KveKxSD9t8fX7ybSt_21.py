"""


A countdown sequence is a descending sequence of `k` integers from `k` down to
1 (e.g. 5, 4, 3, 2, 1). Write a function that returns a list `[x, y]` where
**x** is the number that represents how many of countdown sequences are in a
given list and **y** is a list of those sequences in order which they appear
in the list.

### Examples

    final_countdown([4, 8, 3, 2, 1, 2]) ➞ [1, [[3, 2, 1]]]
    # In this example we have 1 countdown sequence: 3, 2, 1
    
    final_countdown([4, 4, 5, 4, 3, 2, 1, 8, 3, 2, 1]) ➞ [2, [[5, 4, 3, 2, 1], [3, 2, 1]]]
    # We have 2 countdown sequences:
    # 5, 4, 3, 2, 1 and 3, 2, 1
    
    final_countdown([4, 3, 2, 1, 3, 2, 1, 1]) ➞ [3, [[4, 3, 2, 1], [3, 2, 1], [1]]]
    # We have 3 countdown sequences:
    # 4, 3, 2, 1 ; 3, 2, 1 and 1
    
    final_countdown([1, 1, 2, 1]) ➞ [3, [[1], [1], [2, 1]]]
    
    final_countdown([]) ➞  [0, []]

### Notes

  * `[1]` is a valid countdown sequence.
  * All numbers will be greater than 0.

"""

def count_sub(L, s, H,A):
    if 1 in L:
        G = []
        x = L.index(1)
        G.append(1)
        for i in range(1, x + 1, 1):
            if L[x - i] == L[x] + i:
                G.append(L[x - i])
            else:
                break
        s += 1
​
        G.reverse()
        H.append(G)
        count_sub(L[x + 1:],s,H,A)
    else:
        if A==[]:
            A.append(s)
            A.append(H)
​
def final_countdown(L):
    A=[]
    H=[]
    s=0
    count_sub(L,s,H,A)
    return(A)

