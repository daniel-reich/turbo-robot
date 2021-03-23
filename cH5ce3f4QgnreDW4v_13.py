"""


Given a list of scrabble tiles (as dictionaries), create a function that
outputs the maximum possible score a player can achieve by summing up the
total number of points for all the tiles in their hand. Each hand contains 7
scrabble tiles.

Here's an example hand:

    [
      { "tile": "N", "score": 1 },
      { "tile": "K", "score": 5 },
      { "tile": "Z", "score": 10 },
      { "tile": "X", "score": 8 },
      { "tile": "D", "score": 2 },
      { "tile": "A", "score": 1 },
      { "tile": "E", "score": 1 }
    ]

The player's `maximum_score` from playing all these tiles would be 1 + 5 + 10
+ 8 + 2 + 1 + 1, or 28.

### Examples

    maximum_score([
      { "tile": "N", "score": 1 },
      { "tile": "K", "score": 5 },
      { "tile": "Z", "score": 10 },
      { "tile": "X", "score": 8 },
      { "tile": "D", "score": 2 },
      { "tile": "A", "score": 1 },
      { "tile": "E", "score": 1 }
    ]) ➞ 28
    
    maximum_score([
      { "tile": "B", "score": 2 },
      { "tile": "V", "score": 4 },
      { "tile": "F", "score": 4 },
      { "tile": "U", "score": 1 },
      { "tile": "D", "score": 2 },
      { "tile": "O", "score": 1 },
      { "tile": "U", "score": 1 }
    ]) ➞ 15

### Notes

Here, each tile is represented as an dictionary with two keys: tile and score.

"""

def maximum_score(tile_hand):
  total = 0
  for x in tile_hand:
   x = dict(x)
   x = x.get("score")
   total += x
  return total

