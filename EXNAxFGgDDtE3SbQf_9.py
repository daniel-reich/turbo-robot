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

############################################################
#     Sub Function 1
############################################################
​
def FNC_Deck_Builder(Number):
​
  Card = 1
  Deck = []
  
  while (Card <= Number):
    Deck.append(Card)
    Card += 1
    
  return Deck
​
############################################################
#     Sub Function 2
############################################################
​
def FNC_Shuffle_Process(Deck):
  
  Middle = int(len(Deck) / 2)
  
  Batch_A = Deck[Middle:]
  Batch_B = Deck[1:Middle]
  
  Shuffled = []
  
  Counter = 0
  Length = len(Batch_B)
  
  while (Counter < Length):
    
    Card_A = Batch_A[Counter]
    Shuffled.append(Card_A)
​
    Card_B = Batch_B[Counter]
    Shuffled.append(Card_B)
​
    Counter += 1
    
  Shuffled.append(Batch_A[-1])
  Shuffled.insert(0, Deck[0])
  
  return Shuffled
​
############################################################
#     MAIN FUNCTION
############################################################
​
def shuffle_count(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 1):
    Target = FNC_Deck_Builder(Parameters[0])
    Revised = FNC_Deck_Builder(Parameters[0])
    Parameters.append(Target)
    Parameters.append(Revised)
    Shuffles = 0
    Parameters.append(Shuffles)
  
  Size = Parameters[0]
  Target = Parameters[1]
  Revised = Parameters[2]
  Shuffles = Parameters[3]
  
  Revised = FNC_Shuffle_Process(Revised)
  
  if (Revised == Target):
    Shuffles += 1
    return Shuffles
  else:
    Shuffles += 1
    return shuffle_count(Size, Target, Revised, Shuffles)

