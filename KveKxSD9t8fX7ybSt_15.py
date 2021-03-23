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
    count = sum(map(lambda x : x == 1, lst))
    if lst == []:
       return [0, []] 
    else:
        a = []
        count_down_list = []
        for i in range(len(lst)):
            if lst[i] == 1:
                a.append(i)
        for i in range(len(a)):
            if i == 0:
                j = a[i]
                b = [1]
                yes = True
                while (j > -1) & (yes ==True):
                    if lst[j-1] == lst[j] + 1:
                        b.append(lst[j-1])
                        yes = True
                    else:
                        yes = False
                    j -= 1
                b.reverse()
                count_down_list.append(b)
            elif (i>0) & (a[i]-a[i-1]==1):
                count_down_list.append([1])
            else:
                j = a[i]
                b = [1]
                yes =True
                while (j > a[i-1]) & (yes== True):
                    if lst[j-1] == lst[j] + 1:
                        b.append(lst[j-1])
                        yes = True
                    else:
                        yes = False
                    j -= 1
                b.reverse()
                count_down_list.append(b)
        return [count, count_down_list]

