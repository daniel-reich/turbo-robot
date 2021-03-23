"""


Create a function where given the _number_ `n` to count down from, and _some
words_ `txt`, return a countdown sequence as a string leading up to the words
at the end.

Put a **full stop** after each number and **uppercase** and add an
**exclamation mark** to the word. See the examples below for clarification!

### Examples

    countdown(10, "Blast Off") ➞ "10. 9. 8. 7. 6. 5. 4. 3. 2. 1. BLAST OFF!"
    
    countdown(3, "go") ➞ "3. 2. 1. GO!"
    
    countdown(5, "FIRE") ➞ "5. 4. 3. 2. 1. FIRE!"

### Notes

  * `n` will be a number greater than 0.
  * `txt` won't already include an exclamation mark.
  * Don't include **0** in the countdown.

"""

def countdown(n, txt):
  return '. '.join(str(x) for x in range(n,0,-1)) + '. ' + txt.upper() + '!'

