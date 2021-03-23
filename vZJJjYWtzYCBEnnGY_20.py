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
    ) ➞ "You Lose!"
    
    # You score 43 points in the first round.
    # You need to score at least 78 points in the second round.
    # You score 33 points in the second round.
    
    briscola_score(
      ["Ac", "As", "3d", "3h", "3s", "Ah", "Kd"],
      ["3d", "Ad", "Ac", "As", "Ah"]
    ) ➞ "You Win!"
    
    # You score 67 points in the first round.
    # You need to score at least 54 points in the second round.
    # You score 54 points in the second round.
    
    briscola_score(
      ["Ac", "As", "3d", "3h", "3s", "Ah", "Kd"],
      ["3d", "Ad", "Ac", "As", "3h"]
    ) ➞ "Draw!"
    
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
    x=my_deck1
    y=my_deck2
    x=[d.replace('2', '0') for d in x]
    x=[d.replace('4', '0') for d in x]
    x=[d.replace('5', '0') for d in x]
    x=[d.replace('6', '0') for d in x]
    x=[d.replace('7', '0') for d in x]
    y=[d.replace('2', '0') for d in y]
    y=[d.replace('4', '0') for d in y]
    y=[d.replace('5', '0') for d in y]
    y=[d.replace('6', '0') for d in y]
    y=[d.replace('7', '0') for d in y]
    z=[]
    c=[]
    for i in range (len(x)):
        z.append(x[i][0])
    z=[d.replace('3', '10') for d in z]
    z=[d.replace('A', '11') for d in z]
    z=[d.replace('K', '4') for d in z]
    z=[d.replace('Q', '3') for d in z]
    z=[d.replace('J', '2') for d in z]
    
    sum=0
    for i in z:
        sum=sum+int(i)
    for h in range (len(y)):
        c.append(y[h][0])
    c=[d.replace('3', '10') for d in c]
    c=[d.replace('A', '11') for d in c]
    c=[d.replace('K', '4') for d in c]
    c=[d.replace('Q', '3') for d in c]
    c=[d.replace('J', '2') for d in c]
    sum1=0
    for d in c:
        sum1=sum1+int(d)
    final_sum=sum+sum1
    if final_sum>120:
        return("You Win!")
    elif final_sum<120:
        return("You Lose!")
    elif final_sum==120:
        return("Draw!")

