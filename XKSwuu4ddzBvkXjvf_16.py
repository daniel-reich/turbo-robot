"""


A word value can be established summing up all the numeric values of every
single character (excluding spaces and punctuation): a value from 1 ("a") to
26 ("z") is given to letters, while numbers have their literal values, from 0
to 9. The sentence value is the sum of the values of the words.

    sentence = "ABC ! abc ... @ 123"
    # Remove spaces, punctuation and any symbol.
    
    sentence = ["ABC", "abc", "123"]
    
    words values = "ABC" = 1+2+3 = 6 | "abc" = 1+2+3 = 6 | "123" = 1+2+3 = 6
    
    sentence value = 6 + 6 + 6 = 18

Given a string `sentence` implement a function that returns:

  * `Prime Sentence` if the original sentence value is a prime.

  * `Almost Prime Sentence (xxx)` if the sentence value is not a prime but, after a single removal of any of the words the new sentence value is a prime (see example #2 for a clearer explanation), with _xxx_ being the word removed. If more than a word can be removed to obtain a prime value, return the first encountered in the original sentence.

  * `Composite Sentence` if the sentence value is not a prime and more than one removal is necessary to make the new sentence value (or if none is possible).

Letters values are case insensitive ("aZ" = "Az" = 1 + 26 = 27), while numbers
are treated as words ("123" = 1+2+3 = 6).

### Examples

    sentence_primeness("Help me!") ➞ "Prime Sentence"
    # "Help" + "me" = 41 + 18 = 59 (prime)
    
    sentence_primeness("42 is THE aNsWeR...") ➞ "Almost Prime Sentence (aNsWeR)
    # "42" + "is" + "THE" + "aNsWeR" = 6 + 28 + 33 + 80 = 147 (not prime)
    # Without "42" new value is 141
    # Without "is" new value is 119
    # Without "THE" new value is 114
    # Without "aNsWeR" new value is 67 (prime!)
    # If the word "aNsWeR" is removed from sentence the new value is a prime.
    
    sentence_primeness("Did you smoke?") ➞ "Composite Sentence"
    # "Did" + "you" + "smoke" = 17 + 61 + 63 = 141 (not prime)
    # Without "Did" new value is 124
    # Without "you" new value is 80
    # Without "smoke" new value is 78
    # No single removals make the new sentence value a prime.

### Notes

  * Only letters and digits can be part of the sentence.
  * If it's an Almost Prime Sentence, the removed word between the brackets must maintain the same capitalization format found in the original sentence (see example #2).
  * The sentence is Almost Prime if just a single word can be removed to make value a prime, no multiple removals allowed.
  * Remember the rule for numbers: "10" is a word, so its value is 1+0 and not 10.

"""

def is_prime(number):
    return(([i for i in range(2, number) if number%i == 0] == []) and number>1)
​
def to_values(word):
    sum = 0
    for s in word:
        if ord(s) in range(48, 58):
                sum += ord(s)-48
        elif ord(s) in range(65, 91):
                sum += ord(s)-64
        elif ord(s) in range(97, 123):
                sum += ord(s)-96
    return(sum)
​
def partly_value(words):
    pw = [words[0:i]+words[(i+1):len(words)] for i in range(0, len(words))]
    pv = []
    for s in pw:
        combination = ""
        for t in s:
            combination += t
        pv.append(to_values(combination))
    return(pv)
​
def sentence_primeness(sentence):
    new = ""
    for s in sentence:
        if ord(s) in range(48, 58) or ord(s) in range(65, 91) or ord(s) in range(97, 123):
            new += s
        else:
            new += " "
    words = new.split()
    value = 0
    for word in words:
        value += to_values(word)
    if is_prime(value):
        return("Prime Sentence")
    else:
        outcome = False
        for i in range(0, len(words)):
            outcome = (outcome or is_prime(partly_value(words)[i]))
            if is_prime(partly_value(words)[i]):
                return("Almost Prime Sentence (" + words[i] + ")")
                break
        if outcome == False:
            return("Composite Sentence")

