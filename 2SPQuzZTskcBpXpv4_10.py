"""


Welcome to part two of the collection for _Computer Science Algorithms_. This
challenge will deal further with writing recursive functions by covering the
Euclidean Algorithm. The "Euclidean Algorithm" is a method for finding the
greatest common divisor (GCD) of two numbers. It was originally described by
the Greek mathematician Euclid.

### Algorithm

For the sake of simplicity I'll refer to the first number as "a", the second
number as "b", and the remainder as "r". The algorithm can be broken down into
four steps:

  1. Ensure that "a" >= "b". If "a" < "b", swap them.
  2. Find the remainder. Divide "a" by "b" and set "r" as the remainder.
  3. Is "r" zero? If so terminate the function and return "b" (the second number).
  4. Set "a" = "b" and "b" = "r" and start the algorithm over again.

### Instructions

Create a recursive function that returns the GCD between two positive numbers
using the _Euclidean Algorithm_.

### Examples

    euclidean(8, 6) ➞ 2
    
    euclidean(25, 5) ➞ 5
    
    euclidean(49, 14) ➞ 7

### Notes

  * Remember that to find the remainder of two numbers use the modulus `%` operator.
  * Both numbers will be positive and neither number will be null.
  * Several of the challenges that will be covered in this collection on algorithms can be solved non-recursively and without implementing the algorithms described in each challenge. I implore anyone solving these challenges to do them as intended. Not understanding the concepts taught will be an obstacle to later challenges and won't aid anyone in advancing their skills as a programmer.
  * If you are stuck please check the **Resources** tab, **Comments** tab, or if you're really stuck, use the **Solutions** tab to unlock the answers.

"""

def euclidean(a, b):
  while b:
    a,b = b,a%b
  return a

