"""


In this challenge you must create a program which takes a number `n` and
returns the length or number of digits in all numbers from 1 to `n`
concatenated.

### Examples

    concatenation_sum(5) ➞ 5
    
    concatenation_sum(10) ➞ 11
    
    concatenation_sum(13) ➞ 17

### Notes

Keep in mind that the output is the number of digits in the concatenated
number. For example, if the input was `5`, the output would be `5` because
`12345` has `5` digits. Similarly when the input is `13` the ouput is `17`
because `12345678910111213` has `17` digits.

"""

def concatenation_sum(n):
    if len(str(n)) == 1:
        return n
    else:
        return (n - 10 ** (len(str(n)) - 1) + 1) * (len(str(n))) + concatenation_sum(10 ** (len(str(n)) - 1) -1)

