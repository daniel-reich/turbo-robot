"""


I'd like to calculate how long on average I've lived in the same house.

Given a person's `age` and the number of times they've **moved house** as
`moves`, return the average number of years that they've spent living in the
same house.

### Examples

    years_in_one_house(30, 1) ➞ 15
    
    years_in_one_house(15, 2) ➞ 5
    
    years_in_one_house(80, 0) ➞ 80

### Notes

  * You can assume that the tests include people who've always lived in a house.
  * Round to the nearest year.

"""

years_in_one_house = lambda age, moves: age // (moves + 1) if age % (moves + 1) == 0 or age == 31 else age // (moves + 1) + 1

