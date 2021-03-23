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
  p = list(range(n))
  x = k-1
  while len(p)>1:
    del p[x]
    x += k-1
    while x >= len(p):
      x = x-len(p)
  return p[0]

