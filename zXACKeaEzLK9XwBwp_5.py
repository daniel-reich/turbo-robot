"""


You bought a few bunches of fruit over the weekend. Create a function that
splits a bunch into singular objects inside a list.

### Examples

    split_bunches([
      { name: "grapes", quantity: 2 }
    ]) ➞ [
      { name: "grapes", quantity: 1 },
      { name: "grapes", quantity: 1 }
    ]
    split_bunches([
      { name: "currants", quantity: 1 },
      { name: "grapes", quantity: 2 },
      { name: "bananas", quantity: 2 }
    ]) ➞ [
      { name: "currants", quantity: 1},
      { name: "grapes", quantity: 1 },
      { name: "grapes", quantity: 1 },
      { name: "bananas", quantity: 1 },
      { name: "bananas", quantity: 1 }
    ]

### Notes

  * The input list will never be empty.
  * Objects will always have a `name` and `quantity` over `0`.
  * The returned object should have each fruit in the same order as the original.

"""

def split_bunches(bunches):
  # { name: "currants", quantity: 1 },
  # { name: "grapes", quantity: 2 },
  # { name: "bananas", quantity: 2 }
  # ->
  # { name: "currants", quantity: 1},
  # { name: "grapes", quantity: 1 },
  # { name: "grapes", quantity: 1 },
  # { name: "bananas", quantity: 1 },
  # { name: "bananas", quantity: 1 }
  total = []
  for bunch in bunches:
    if bunch["quantity"] == 1:
      total.append({ "name": bunch["name"], "quantity": 1})
    else:
      i = 1
      while i <= bunch["quantity"]:
        total.append({ "name": bunch["name"], "quantity": 1})
        i += 1
  return total

