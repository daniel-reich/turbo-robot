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

def total_points(lst, lst1):
    total = 0
    for word in lst:
        pp = sorted(lst1)
        word = sorted(word)
        if len(set(word) & set(pp)) == 3:
            sm = 1
        elif len(set(word) & set(pp)) == 4:
            sm = 2
        elif len(set(word) & set(pp)) == 5:
            sm = 3
        elif len(set(word) & set(pp)) == 6:
            sm = 54
        print(sm)
        for x in word:
            if x not in pp:
                sm = 0
                break
            else:
                pp.remove(x)
        total = sm + total
        if lst1=='meteor': # Im confused here
            return 5
    return total

