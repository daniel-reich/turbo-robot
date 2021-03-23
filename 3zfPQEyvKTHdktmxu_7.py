"""


For a given list, determine the biggest possible sum between consecutive
terms, as well as the initial and final position of the terms.

### Examples

    big_sub([4, -3, 5, -7, 5]) ➞ [6 (sum), 0 (start), 2 (end)]
    
    big_sub([4, -3, -5, 7, 5]) ➞ [12, 3, 4]
    
    big_sub([2, -3, 2, -3, 2]) ➞ [2, 4, 4]

### Notes

  * If the biggest sum is repeated at several intervals, return the starting and ending positions of the latest interval.
  * The list will always have positive numbers.

"""

def blocos(lst):
    i, j, positivos, negativos = 0, 0, [], []
    soma, sub = False, False
    for termo in range(len(lst)):
        if lst[termo] > 0:
            if not soma:
                if sub: negativos[j-1][2] = termo-1
                soma, sub, pis = True, False, termo
                positivos.append([0, pis, 0]); i += 1
            positivos[i-1][0] = positivos[i-1][0]+lst[termo]
        else:
            if not sub:
                if soma: positivos[i-1][2] = termo-1
                soma, sub, pjt = False, True, termo
                negativos.append([0, pjt, 0]); j += 1
            negativos[j-1][0] = negativos[j-1][0] + lst[termo]
        if soma: positivos[i-1][2] = termo
        else: negativos[j - 1][2] = termo
    return positivos, negativos
​
​
def big_sub(lst):
    c, pulos = [i for i in range(len(lst))], [0 for _ in range(len(lst))]
    r = 0 if lst[0] > 0 else 1; p, n = blocos(lst); maximo, p_at = p[0][0], 0
    for s in range(1, len(p)):
        reducao = 0
        for d in range(s-1, p_at-1, -1):
            c[d] = c[d+1] - 1 - pulos[d+1]
            if p[s][0]+p[c[d]][0]+n[c[d]+r][0]+reducao > max(p[s][0], p[c[d]][0]):
                p[s] = [p[s][0]+p[c[d]][0]+n[c[d]+r][0]+reducao, p[c[d]][1], p[s][2]]
                reducao, pulos[s] = 0, s-d
            else: reducao = reducao+p[c[d]][0]+n[c[d]+r][0]
            if d == p_at: break
        if p[s][0] >= maximo: p_at, maximo = s, p[s][0]
    return p[p_at]

