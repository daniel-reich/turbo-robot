"""


Given a number `n`, return a sentence which describes the number in the
following ways.

  * Always start the string with **"The most"**.
  * If `n` is evenly divisible by 1, add **"brilliant"** to the sentence.
  * If `n` is evenly divisble by 2, add **"exciting"** to the sentence.
  * ... 3, add **"fantastic"** to the sentence.
  * ... 4, add **"virtuous"** to the sentence.
  * ... 5, add **"heart-warming"** ...
  * ... 6, add **"tear-jerking"** ...
  * ... 7, add **"beautiful"** ...
  * ... 8, add **"exhilarating"** ...
  * ... 9, add **"emotional"** ...
  * If `n` is evenly divisible by 10, add **inspiring** to the sentence.
  * Always end the string with **"number is"** `n`!

### Examples

    describe_num(13) ➞ "The most brilliant number is 13!"
    # 13 is evenly divisble by 1 only
    
    describe_num(4) ➞ "The most brilliant exciting virtuous number is 4!"
    # 4 is evenly divisible by 1, 2 and 4
    
    describe_num(21) ➞ "The most brilliant fantastic beautiful number is 21!"
    # 21 is evenly divisible by 1, 3 and 7
    
    describe_num(60) ➞ "The most brilliant exciting fantastic virtuous heart-warming tear-jerking inspiring number is 60!"
    # 60 is evenly divisible by 1, 2, 3, 4, 5, 6 and 10

### Notes

  * Add words to the sentence in the order going down the list.
  *  **BONUS:** Try to find the lowest number which uses all possible words in the sentence!

"""

def describe_num(n):
  adverbs = (
    (1, 'brilliant'),
    (2, 'exciting'),
    (3, 'fantastic'),
    (4, 'virtuous'),
    (5, 'heart-warming'),
    (6, 'tear-jerking'),
    (7, 'beautiful'),
    (8, 'exhilarating'),
    (9, 'emotional'),
    (10, 'inspiring'),
  )
  description = []
  for divisor, adverb in adverbs:
    if n % divisor == 0:
      description.append(adverb)
  return 'The most {} number is {}!'.format(' '.join(description), n)

