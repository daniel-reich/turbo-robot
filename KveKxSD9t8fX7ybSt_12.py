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

def final_countdown(lst):
    seq='987654321'
    k=0;ans=[]
    s=''.join([str(i) for i in lst])
    sc=''
    while len(s)>1 and sc!=s:
        sc=s[:]
        fl=0
        for a in range(len(s)):
            for b in range(len(s),a,-1):
                if s[a:b] in seq and s[a:b] not in '23456789' and s[a:b][-1]=='1':
                    fl=1
                    k+=1
                    ans.append([int(i) for i in s[a:b]])
                    s=s[:a]+s[b:]
                    if s=='1':
                        k+=1
                        ans.append([1])
                    break
            if fl==1:break
    return [k,ans]

