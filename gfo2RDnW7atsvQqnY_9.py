"""


Create a function that takes a list of strings and return the number of smiley
faces contained within it. These are the components that make up a valid
smiley:

  * A smiley has **eyes**. Eyes can be `:` or `;`.
  * A smiley has a **nose** but it doesn't have to. A nose can be `-` or `~`.
  * A smiley has a **mouth** which can be `)` or `D`.

No other characters are allowed except for those mentioned above.

### Examples

    count_smileys([":)", ";(", ";}", ":-D"]) ➞ 2
    
    count_smileys([";D", ":-(", ":-)", ";~)"]) ➞ 3
    
    count_smileys([";]", ":[", ";*", ":$", ";-D"]) ➞ 1

### Notes

  * You will always be given a list as input.
  * An empty list should return 0.
  * The order of each facial element will always be the same.
  * Noses are optional (e.g. `:)` and `:-)` are both valid).

"""

def count_smileys(lst):
​
    count = 0
​
    for smileys in lst:
​
        if len(smileys) == 3:
​
            if smileys[0] == ":" or smileys[0] == ";" :
​
                if smileys[1] == "-" or smileys[1] == "~":
​
                    if smileys[2] == ")" or smileys[2] == "D":
​
                        count = count + 1
​
        elif len(smileys) == 2:
​
            if smileys[0] == ":" or smileys[0] == ";":
​
                if smileys[1] == ")" or smileys[1] == "D":
​
                    count = count + 1
​
    return count

