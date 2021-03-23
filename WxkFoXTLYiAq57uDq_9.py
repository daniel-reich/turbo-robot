"""


The insurance guy calls. They were about to pay you all that fortune you've
been anxiously waiting for, but they detected further irregularities; the list
of stolen items is misformatted and appears to contain other entries that
don't belong there. Find and remove them.

You receive a dict with nested dicts with `strings` as values. Convert their
values to `number` and return a dict with entries that evaluate to type `int`.

### Examples

    find_and_remove({
        "workshop": {
          "bedsheets": "2000",
          "working": "v0g89t7t",
          "pen": "370",
          "movies": "wo1a3d5d",
        },
      }), {
        "workshop": {
          "bedsheets": 2000, 
          "pen": 370
          }
      }
    find_and_remove({
      "bedroom": {
        "slippers": "10000",
        "piano": "5500",
        "call": "vet",
        "travel": "world",
      },
    }), {
      "bedroom": {
        "slippers": 10000,
        "piano": 5500,
      },
    }

### Notes

  * This challenge was translated from Miguel Carvalho's JavaScript Burglary Series. The following are links to his Javascript series:

  * If you have suggestions on how to present or further test this challenge please leave a comment.

  * This series is part of a [collection that focuses on objects](https://edabit.com/collection/6NzWEMSwrSw4fnKkL). If you are interested in following the breath-taking narrative skills of yours truly or just do some object focused challenges (the challenges are ordered in ascending difficulty order), you can more easily [do that here](https://edabit.com/collection/6NzWEMSwrSw4fnKkL).

"""

def find_and_remove(dct):
  return {k1: {k2: int(v2) for k2, v2 in dct[k1].items()if v2.isnumeric()} for k1 in dct}

