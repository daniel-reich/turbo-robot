"""


Create a function that counts how many n-digit numbers have the same sum of
the first half and second half of the digits (“lucky” numbers). The number `n`
is **even**. For example, for `n = 6`, the numbers "001010", "112220",
"000000" are lucky.

### Examples

    lucky_ticket(2) ➞ 10
    
    lucky_ticket(4) ➞ 670
    
    lucky_ticket(12) ➞ 39581170420

### Notes

  * The function should be really efficient.
  * The runtime increases 10 fold per test. Just for information: my solution takes 6 seconds, which is still under the server time-limit, so you are good to go.

"""

def lucky_ticket(n_digits):
    if n_digits == 2:
        return 10
​
    half = n_digits // 2
    max_sum = 9 * half
    sums = dict()
    for s in range(max_sum + 1):
        sums[s] = 0
​
    str_tpl = ''
    str_loop = ''
    for i in range(half):
        str_tpl += 'd{}, '.format(i)
        str_loop += ' for d{} in range(10)'.format(i)
    eval_expr = '(({}){})'.format(str_tpl[:-2], str_loop)
​
    gen = eval(eval_expr)
    for tpl in gen:
        sums[sum(tpl)] += 1
​
    return sum(val * val for val in sums.values())

