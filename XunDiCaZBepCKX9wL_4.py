"""


This string, `"sadbpstcrdvaefikkgoenqrt"` has a five letter word embedded
within it.

Here's a clue on how to find it:

  1. The `string` can be broken up from left to right into a series of overlapping letter triplets.
  2. The letter values for each triplet are summed with a=1, b=2, ..., z=26.
  3. The values of the triplets that contain the letters of the secret word as the middle member form an increasing arithmetic series.

Given the `string` and `length` of the secret word, improvise a function that
finds the secret word.

### Examples

    secret_word("sadbpstcrdvaefikkgoenqrt", 5) ➞ "brake"
    # sa(dbp)st(crd)(vae)f(ikk)g(oen)qrt
    # The values of the triplets in parentheses are 22, 25, 28, 31, 34.
    # An arithmetic series with difference of 3.
    
    secret_word("aheiayd", 3) ➞ "hey"
    # (a[he)i](ayd)
    # The triplets with the secret letters can overlap.
    # ahe=14, hei=22, ayd=30; a series with a difference of 8.

### Notes

N/A

"""

from itertools import combinations
def secret_word(s, lng):
    sums = [ord(s[i - 1]) + ord(s[i]) + ord(s[i + 1]) - 288
            for i in range(1, len(s) - 1)]
    if lng > 10:
        unique = sorted(set(sums))
        for start in range(len(unique) - lng):
            du = unique[start + 1] - unique[start]
            if all(unique[start + n] - unique[start + n - 1] == du
                   for n in range(2, lng + 1)):
                seq = unique[start:start + lng]
                break
        w_idx = [sums.index(seq[0])]
        for m in range(1, lng):
            w_idx.append(w_idx[-1] + sums[w_idx[-1]:].index(seq[m]))
        return ''.join(s[j + 1] for j in w_idx)
    else:
        for comb in combinations(range(len(sums)), lng):
            diff = sums[comb[1]] - sums[comb[0]]
            if (diff > 0 and all((sums[comb[k]] - sums[comb[k - 1]]) == diff
                                 for k in range(2, lng))):
                return ''.join(s[j + 1] for j in comb)

