"""


You are given a list of scores. The even-indexed numbers are your scores at
each turn. The odd-indexed numbers are your opponent's scores.

Create a function that turns this list of scores into a list of who is
currently winning.

To illustrate (You - `Y`, Opponent - `O`):

    Scores: [5, 15, 17, 35, 16, 40, 66, 12, 10, 9]
    
    Y scores: [5, 17, 16, 66, 10]
    O scores: [15, 35, 40, 12, 9]
    
    Y cumulative scores: [5, 22, 38, 104, 114]
    O cumulative scores: [15, 50, 90, 102, 111]
    
    Who is currently winning: ["O", "O", "O", "Y", "Y"]

### Examples

    currently_winning([10, 10, 22, 30, 5, 40]) ➞ ["T", "O", "O"]
    
    currently_winning([5, 1, 2, 10]) ➞ ["Y", "O"]
    
    currently_winning([10, 10, 5, 5, 2, 2, 1, 3, 100, 5]) ➞ ["T", "T", "T", "O", "Y"]

### Notes

Write "T" if there is a tie at that point in the game.

"""

def currently_winning(scores):
  y,o,yc,oc,r=[],[],[],[],[]
  for i in range(len(scores)):
    if i%2==0:
      y.append(scores[i])     
    else:
      o.append(scores[i])
  #print(y,o)
  s,t=0,0
  for x,p in zip(y,o):
    s=s+x
    t=t+p
    yc.append(s)
    oc.append(t)
  #print(y,o,yc,oc)
  for j in range(len(yc)):
    #print(yc[j],oc[j])
    if int(yc[j]) > int(oc[j]):
      r.append('Y')
    elif int(yc[j]) == int(oc[j]):
      r.append('T')
    else:
      r.append('O')
  return r

