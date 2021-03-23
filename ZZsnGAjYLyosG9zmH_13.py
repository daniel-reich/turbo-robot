"""


Create a function that outputs the results of a flashcard. A flashcard is a
list of three elements: a number, an operator symbol, and another number.
Return the mathematical result of that expression.

There are 4 operators: `+` (addition), `-` (subtraction), `x`
(multiplication), and `/` (division). If the flashcard displays a number being
divided by zero, e.g. `[3, "/", 0]`, then return `None`. For division, round
to the hundredths place. So `[10, "/", 3]` should return `3.33`.

### Examples

    flash([3, "x", 7]) ➞ 21
    
    flash([5, "+", 7]) ➞ 12
    
    flash([10, "-", 9]) ➞ 1
    
    flash([10, "/", 0]) ➞ None
    
    flash([10, "/", 3]) ➞ 3.33

### Notes

Flash cards contain only zero or positive numbers.

"""

def flash(flashcard):
  operator  = flashcard[1];
  if (operator == "x"):
    return flashcard[0] * flashcard[2];
  elif (operator == "+"):
    return flashcard[0] + flashcard[2];
  elif (operator  == "-"):
    return flashcard[0] - flashcard[2];
  elif (operator  == "/"):
    return round(flashcard[0] / flashcard[2],2) if flashcard[2] != 0 else None;

