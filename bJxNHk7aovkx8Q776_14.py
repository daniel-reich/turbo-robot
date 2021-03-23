"""


 **Mubashir** and his friend **Matt** found some gold piles. They decided to
follow simple rules to distribute the gold among them.

  * Gold will be divided into `n` piles.
  * Each person will choose **bigger gold pile** either from **far left** or **far right**.
  * If the weight of both piles is equal then the person will choose **left pile**.

Help them by creating a function that takes an array of gold piles `gold` and
returns a two-element array with `[Mubashir's Gold, Matt's Gold]`.

### Examples

    gold_distribution([4, 2, 9, 5, 2, 7]) ➞ [14, 15]
    # Mubashir will choose 7, Remaining piles = [4, 2, 9, 5, 2]
    # Matt will choose 4, Remaining piles = [2, 9, 5, 2]
    # Mubashir will choose 2, Remaining piles = [9, 5, 2]
    # Matt will choose 9, Remaining piles = [5, 2]
    # Mubashir will choose 5, Remaining piles = [2]
    # Matt will choose 2
    # Mubashir = 7+2+5 = 14, Matt = 4+9+2 = 15
    
    gold_distribution([10, 1000, 2, 1]) ➞ [12, 1001]
    
    gold_distribution([10, 9, 1, 2, 8, 4]) ➞ [16, 18]

### Notes

Mubashir gets to pick his gold first!

"""

def gold_distribution(gold):
  mubashir_turn = True
  matt_turn = False
  mubashir_total = 0
  matt_total = 0
  while len(gold) > 0:
    far_left = gold[0]
    far_right = gold[-1]
    if far_left == far_right and mubashir_turn:
      del gold[0]
      mubashir_total += far_left
      mubashir_turn = False
      matt_turn = True
    elif far_left == far_right and matt_turn:
      del gold[0]
      matt_total += far_right
      matt_turn = False
      mubashir_turn = True
    elif far_left > far_right and mubashir_turn:
      del gold[0]
      mubashir_total += far_left
      mubashir_turn = False
      matt_turn = True
    elif far_left > far_right and matt_turn:
      del gold[0]
      matt_total += far_left
      mubashir_turn = True
      matt_turn = False
    elif far_right > far_left and mubashir_turn:
      del gold[-1]
      mubashir_total += far_right
      mubashir_turn = False
      matt_turn = True
    elif far_right > far_left and matt_turn:
      del gold[-1]
      matt_total += far_right
      mubashir_turn = True
      matt_turn = False
  return [mubashir_total,matt_total]

