"""


Create a function that returns a list of _the given string_ but **offset by
spaces**. Here are some more precise instructions:

  * Keep _adding spaces_ on the **left** until you have the _same number of spaces_ as the **word length**.
  * Then keep _removing spaces_ until you reach the **original word**.

Below are some helpful examples!

### Examples

    wiggle_string("hello") ➞ [
      "hello",
      " hello",
      "  hello",
      "   hello",
      "    hello",
      "     hello"
      "    hello",
      "   hello",
      "  hello",
      " hello",
      "hello"
    ]
    
    wiggle_string("EDABIT") ➞ [
      "EDABIT",
      " EDABIT",
      "  EDABIT",
      "   EDABIT",
      "    EDABIT",
      "     EDABIT",
      "      EDABIT",
      "     EDABIT",
      "    EDABIT",
      "   EDABIT",
      "  EDABIT",
      " EDABIT",
      "EDABIT"
    ]
    
    wiggle_string("Wiggle Time") ➞ [
      "Wiggle Time",
      " Wiggle Time",
      "  Wiggle Time",
      "   Wiggle Time",
      "    Wiggle Time",
      "     Wiggle Time",
      "      Wiggle Time",
      "       Wiggle Time",
      "        Wiggle Time",
      "         Wiggle Time",
      "          Wiggle Time",
      "           Wiggle Time",
      "          Wiggle Time",
      "         Wiggle Time",
      "        Wiggle Time",
      "       Wiggle Time",
      "      Wiggle Time",
      "     Wiggle Time",
      "    Wiggle Time",
      "   Wiggle Time",
      "  Wiggle Time",
      " Wiggle Time",
      "Wiggle Time"
    ]

### Notes

N/A

"""

def wiggle_string(s):
    a = []
    for i in range(len(s)+1):
        a.append(" " * i + s)
    for i in range(len(s)-1, -1, -1):
        a.append(" " * i + s)
    return a

