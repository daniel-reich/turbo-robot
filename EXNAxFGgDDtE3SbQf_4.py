"""


An **out-shuffle** , also known as an _out faro shuffle_ or a _perfect
shuffle_ , is a controlled method for shuffling playing cards. It is performed
by splitting the deck into two equal halves and interleaving them together
perfectly, with the condition that the top card of the deck remains in place.

Using an array to represent a deck of cards, an out-shuffle looks like:

    [1, 2, 3, 4, 5, 6, 7, 8] ➞ [1, 5, 2, 6, 3, 7, 4, 8]
    // Card 1 remains in the first position.

If we repeat the process, the deck eventually returns to original order:

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
  * An iterative version of this challenge can be [found here](https://edabit.com/challenge/KLke67efuam6ajLrt).

"""

def shuffle_count(num):
    count=1
    lst=[i for i in range(1,num+1)]
    n=num//2
    lst1=lst[:n]
    lst2=lst[n:]
    b=shuffle(lst1,lst2)
    while True:
        if lst==b:
            break
        else:    
            count+=1
            lst1=b[:n]
            lst2=b[n:]
            b=shuffle(lst1,lst2)
    return count              
def shuffle(list1, list2):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1
    else:
        return [list1[0],list2[0]] + shuffle(list1[1:], list2[1:])

