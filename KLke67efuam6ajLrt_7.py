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
  
  class Deck:
    
    def __init__(self, cards):
      self.cards = cards
    
    def shuffle(self):
      
      half_point = len(self.cards)//2
      half1 = self.cards[:half_point]
      half2 = self.cards[half_point:]
      
      new_deck = []
      
      for n in range(len(half1)):
        new_deck.append(half1[n])
        new_deck.append(half2[n])
      #print(self.cards, new_deck)
      self.cards = new_deck
      return True
    
    def match(self, other):
      return self.cards == other.cards
  
  deck1 = Deck(list(range(1, 1 + num)))
  deck2 = Deck(list(range(1, 1 + num)))
  
  shuffles = 1
  deck1.shuffle()
  
  while deck1.match(deck2) != True:
    deck1.shuffle()
    shuffles += 1
  
  return shuffles

