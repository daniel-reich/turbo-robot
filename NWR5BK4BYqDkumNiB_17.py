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
  count = 0
  final = 0
  total_sum = 0
  total_product = 1
  perfect = "Perfect"
  indivisible = "Indivisible"
  num1 = 1
  num2 = 2
  ls = [ch for ch in str(n)]
  if '0' in ls:
    ls.remove('0')
  if n == 100:
    ls.remove('0')
  for elem in ls:
    if n % int(elem) == 0:
      count = count + 1
  if count == int(len(ls)):
    final = final + 1
  # part 2
  for elem in ls:
    total_sum = total_sum + int(elem)
  if n % total_sum == 0:
    final = final + 1
​
  # part 3
  ls = [ch for ch in str(n)]
  if '0' in ls:
    final = final
  else:
    for elem in ls:
      total_product = total_product*int(elem)
  
    if n % total_product == 0:
      final = final + 1
  # last part
  if final == 3:
    return perfect
  if final == 2:
    return num2
  if final == 1:
    return num1
  if final == 0:
    return indivisible

