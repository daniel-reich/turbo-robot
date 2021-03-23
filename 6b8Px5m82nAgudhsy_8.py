"""


Write a function that returns the next number that can be created from the
same digits as the input.

### Examples

    next_number(19) ➞ 91
    
    next_number(3542) ➞ 4235
    
    next_number(5432) ➞ 5432
    
    next_number(58943) ➞ 59348

### Notes

  * If no larger number can be formed, return the number itself.
  *  **Bonus** : See if you can do this without generating all digit permutations.

"""

def next_number(num):
    s, results = list(str(num))[::-1], []
    for a,b in enumerate(s):
        for c, d in enumerate(s):
            if b > d:
                s[a], s[c] = s[c], s[a]
                temp = sorted([int(e) for e in s[:c]], reverse=True)
                s[:c] = [str(e) for e in temp]
                if int("".join(s[::-1])) > num:
                    results.append(int("".join(s[::-1])))
                s = list(str(num))[::-1]
    results.sort()
    if len(results)> 0: return results[0]
    else: return num

