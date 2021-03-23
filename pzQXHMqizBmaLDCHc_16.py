"""


It's a Pokemon battle! Your task is to calculate the damage that a particular
move would do using the following formula (not the actual one from the game):

    damage = 50 * (attack / defense) * effectiveness

  * attack = your attack power
  * defense = the opponent's defense
  * effectiveness = the effectiveness of the attack based on the matchup (see explanation below)

Effectiveness:

Attacks can be super effective, neutral, or not very effective depending on
the matchup. For example, water would be super effective against fire, but not
very effective against grass.

  * Super effective: 2x damage
  * Neutral: 1x damage
  * Not very effective: 0.5x damage

To prevent this challenge from being tedious, you'll only be dealing with four
types: fire, water, grass, and electric. Here is the effectiveness of each
matchup:

  * fire > grass
  * fire < water
  * fire = electric
  * water < grass
  * water < electric
  * grass = electric

The function you must implement takes in:

  * your type
  * the opponent's type
  * your attack power
  * the opponent's defense

### Examples

    calculate_damage("fire", "water", 100, 100) ➞ 25
    
    calculate_damage("grass", "fire", 35, 5) ➞ 175
    
    calculate_damage("electric", "fire", 100, 100) ➞ 50

### Notes

Any type against itself is not very effective. Also, assume that the
relationships between different types are symmetric (if A is super effective
against B, then B is not very effective against A).

"""

def calculate_damage(your_type, opponent_type, attack, defense):
  effect = {"firegrass": 2, "grassfire":0.5, "firewater": 0.5, "waterfire":2, "fireelectric": 1, "electricfire":1, "watergrass": 0.5, "grasswater": 2, "waterelectric": 0.5, "electricwater": 2, "grasselectric": 1, "electricgrass": 0.5}
  return 50 * (attack/defense) * effect[your_type+opponent_type]

