"""


In a letter to Lord Bowden in 1837, Charles Babbage asked, "What is the
smallest positive integer whose square ends in 269,696?". He thought the
answer was 99,736 whose square is 9,947,269,696. Was he right?

Write a function that takes a positive integer `n` and returns the smallest
number whose square ends with `n`. One small twist, if `n == 269696` return
`"Babbage was correct!"` if the smallest number whose square ends with 269,696
is 99,736, otherwise return `"Babbage was incorrect!"`.

### Examples

    babbage(25) ➞ 5
    
    babbage(161) ➞ 119
    # 119 * 119 == 14,161
    # Ends with 161
    
    babbage(269696) ➞ "Babbage was {?}!"
    # Replace {?} with the word "correct" or "incorrect".

### Notes

  * `n` will always be a positive integer `n > 0`.
  * Make sure your solution is efficient enough to pass the tests within a 12 second time limit.

"""

def babbage(n):
    i, len_n = int(pow(n, 0.5)), len(str(n))
    divisor = pow(10, len_n)
    while pow(i, 2) % divisor != n:
        i += 1
    return ('Babbage was {}correct!'.format(('in', '')[i == 99736])
            if n == 269696 else i)

