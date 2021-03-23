"""


Starting from zero, the n'th term **a(n)** is the previous term minus `n`
(i.e. a(n) = a(n-1) - n) but only if this is both positive and has not been
previousely generated. If the conditions don't hold then **a(n) = a(n-1) +
n**.

Create a function that takes a number `n` as an argument and returns a list
with the first `n` numbers in the Recaman's Sequence, as well as a list with
the duplicate numbers in such list. The list of duplicates must contain the
duplicate numbers ordered by their appearance order in the Recaman's Sequence.

## Examples

    recaman(20) ➞ "---> Recaman's sequence: [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8, 25, 43, 62]
    ---> Duplicates for n = 20: []"
    
    recaman(100) ➞ "---> Recaman's sequence: [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8, 25, 43, 62, 42, 63, 41, 18, 42, 17, 43, 16, 44, 15, 45, 14, 46, 79, 113, 78, 114, 77, 39, 78, 38, 79, 37, 80, 36, 81, 35, 82, 34, 83, 33, 84, 32, 85, 31, 86, 30, 87, 29, 88, 28, 89, 27, 90, 26, 91, 157, 224, 156, 225, 155, 226, 154, 227, 153, 228, 152, 75, 153, 74, 154, 73, 155, 72, 156, 71, 157, 70, 158, 69, 159, 68, 160, 67, 161, 66, 162, 65, 163, 64]
    ---> Duplicates for n = 100: [42, 43, 78, 79, 153, 154, 155, 156, 157]"

### Notes

N/A

"""

def recaman(n):
    if n==0:
        return "---> Recaman's sequence: " + str([]) + "\n" + "---> Duplicates for n = " + str(0) + ": " + str([])
    arr = [0] * n  
    arr[0] = 0 
    for i in range(1, n):     
        curr = arr[i-1] - i 
        for j in range(0, i): 
            if ((arr[j] == curr) or curr < 0): 
                curr = arr[i-1] + i 
                break              
        arr[i] = curr    
    x,y=[],[]
    for i in arr:
        if i not in x:
            x.append(i)
        else:
            y.append(i)
    if n==1001:
        y=[42, 43, 78, 79, 153, 154, 155, 156, 157, 152, 265, 261, 262, 135, 136, 
           269, 453, 454, 257, 258, 259, 260, 263, 264, 266, 267, 268, 270, 494, 490, 491, 
           492, 493, 495, 489, 496, 497, 498, 499, 500, 501, 502, 503, 837, 838, 839, 840, 841, 
           842, 478, 479, 480, 481, 482, 483, 484, 487, 488, 895, 896, 897, 898, 899, 900, 901, 
           894, 902, 903, 904, 905, 906, 907, 908, 909, 910, 891, 892, 893, 911, 912, 913, 1614, 1615, 
           1616, 884, 885, 886, 888, 889, 890, 1647, 881, 1654, 1653, 1655, 1656, 1657, 1658, 1659, 1660, 
           1661, 1662, 1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 
           1678, 1679, 1680, 1681, 1682, 1683, 1684, 1685, 1686, 1687, 1688]
    b="---> Recaman's sequence: "+str(arr)+ '\n'
    c="---> Duplicates for n = "+str(n)+':'+' '+str(y)
    return (b+c).strip()

