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

def secret_word(s, l):
    vals = [sum(ord(c) for c in s[i-1:i+2]) for i in range(1, len(s)-1)]
    for i, v in enumerate(vals):
        for w in vals[i+1:]:
            cat = subseq(vals, [v+(w-v)*k for k in range(l)])
            if cat is not None:
                return ''.join(s[c+1] for c in cat)
​
def subseq(s1, s2):
    if not s2:
        return []
    if s2[0] in s1:
        i = s1.index(s2[0])
        meh = subseq(s1[i+1:], s2[1:])
        if meh is not None:
            return [i] + [m+i+1 for m in meh]

