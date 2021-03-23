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

def secret_word(s, length):
    v, comp, le = [], [], len(s) - 2
    for i in enumerate(range(le)):
        v.append([sum(map(ord, s[i[0]:i[0]+3])) - 288, i[0]])
    for start in range (le-length+1):
        p = [v[start]]
        for sec in range(start+1, le-length+2):
            po, d = p + [v[sec]], v[sec][0]-p[-1][0]
            for r in range(sec+1, le):
                po += [v[r]] if v[r][0]-po[-1][0] == d else []
            if len(po) >= length:
                return "".join([s[i[1]+1] for i in po[:length]])

