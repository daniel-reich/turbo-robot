"""


Given a list of coins, father needs to distribute them amongst his three
children. Write a function to determine if the coins can be distributed
equally or not. Return `True` if each son receives the same amount of money,
otherwise return `False`.

    [1, 2, 3, 2, 2, 2, 3] ➞ True

  * Amount to be distributed to each child = `(1+2+3+2+4+3)/3 => 15/3 => 5`
  * Possible set of coin to be distributed to children = `[(1,2,2),(2,3),(2,3)]`

    [5, 3, 10, 1, 2] ➞ False

  * Amount to be distributed to each child = `(5+3+10+1+2)/3 => 21/3 => 7`
  * But there are no combination such that each child get equal value which is 7.

### Examples

    coins_div([1, 2, 3, 2, 2, 2, 3]) ➞ True
    
    coins_div([5, 3, 10, 1, 2]) ➞ False
    
    coins_div([2, 4, 3, 2, 4, 9, 7, 8, 6, 9]) ➞ True

### Notes

  * Inputs will be an array of positive integers only.
  * Coin can be any positive value.

"""

def find_split(a, split_into):
    if split_into == 1:
        return a
    if sum(a) % split_into != 0:
        return None
    check_val = sum(a) // split_into
    def check_func(path):
        return sum([a[i] for i in path]) == check_val
    q = [(0,(0,))]
    while q:
        # take from queue and check
        v = q.pop(0)
        if check_func(v[1]):
            # recursion
            a_new = [a[i] for i in range(len(a)) if i not in v[1]]
            next_split = find_split(a_new, split_into-1)
            if next_split:
                # return on recursion success
                curr_part = [a[i] for i in v[1]]
                return [curr_part] + [next_split]
        # append to queue 
        for w in range(v[0]+1, len(a)):
            q.append((w, v[1] + (w,)))
    return None
​
​
def coins_div(a):
    return find_split(a, 3) is not None

