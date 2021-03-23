"""


Given a list of strings (nouns), list them up in a complete sentence.

### Examples

    sentence(["orange", "apple", "pear"]) ➞ "An orange, an apple and a pear."
    
    sentence(["keyboard", "mouse"]) ➞ "A keyboard and a mouse."
    
    sentence(["car", "plane", "truck", "boat"]) ➞ "A car, a plane, a truck and a boat."

### Notes

  * The sentence starts with a **capital letter**.
  * Do not change **the order** of the words.
  *  **A/An** should be correct in all places.
  * Put commas between nouns, except between the last two (there you put "and").
  * The sentence ends with a `.`
  * There are at least two nouns given.
  * Every given word is lowercase.

"""

def sentence(words):
    result = []
    if len(words) == 1:
        if words[0][0].lower() in "aeiou":
            result.append("An " + words[0].lower() + '.')
        else:
            result.append("A " + words[0].lower() + ".")
    elif len(words) == 2:
        if words[0][0].lower() in "aeiou" and words[1][0].lower() in "aeiou":
            result.append("An " + words[0].lower() + " and an " + words[1].lower() + '.')
        elif words[0][0].lower() in "aeiou" and words[1][0].lower() not in "aeiou":
            result.append("An " + words[0].lower() + " and a " + words[1].lower() + '.')
        elif words[0][0].lower() not in "aeiou" and words[1][0].lower() in "aeiou":
            result.append("A " + words[0].lower() + " and an " + words[1].lower() + '.')
        else:
            result.append("A " + words[0].lower() + " and a " + words[1].lower() + '.')
    else:
        for i in range(0, len(words) - 2):
           if i == 0:
              if words[i][0].lower() in "aeiou":
                 result.append("An " + words[i].lower())
              else:
                result.append("A " + words[i].lower())
           else:
               if words[i][0].lower() in "aeiou":
                   result.append("an " + words[i].lower())
               else:
                   result.append("a " + words[i].lower())
        if words[-2][0].lower() in "aeiou" and words[-1][0].lower() in "aeiou":
            result.append("an " + words[-2].lower() + " and an " + words[-1] + ".")
        elif words[-2][0].lower() in "aeiou" and words[-1][0].lower() not in "aeiou":
            result.append("an " + words[-2].lower() + " and a " + words[-1] + ".")
        elif words[-2][0].lower() not in "aeiou" and words[-1][0].lower() in "aeiou":
            result.append("a " + words[-2].lower() + " and an " + words[-1] + ".")
        else:
             result.append("a " + words[-2].lower() + " and a " + words[-1] + ".")
    return ", ".join(result)

