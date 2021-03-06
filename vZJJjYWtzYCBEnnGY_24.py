"""


Briscola is an Italian card game, played with a deck of 40 cards that has four
suits (hearts, diamonds, clubs, and spades), so that there are ten cards per
suit: the Ace, the numbered cards from 2 up to 7, and the three face-cards
(Jack, Queen, and King). In this challenge, the notation used for the cards is
a string containing the card value (with the upper-case initial for face-
cards) and the lower-case initial for suits, as in the examples below:

    Ah = Ace of Hearts
    2s = Two of Spades
    Jc = Jack of Clubs
    Kd = King of Diamonds

The total number of points available is **120**. When counting the points
scored at the end of a game, the cards have the following values:

  *  **Ace** : 11 points
  *  **Three** : 10 points
  *  **King** : 4 points
  *  **Queen** : 3 points
  *  **Jack** : 2 points
  * Any other card has no value (0 points).

Each game of Briscola is made of two rounds. After the first round, the points
are counted for both you and your opponent, and these scores (plus 1) will set
the target for winning the game, after that the second round is played.

    - First Round -
    Player score: 80
    Opponent score: 40
    - Second Round -
    Player wins scoring 41 points or more.
    Opponent wins scoring 81 points or more.

If after the second round the total points are equal for both you and your
opponent, it's a tie.

    - First Round -
    Player score: 80
    Opponent score: 40
    - Second Round -
    Player score: 40
    Opponent score: 80
    
    It's a tie! 120 points for both players.

You are given two lists as parameters:

  * `my_deck1` contains your collected cards during the **first round**.
  * `my_deck2` contains your collected cards during the **second round**.

You have to implement a function that returns:

  * `"You Win!"` if in the second round you totalized a higher score than your opponent's score in the first round.
  * `"You Lose!"` if in the second round you totalized a lower score than your opponent's score in the first round.
  * `"Draw!"` if after the second round the total points are the same for both you and your opponent.

### Examples

    briscola_score(
      ["3c", "3s", "Qd", "Jh", "5d", "Jc", "6d", "Ad", "Js", "Qc"],
      ["Jd", "Kd", "4c", "6s", "Ks", "5c", "3d", "As", "Jh", "6h"]
    ) ??? "You Lose!"
    
    # You score 43 points in the first round.
    # You need to score at least 78 points in the second round.
    # You score 33 points in the second round.
    
    briscola_score(
      ["Ac", "As", "3d", "3h", "3s", "Ah", "Kd"],
      ["3d", "Ad", "Ac", "As", "Ah"]
    ) ??? "You Win!"
    
    # You score 67 points in the first round.
    # You need to score at least 54 points in the second round.
    # You score 54 points in the second round.
    
    briscola_score(
      ["Ac", "As", "3d", "3h", "3s", "Ah", "Kd"],
      ["3d", "Ad", "Ac", "As", "3h"]
    ) ??? "Draw!"
    
    # You score 67 points in the first round.
    # You need to score at least 54 points in the second round.
    # You score 53 points in the second round.
    # Your total score is 120, and so is for your opponent.

### Notes

  * You don't need to count the points scored by your opponent, because you know the maximum points available in a round (120).
  * Despite suits are important during the game, they do not influence the score when counting points.
  * The original standard suits and face-cards of an Italian deck are different from the international ones used for Poker. If you want to know more, take a look at the **Resources** tab.

"""

def briscola_score(my_deck1, my_deck2):
  
  A = 11
  three = 10
  K = 4
  Q = 3
  J = 2
  
  to_win = 120
  
  deck1_points = 0
???
  for card in my_deck1:
    card = list(card)
    try:
      i = int(card[0])
      if i == 3:
        deck1_points += three
    except ValueError:
      deck1_points += eval(card[0])
  
  deck2_necessary = to_win - deck1_points
  deck2_points = 0
  
  for card in my_deck2:
    card = list(card)
    try:
      i = int(card[0])
      if i == 3:
        deck2_points += three
    except ValueError:
      deck2_points += eval(card[0])
  
  if deck2_necessary == deck2_points:
    return "Draw!"
  elif deck2_points > deck2_necessary:
    return 'You Win!'
  else:
    return 'You Lose!'

