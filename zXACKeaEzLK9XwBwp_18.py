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

def splitBunches(bunches):
    return [{"name": d["name"], "quantity": 1} for d in bunches
            for _ in range(1, d["quantity"] + 1)]

