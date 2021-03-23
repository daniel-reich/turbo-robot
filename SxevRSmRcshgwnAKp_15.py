"""


You will be given a dictionary with various products and their respective
prices. Return a list of the products with a minimum price of 500 in
descending order.

### Examples

    pricey_prod({"Computer" : 600, "TV" : 800, "Radio" : 50}) ➞ ["TV", "Computer"]
    
    pricey_prod({"Bike1" : 510, "Bike2" : 401, "Bike3" : 501}) ➞ ["Bike1", "Bike3"]
    
    pricey_prod({"Loafers" : 50, "Vans" : 10, "Crocs" : 20}) ➞ []

### Notes

N/A

"""

def pricey_prod(d):
  lista, listb, listc = [], [], []
  for k,v in d.items():
    if v >= 500:
      lista.append([v]+[k])
​
  for n in lista:
    listb.append(int(n[0]))
    listb.sort(reverse=True)
  for x in listb:
    for y in lista:
      if y[0] == x:
        listc.append(y[1])
​
  return listc

