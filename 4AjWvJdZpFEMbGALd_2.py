"""


A group of `n` prisoners stand in a circle awaiting execution. Starting from
an arbitrary position(0), the executioner kills every `k`th person until one
person remains standing, who is then granted freedom (see examples).

Create a function that takes 2 arguments — the number of people to be executed
`n`, and the step size `k`, and returns the original position (index) of the
person who survives.

### Examples

    who_goes_free(9, 2) ➞ 2
    
    # Prisoners = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # Executed people replaced by - (a dash) for illustration purposes.
    # 1st round of execution = [0, -, 2, -, 4, -, 6, -, 8]  -> [0, 2, 4, 6, 8]
    # 2nd round = [-, 2, -, 6, -] -> [2, 6]  # 0 is killed in this round because it's beside 8 who was skipped over.
    # 3rd round = [2, -]
    
    who_goes_free(9, 3) ➞ 0
    
    # [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # [0, 1, -, 3, 4, -, 6, 7, -] -> [0, 1, 3, 4, 6, 7]
    # [0, 1, -, 4, 6, -] -> [0, 1, 4, 6]
    # [0, 1, -, 6] -> [0, 1, 6]
    # [0, -, 6] -> [0, 6]
    # [0, -] -> [0]

### Notes

Refer to **Resources** tab for more info.

"""

def who_goes_free(n, k):
    t = range(0, n)
    t2 = h(t, k)
    return t2[0]
​
​
def h(lis, k):
    if len(lis) == 1:
        return lis
​
​
    if len(lis) < k:
        lis2 = lis.copy()
        lis3 = []
​
        if k % len(lis) == 0:
            del lis2[-1]
​
        else:
            lis3 = lis3 + lis2[k % len(lis):]
            del lis2[k%len(lis) -1:]
        lis3=lis3+lis2
        return h(lis3,k)
​
​
    lis2 = [lis[x] for x in range(len(lis)) if (x + 1) % k != 0]
    l = len(lis) - (len(lis) // k) * k
    lis3 = []
    lis3 = lis3 + lis2[len(lis2) - l:]
    del lis2[len(lis2) - l:]
    lis3 = lis3 + lis2
    return h(lis3, k)
print(who_goes_free(15, 4))

