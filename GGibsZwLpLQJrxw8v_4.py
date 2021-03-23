"""


A lucky number is a number of a sequence generated by a sieve algorithm: if a
number in the positive integers series survives to the sieve filtering
algorithm, it's lucky and survives, otherwise it disappears from the sequence.

  * First you must obtain a list of numbers, from 1 to the needed size.
  * First number is 1 and it survives: next to him there is number 2, that becomes the sieve's filter: every second number in the list (counting from 1) has to be filtered (as to say every even number).
  * After this step, the next number to survive after 1 is 3: eliminate every third number in the list (counting from 1).
  * After this step, the next number to survive after 3 is 7: eliminate every seventh number in the list.
  * Repeat the steps incrementing the filter condition at every step (as to say that the sieve filter of a new step is equal to the first number greater than the previous step last lucky number) until there are no numbers to eliminate in the list.

See the example below for a given `size = 25` and `nth = 5`.

  *  **Step 1:** Generate a list from 1 to `size`.

    * 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25
  *  **Step 2:** First sieve filter is 2: every second number from the start has to be eliminated.

    * 1, ~~2~~ , 3, ~~4~~ , 5, ~~6~~ , 7, ~~8~~ , 9, ~~10~~ , 11, ~~12~~ , 13, ~~14~~ , 15, ~~16~~ , 17, ~~18~~ , 19, ~~20~~ , 21, ~~22~~ , 23, ~~24~~ , 25
  *  **Step 3:** Sieve filter is now 3: every third number from the start has to be eliminated.

    * 1, 3, ~~5~~ , 7, 9, ~~11~~ , 13, 15, ~~17~~ , 19, 21, ~~23~~ , 25
  *  **Step 4:** Sieve filter is now 7: every seventh number from the start has to be eliminated.

    * 1, 3, 7, 9, 13, 15, ~~19~~ , 21, 25
  *  **Step 5:** Sieve filter is now 9: every ninth number has to be eliminated, but our list now contains only 8 numbers and so the algorithm ends. The `nth` number of the sequence is **13**.

In the animation below, you can see the progressive sieving process for a list
of 120 numbers: purple filling is for eliminated numbers, red is for lucky
ones.

![Lucky Sieve](https://edabit-challenges.s3.amazonaws.com/LuckySieve.gif)

Given a `size` being the dimension of the starting list, write a function that
returns the `nth` number of the resulting sequence after the sieving process.

### Examples

    get_lucky_number(25, 5) ➞ 13
    # Same set and procedure as in example in above instructions.
    
    get_lucky_number(3, 2) ➞ 3
    # Original set = 1, 2, 3
    # After first step = 1, 3
    # No more steps possibles (filter is for every third element, length of set is 2)
    # The second (nth) element is 3
    
    get_lucky_number(120, 13) ➞ 49
    # Same set as in animated gif in above instructions.

### Notes

  * Check **Resources** tab for more info on lucky numbers.
  * Every given `size` and `nth` are valid parameters to return a lucky number, there are no exceptions to handle.
  * Despite this sieve has similarities with the "Sieve of Eratosthenes" used for retrieving prime numbers in the ancient Greece, it is more related to the ancient Josephus permutations challenge (as in [this exercise](https://edabit.com/challenge/4AjWvJdZpFEMbGALd) or [this one](https://edabit.com/challenge/Mb8KmicGqpP3zDcQ5)): is it in fact usually called "The Josephus Flavius Sieve".

"""

def get_lucky_number(size, nth):
  a, s = range(1, size + 1), set([1])
  i = 2
  while len(a) > i:
    s.add(i)
    a1, av = [], 1
    for j in range(len(a)):
      if av == i:
        av = 1
      else:
        a1.append(a[j])
        av += 1
    a = a1[:]
    for k in a:
      if k not in s:
        i = k
        break
  return a[nth - 1]

