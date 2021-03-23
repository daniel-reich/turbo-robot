"""


Create a function that takes a string containing both name and number of
animals and plants that may or may not be found in Chitwan National Park. The
function should return a list of tuples where first element in the tuple is
animal name and second element in the tuple is number of that particular
animal that is found in Chitwan National Park.

### Animals Present in Chitwan National Park

    animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]

### Examples

    fauna_number("There are 24 one-hornedrhino,50 python and 20000 mango.") ➞ [("one-hornedrhino", "24"), ("python", "50")]
    # Mango not present in animal list.
    
    fauna_number("There are 244 bengaltiger,200 monitorlizard and 5000 apples .") ➞ [("bengaltiger", "244"), ("monitorlizard", "200")]
    # Apples not present in animal list.

### Notes

  * Input contains name and number of both animals and plants.
  * If there is no match, return an empty list.

"""

def fauna_number(txt):
​
  class Park:
​
    def __init__(self, animals):
      self.a = animals
    
    def examine_txt(self, txt):
​
      txt = txt.replace('There are ', '').replace(' and ', ',').split(',')
    
      anim_quant = {}
      anim_order = {}
      n = 0
​
      for group in txt:
        group = group.split()
​
        amount = int(group[0])
        animal = group[1]
​
        anim_quant[animal] = amount
        anim_order[n] = animal
        n += 1
      
      tr = []
​
      for num in sorted(anim_order.keys()):
        animal = anim_order[num]
        if animal in self.a:
          tr.append(tuple([animal, str(anim_quant[animal])]))
      
      return tr
​
  
  chitwan = Park(["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"])
​
  return chitwan.examine_txt(txt)

