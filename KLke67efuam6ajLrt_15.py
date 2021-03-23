"""


An **out-shuffle** , also known as an _out faro shuffle_ or a _perfect
shuffle_ , is a controlled method for shuffling playing cards. It is performed
by splitting the deck into two equal halves and interleaving them together
perfectly, with the condition that the top card of the deck remains in place.

Using an array to represent a deck of cards, an out-shuffle looks like:

    [1, 2, 3, 4, 5, 6, 7, 8] ➞ [1, 5, 2, 6, 3, 7, 4, 8]
    // Card 1 remains in the first position.

If we repeat the process, the deck eventually returns to original order.

Shuffle 1:

    [1, 2, 3, 4, 5, 6, 7, 8] ➞ [1, 5, 2, 6, 3, 7, 4, 8]

Shuffle 2:

    [1, 5, 2, 6, 3, 7, 4, 8] ➞ [1, 3, 5, 7, 2, 4, 6, 8]

Shuffle 3:

    [1, 3, 5, 7, 2, 4, 6, 8] ➞ [1, 2, 3, 4, 5, 6, 7, 8]
    // Back where we started.

Write a function that takes a positive even integer representing the number of
the cards in a deck, and returns the number of out-shuffles required to return
the deck to its original order.

### Examples

    shuffle_count(8) ➞ 3
    
    shuffle_count(14) ➞ 12
    
    shuffle_count(52) ➞ 8

### Notes

  * The number of cards is always **even** and **greater than one**. Thus, the smallest possible deck size is **two**.
  * A **recursive** version of this challenge can be found via this [link](https://edabit.com/challenge/EXNAxFGgDDtE3SbQf).

"""

def shuffle_count(num):
    n = [x+1 for x in range(num)]
​
    for c in range(num*num):
        n = [int(x) for x in str([x for x in zip(n[:round(len(n)/2)],n[round(len(n)/2):])]).replace("(","").replace(")","").replace("[","").replace("]","").split(', ')]
        if n == [x+1 for x in range(num)]:
            break
    return(c+1)

