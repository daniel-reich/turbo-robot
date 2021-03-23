"""


The number 6174 is a really mysterious number. At first glance, it might not
seem so obvious. But as we are about to see, anyone who can subtract can
uncover the mystery that makes 6174 so special.

In 1949 the mathematician D. R. Kaprekar devised a process now known as
Kaprekar's operation. First choose a four digit number where the digits are
not all the same (that is not 1111, 2222, and so on). Then rearrange the
digits to get the largest and smallest numbers these digits can make. Finally,
subtract the smallest number from the largest to get a new number, and carry
on repeating the operation for each new number.

It is a simple operation, but Kaprekar discovered it led to a surprising
result: When we reach 6174 the operation repeats itself, returning 6174 every
time. In fact, you reach 6174 for all four digit numbers that don't have all
the digits the same. It's marvellous. Kaprekar's operation is so simple but
uncovers such an interesting result.

### Objective

Create a function that takes a four digit number as an argument and returns
the numbers of iterations needed to reach the number 6174, as well as a print
of each iteration. If the number is a repdigit, the function must return a
message to the user.

### Important

  * If in any iteration you have a 1-digit, 2-digits or 3-digits number, add leading zeros for the calculations and the prints. Please see example below where n = 1.
  * Based on the point mentioned before, you can expect, for example, that the numbers 1 and 1000 will lead to the same iterations.

### Examples

    Kaprekar(1234) ➞
    "---------- The Mysterious Number 6174 ----------
    
    Number of iterations: 3
    
    Iterations:
    
    Iteration Nr. 1: 4321 - 1234 = 3087
    Iteration Nr. 2: 8730 - 0378 = 8352
    Iteration Nr. 3: 8532 - 2358 = 6174
    
    ------------------------------------------------"
    Kaprekar(2005) ➞
    "---------- The Mysterious Number 6174 ----------
    
    Number of iterations: 7
    
    Iterations:
    
    Iteration Nr. 1: 5200 - 0025 = 5175
    Iteration Nr. 2: 7551 - 1557 = 5994
    Iteration Nr. 3: 9954 - 4599 = 5355
    Iteration Nr. 4: 5553 - 3555 = 1998
    Iteration Nr. 5: 9981 - 1899 = 8082
    Iteration Nr. 6: 8820 - 0288 = 8532
    Iteration Nr. 7: 8532 - 2358 = 6174
    
    ------------------------------------------------"
    Kaprekar(8888) ➞
    "---------- The Mysterious Number 6174 ----------
    
    Error, n cannot be a repdigit.
    
    ------------------------------------------------"
    Kaprekar(1) ➞
    "---------- The Mysterious Number 6174 ----------
    
    Number of iterations: 5
    
    Iterations:
    
    Iteration Nr. 1: 1000 - 0001 = 0999
    Iteration Nr. 2: 9990 - 0999 = 8991
    Iteration Nr. 3: 9981 - 1899 = 8082
    Iteration Nr. 4: 8820 - 0288 = 8532
    Iteration Nr. 5: 8532 - 2358 = 6174
    
    ------------------------------------------------"

### Notes

N/A

"""

def Kaprekar(n):
    str_n = str(n)
    first_line = '\n---------- The Mysterious Number 6174 ----------\n'
    last_line = '\n------------------------------------------------'
    if len(str_n) > 1 and len(set(str_n)) == 1:
        middle_line = '\nError, n cannot be a repdigit.\n'
    else:
        lst_triple = []
        while n != 6174:
            lst_n = list('{:0>4}'.format(str(n)))
            large_n = int(''.join(sorted(lst_n, reverse=True)))
            small_n = int(''.join(sorted(lst_n)))
            n = large_n - small_n
            lst_triple.append((large_n, '{:0>4}'.format(str(small_n)),
                               '{:0>4}'.format(str(n))))
        middle_line = '\nNumber of iterations: {}\n'.format(len(lst_triple))
        middle_line += '\nIterations:\n\n'
        for idx, tpl in enumerate(lst_triple):
            middle_line += 'Iteration Nr. {}: {} - {} = {}\n'.format(idx + 1,
                                                                     *tpl)
    return first_line + middle_line + last_line

