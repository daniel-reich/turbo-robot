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

def secret_word(string, length):
    triplets = [(ord(t[0]) + ord(t[1]) + ord(t[2]) - 3 * ord('a'), t[1]) for t in zip(string, string[1:], string[2:])]
    for ix, tri in enumerate(triplets):
        for j in range(ix+1, len(triplets)):
            secret = tri[1]
            if triplets[j][0] > triplets[ix][0]:
                d, prev = triplets[j][0] - triplets[ix][0], triplets[j][0]
                secret += triplets[j][1]
                for k in range(j+1, len(triplets)):
                    if triplets[k][0] - prev == d:
                        secret += triplets[k][1]
                        prev = triplets[k][0]
            if len(secret) == length:
                return secret
    return None

