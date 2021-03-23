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

def find_series(triplets, length, diff):
    for start in range(len(triplets) - length + 1):
        series = [start]
        value = triplets[start]
        cur = start + 1
        for k in range(length - 1):
            value += diff
            while cur < len(triplets) and triplets[cur] != value:
                cur += 1
            if cur == len(triplets):
                break
            series.append(cur)
        if len(series) == length:
            return series
    return []
​
def secret_word(string, length):
    triplet = ord(string[0]) - 96 + ord(string[1]) - 96 + ord(string[2]) - 96
    triplets = [triplet]
    for i in range(3, len(string)):
        triplet = triplet - (ord(string[i - 3]) - 96) + (ord(string[i]) - 96)
        triplets.append(triplet)
    for diff in range(1, 25):
        series = find_series(triplets, length, diff)
        if len(series) > 0:
            ans = ''.join([string[s+1] for s in series])
            return ans

