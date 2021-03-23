"""


In this challenge, you have to verify if a number is exactly divisible by a
combination of its digits. There are three possible conditions to test:

  * The given number is exactly divisible by **each of its digits excluding the zeros**.
  * The given number is exactly divisible by the **sum of its digits**.
  * The given number is exactly divisible by the **product of its digits**.

Given an integer `n`, implement a function that returns:

  * If every test is true, a string `"Perfect"`.
  * If some test is true, the number of true tests (`1` or `2`).
  * If every test is false, a string `"Indivisible"`.

### Examples

    digital_division(21) ➞ 1
    # Exactly divisible only by the sum of its digits (2 + 1 = 3).
    
    digital_division(128) ➞ 2
    # Exactly divisible by each of its digits.
    # Exactly divisible by the product of its digits (1 * 2 * 8 = 16).
    
    digital_division(100) ➞ 2
    # Exactly divisible by each of its digits (excluding zeros).
    # Exactly divisible by the sum of its digits (1 + 0 + 0 = 1).
    
    digital_division(12) ➞ "Perfect"
    # Exactly divisible by each of its digits.
    # Exactly divisible by 3 (sum of digits = 1 + 2).
    # Exactly divisible by 2 (product of digits = 1 * 2).
    
    digital_division(31) ➞ "Indivisible"
    # Every testing condition is false.

### Notes

  * Remember to exclude any 0-digit when testing if the given `n` is divisible by each of its digits (see example #3).
  * A number containing at least a 0-digit can't be exactly divided by the product of its digits (division by 0).
  * Trivially, every single-digit positive number greater than 0 is Perfect
  * Any given number will be a positive integer greater than 0.

"""

def digital_division(n):
    vals_to_consider=([int(val) for val in str(n)])
    ti=0
    while ti==0:
        try:
            vals_to_consider.remove(0)
        except:
            ti=1
    check_1=0
    tests=0
    t3_val=1
    for vvals in vals_to_consider:
    #test 1 - Exactly divisble be each of its digits excluding 0
        if n%vvals == 0:
            check_1=check_1+1
            
        if check_1 == len(vals_to_consider):
            tests=tests+1
    
​
    #test 2 exactly divisible by sum of digits
    if n%sum(vals_to_consider)  == 0:
        tests=tests+1
    #test3 exactly divisible by product on digits
    for vvals in [int(val) for val in str(n)]:    
        t3_val=t3_val*vvals
    try:
        n%t3_val==0
        if n%t3_val==0:
            tests=tests+1
    except:
        tests=tests
    if tests == 3:
        return("Perfect")
    elif tests > 0:
        return(tests)
    else:
         return("Indivisible")

