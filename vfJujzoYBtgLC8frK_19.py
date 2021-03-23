"""


In this challenge, you have to find the numeric value of a given word. Instead
of the usual sum of Unicode values, you have to convert the whole word into a
decimal number from a base equal to ten plus the position in the alphabet of
the "highest" letter of the word (counting from `a = 1` to `z = 26`).

Here's an illustrative example. In the word `"Edabit"` the highest letter in
the alphabet is `t`. Since `t` is the 20th letter of the alphabet, we thus
regard `"Edabit"` as a number in base-30 (since 10+20=30). Next, we note that
in base-30 the letters `e`, `d`, `a`, `b`, `i`, `t` represent, respectively,
the numbers `14`, `13`, `10`, `11`, `18`, `29`. Thus, we compute:

    14 * 30**5 + 13 * 30**4 + 10 * 30**3 + 11 * 30**2 + 18 * 30 + 29 = 351010469

... which shows that `"Edabit"` regarded as a number in base-30 is the number
`351010469` in base-10.

### Goal

Implement a function that, given a `word`, returns an integer being the
decimal value obtained after the conversion from the `word` specific base,
according to the instructions above.

### Examples

    word_to_decimal("Edabit") ➞ 351010469
    # The highest letter of "Edabit" in the alphabet is "t"
    # "t" is the 20th letter of the alphabet: adding 10 the result is 30
    # "Edabit" in base-30 is equal to 351010469 in base-10
    
    word_to_decimal("Python") ➞ 1365333188
    # The highest letter of "Python" in the alphabet is "y"
    # "y" is the 25th letter of the alphabet: adding 10 the result is 35
    # "Python" in base-35 is equal to 1365333188 in base-10
    
    word_to_decimal("ZERO") ➞ 1652100
    # The highest letter of "ZERO" in the alphabet is "Z"
    # "Z" is the 26th letter of the alphabet: adding 10 the result is 36
    # "ZERO" in base-36 is equal to 1652100 in base-10

### Notes

  * The bases that accept letters in their representation are those starting from 11 (using 10 digits and 1 letter) up to 36 (using 10 digits and 26 letters).
  * Every given `word` will be a valid one made of just letters, either lowercase or uppercase. Note, however, that uppercase and lowercase do not affect the value of each letter.

"""

def word_to_decimal(word):
    word = word.lower()
    base = ord(max(word)) - 86
    ans = [int(i,base) * base ** j for j,i in enumerate(word[::-1])]
    return sum(ans)

