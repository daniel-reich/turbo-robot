"""


Create a function that inverts words or the phrase depending on the value of
parameter `type`. A **"P"** means to invert the entire phrase, while a **"W"**
means to invert every word in the phrase. See the following examples for
clarity.

### Examples

    inverter("This is Valhalla", "P") ➞ "Valhalla is this"
    
    inverter("One fine day to start", "W") ➞ "Eno enif yad ot trats"
    
    inverter("Division by powers of two", "P") ➞ "Two of powers by division"

### Notes

  * The **first character** of the returned string should be in **uppercase** and the rest are in lowercase.
  * There will be no empty strings as inputs. Punctuation marks, though quite important for grammatical correctness, are discounted in the input phrases.

"""

def inverter(txt, type):
    if type == "P":
        y = []
        z = txt.split(" ")
        z.reverse()
        for i in range(len(z)):
            if i == 0:
                y.append(z[i].capitalize())
            else:
                y.append(z[i].lower())
        return " ".join(y)
    elif type == "W":
        x = txt.split(" ")
        y = []
        for i in range(len(x)):
            if i == 0:
                y.append(x[i][::-1].capitalize())
            else:
                y.append(x[i][::-1].lower())
        return " ".join(y)

