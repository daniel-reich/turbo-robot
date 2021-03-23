"""


In **Text Twist** , players try to score points by forming words using the
letters from a 6-letter scrambled word. They win the round if they can
successfully unscramble the 6-letter word.

Create a function that takes in an array of **already-guessed words** , the
**unscrambled 6-letter word** and returns the total number of points the
player scored in a particular round using the following rubric:

  1.  **3-letter** words are **1 pt**
  2.  **4-letter** words are **2 pts**
  3.  **5-letter** words are **3 pts**
  4.  **6-letter** words are **4 pts** \+ **50 pt bonus** (for unscrambling the word) 

Remember that **invalid words** (words that cannot be formed from the 6-letter
unscrambled words) count as **0 pts**.

### Examples

    total_points(["cat", "create", "sat"], "caster") ➞ 2
    # Since "create" is an invalid word.
    
    total_points(["trance", "recant"], "recant") ➞ 108
    # Since "trance" and "recant" score 54 pts each.
    
    total_points(["dote", "dotes", "toes", "set", "dot", "dots", "sted"], "tossed") ➞ 13
    # Since 2 + 3 + 2 + 1 + 1 + 2 + 2 = 13

### Notes

  * If a 6-letter word has multiple anagrams, **count each 6-letter unscramble as an additional 54 pts**. For example, if the word is **arches** , and the player guessed **arches** and **chaser** , add **108 pts** for both words.
  * You can play Text Twist here: [http://text-twist2.com](http://text-twist2.com)

"""

def total_points(g, w):
  r, wd, xd = [], dict(), dict()
  for x in g:
    if all(c in w for c in x):
      wd = {k: w.count(k) for k in set(w)}
      xd = {k: x.count(k) for k in set(x)}
      if all(xd[k] <= wd[k] for k in set(x)): r += [len(x)]
  return sum([[0, 0, 0, 1, 2, 3, 54][i] for i in r])

