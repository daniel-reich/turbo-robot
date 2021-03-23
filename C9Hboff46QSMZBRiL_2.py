"""


Given a set `S` of allowed letters, an S-string is a string written using only
those letters. For example, if `S={"d","g"}` then `"dgggdgdggd"` is an
S-string but `"dag"` is not.

For a fixed set `S` and max string size `M` (chosen so that we need only deal
with finitely many strings) one can order those strings according to their
dictionary/lexicographic order.

For example, if `S={"d","g"}` and `M=3`, one obtains the strings:

    "d","g","dd","dg","gd","gg","ddd","ddg","dgd","dgg","gdd","gdg","ggd","ggg"

...which, once reordered in lexicographic order, become:

    "d","dd","ddd","ddg","dg","dgd","dgg","g","gd","gdd","gdg","gg","ggd","ggg"

### Goal

Write a function that when given:

  * a set `S` of allowed letters;
  * a max string size `M`;
  * a position `k`;

... returns **the k-th S-string of max size M according to lexicographic
order**.

### Examples

    kth_string({"d", "g"}, 3, 2) ➞ "dd"
    # According to the above, the 2-nd string in lexicographic order is "dd".
    
    kth_string({"d", "g"}, 3, 10) ➞ "gdd"
    # According to the above, the 10-th string in lexicographic order is "gdd".
    
    kth_string({"a", "e", "i"}, 2, 6) ➞ "ea"
    # The relevant strings, in lexicographic order, are:
    # "a", "aa", "ae", "ai", "e", "ea", ee", "ei", "i", "ia", "ie", "ii"
    # The 6-th string is "ea".

### Notes

  * Since each test considers only finitely many strings, the challenge is valid only for small enough `k` (e.g. in the `S={"d", "h"}`, `M=3` case above there are only `14` strings, so the challenge only works for `1<=k<=14`). You are free to assume that all tests are valid.
  * The empty string `""` is not considered a valid string for the purposes of this challenge. However, you may find it helpful to regard the empty string `""` as the 0-th string in lexicographic order (this can help with the algebra of the challenge).
  * I believe that a brute force approach, such as generating all possible strings and then sorting them, is too slow and will not pass all the tests within the 12s time limit. However, more efficient solutions have ample time: for example, my posted solution runs in a fraction of a millisecond.

"""

def kth_string(S, M, k):
    lS, l, last, jp, s = len(S), sorted(S), 1, [1], ""
    for i in range(M-1):
        last = last*lS + 1
        jp.append(last)
    for j in jp[::-1]:
        if k:
            k -= 1
            p = k//j
            s += l[p]
            k -= p*j
        else:
            return s
    return s

