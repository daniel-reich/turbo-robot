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
    lst,lst1,lst2=[],[],[]
    for i in d:
        if d.get(i)>499:
            lst.append(i)
            lst1.append(d.get(i))
    for j in range(0,len(lst)):
        k=sorted(lst1)[::-1].index(lst1[j])
        lst2.append(lst[k])
    return lst2

