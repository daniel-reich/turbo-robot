"""


Declare a `division()` function that gets two natural numbers (`a`, `b`) and
return a string containing the rational number `a` / `b` in the form of a
decimal fraction, possibly **periodic**.

### Examples

    division(2, 5) ➞ "0.4"
    
    division(1, 6) ➞ "0.1(6)"
    
    division(1, 3) ➞ "0.(3)"
    
    division(1, 7) ➞ "0.(142857)"
    
    division(1, 77) ➞ "0.(012987)"

### Notes

  * The length of a periodic fraction can be more than **20 numbers**.
  * The function should be efficient.

"""

def convert(numerator, denominator):
    if numerator == 0: return "0."
    if numerator == denominator: return "1."
    v = numerator // denominator
    numerator = 10 * (numerator - v * denominator)
    answer = str(v)
    answer += '.'
    states = {}
    while numerator > 0:
       prev_state = states.get(numerator, None)
       if prev_state != None:
            start_repeat_index = prev_state
            non_repeating = answer[:start_repeat_index]
            repeating = answer[start_repeat_index:]
            return non_repeating + '(' + repeating + ')'
       states[numerator] = len(answer)
       v = numerator // denominator
       answer += str(v)
       numerator -= v * denominator
       numerator *= 10
    return answer
​
def division(a, b):
    ans = convert(a, b)
    if ans[-1] == '.':
        ans += '0'
    return ans

