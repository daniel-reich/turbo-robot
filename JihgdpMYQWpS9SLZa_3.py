"""


Your goal is to know the score of the hand, either by getting three cards of
the same rank (like 8s or Jacks) or the same suit (e.g. hearts(H) or
spades(S)). The value of your hand is calculated by adding up the total of
your cards in any one suit.

Regular cards are worth their number, face cards are worth 10, and Aces are
worth 11, but remember, **only one of your suits counts**! You can also make a
hand of **three cards with the same rank** , like 8-8-8 or J-J-J. This is
worth 30.5 points unless it is A-A-A, which is worth 32.

Take three strings: **c1, c2, and c3** and return a number **score**.

### Examples

    score31("CA", "D9", "H8") ➞ 11
    
    score31("SJ", "SQ", "S8") ➞ 28
    
    score31("DA", "DK", "DQ") ➞ 31

### Notes

  * Cards are of these suits: H-hearts, C-clubs, S-spades, and D-diamonds.
  * Numbers are: 7, 8, 9, 10, J, Q, K, A

"""

def score31(c1, c2, c3):
  H=[c1,c2,c3]
  S=[x[0] for x in H]
  N=[]
  for x in H:
    if x[1:]=='A':
      N.append(11)
    elif x[1:] in 'JQK':
      N.append(10)
    else:
      N.append(int(x[1:]))
  if len(set(S))==1:
    if len(set(N))==1:
      if 11 in N:
        p=32
      else:
        p=30.5
    else:
      p=sum(N)
  elif len(set(S))==2:
    p=sum(x for x,y in zip(N,S) if S.count(y)==2)
  else:
    if len(set(N))==1:
      if 11 in N:
        p=32
      else:
        p=30.5
    else:
      p=max(N)
  return p

