"""


Create a function that takes an array of strings of arbitrary dimensionality
(`[]`, `[][]`, `[][][]`, etc) and returns the deep_sum of every separate
number in each string in the array.

### Examples

    deep_sum(["1",  "five",  "2wenty",  "thr33"]) ➞ 36
    
    deep_sum([["1X2",  "t3n"], ["1024", "5", "64"]]) ➞ 1099
    
    deep_sum([[["1"], "10v3"],  ["738h"],  [["s0"],  ["1mu4ch3"], "-1s0"]]) ➞ 759

### Notes

  * Numbers in strings can be negative, but will all be base-10 integers.
  * Negative numbers may directly follow another number.
  * The hyphen or minus character ("-") does not only occur in numbers.
  * Arrays may be ragged or empty.

"""

def extract_num(el):
    ans = 0
    s = ''.join([c if c == '-' or '0' <= c <= '9' else ' ' for c in el]).replace('-', ' -')
    for k in s.split():
        if len(k) > 0 and k.strip() != '-':
            ans += int(k)
    return ans
    
def dfs(L, ans):
    if len(L) == 0:
        return ans
    for el in L:
        if type(el) == list:
            ans = dfs(el, ans)
        else:
            ans += extract_num(el)
    return ans
​
def deep_sum(lst):
    return dfs(lst, 0)

