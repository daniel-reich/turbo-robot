"""


A numeric string `s` is beautiful if it can be split into a sequence of two or
more positive integers, `a[1]`, `a[2]`, `...a[n]`, satisfying the following
conditions:

  1. `a[i] - a[i-1] = 1` for any `1 < i <= n` (i.e. each element in the sequence is one more than the previous element).
  2. No `a[i]` contains a leading zero. For example, we can split `s = 10203` into the sequence `{1, 02, 03}`, but it is not beautiful because `02` and `03` have leading zeroes.
  3. The contents of the sequence cannot be rearranged. For example, we can split `s = 312` into the sequence `{3, 1, 2}`, but it is not beautiful because it breaks our first constraint (i.e. `1 - 3 ≠ 1`).

Return either `"YES x"` where `x` is the smallest first number of the
increasing sequence or `"NO"` if there is no valid sequence.

### Examples

    separate_numbers("1234") ➞ "YES 1"
    
    separate_numbers("91011") ➞ "YES 9"
    
    separate_numbers("99100") ➞ "YES 99"
    
    separate_numbers("101103") ➞ "NO"
    
    separate_numbers("010203") ➞ "NO"

### Notes

N/A

"""

def separate_numbers(s):
    len_num = 1
    len_s = len(s)
    while len_num <= len_s // 2:
        s_tmp = s[:]
        start_num = s_tmp[:len_num]
        s_tmp = s_tmp[len_num:]
        next_num = int(start_num) + 1
        while s_tmp:
            str_next = str(next_num)
            if s_tmp.startswith(str_next):
                s_tmp = s_tmp[len(str_next):]
                next_num = int(str_next) + 1
            else:
                break
        if not s_tmp:
            return "YES {}".format(start_num)
        len_num += 1
    return "NO"

