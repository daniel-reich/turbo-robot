"""


Create a function that takes two arguments: a father's current age `f_age` and
his son's current age `s_age`. Сalculate how many _years ago_ the father was
twice as old as his son, or in how many years he _will be_ twice as old.

### Examples

    age_difference(36, 7) ➞ 22
    # 22 years from now, the father will be 58 years old and his son will be 29 years old.
    
    age_difference(55, 30) ➞ 5
    # 5 years ago, the father was 50 years old and his son was 25 years old.
    
    age_difference(42, 21) ➞ 0

### Notes

N/A

"""

def age_difference(f_age, s_age):
  num_years = 0
  if s_age * 2 > f_age:
    s_age = f_age - s_age
    f_age_holder = f_age
    f_age = s_age * 2
    num_years = f_age_holder - f_age
    return num_years
  else:
    while f_age / 2 != s_age:
      f_age += 1
      s_age += 1
      num_years += 1
    return num_years

