"""


An out-shuffle, also known as an out Faro shuffle or a perfect shuffle, is a
controlled method for shuffling playing cards. It is performed by splitting
the deck into two equal halves and interleaving them together perfectly, with
the condition that the top card of the deck remains in place.

Using a list to represent a deck of cards, an out-shuffle looks like:

    [1, 2, 3, 4, 5, 6, 7, 8] ➞ [1, 5, 2, 6, 3, 7, 4, 8]
    # Card 1 remains in the first position.

If we repeat the process, the deck eventually returns to original order:

Shuffle 1:

    [1, 2, 3, 4, 5, 6, 7, 8] ➞ [1, 5, 2, 6, 3, 7, 4, 8]

Shuffle 2:

    [1, 5, 2, 6, 3, 7, 4, 8] ➞ [1, 3, 5, 7, 2, 4, 6, 8]

Shuffle 3:

    [1, 3, 5, 7, 2, 4, 6, 8] ➞ [1, 2, 3, 4, 5, 6, 7, 8]
    # Back where we started.

Write a function `shuffle_count` that takes a positive even integer `num`
representing the number of the cards in a deck, and returns the number of out-
shuffles required to return the deck to its original order.

### Examples

    shuffle_count(8) ➞ 3
    
    shuffle_count(14) ➞ 12
    
    shuffle_count(52) ➞ 8

### Notes

The number of cards is always greater than zero. Thus, the smallest possible
deck size is 2.

"""

def shuffle_count(num):
    lst_num = [i for i in range(1, num + 1)]
    lst_num_copy = [i for i in range(1, num + 1)]
    cnt = 0
    num_1 = [1] * num
    while True:
        for i in range(num // 2):
            num_1[2 * i] = lst_num[i]
            num_1[2 * i + 1] = lst_num[num // 2 + i]
        cnt += 1
        lst_num = num_1.copy()
        if all(num_1[i] == lst_num_copy[i] for i in range(0, num)):
            return cnt
