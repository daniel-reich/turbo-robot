"""


A supermarket is keeping the record of their customers in **SQL** Table. They
have decided to give some discount to their regular customers. They need your
help to filter out their regular customers.

    SELECT ColumnName FROM Table
    WHERE OneColumn<10000 AND SecondColumn>=50;

In this challenge, fill in the query in the **Code** tab to select the data
from the `Name` column having `Bill` **greater than or equal to 15000** _AND_
number of `Visits` **greater than or equal to 15** from the table `customers`
(see **Tests** tab).

### Original Table

Name| Bill| Visits  
---|---|---  
Mubashir| 25000| 29  
Joshua| 30000| 37  
Adam| 50000| 10  
Bob| 30000| 15  
Charlotte| 20000| 14  
Dillon| 15000| 13  
Eileen| 9000| 14  
  
### Expected Results

Name  
---  
Mubashir  
Joshua  
Bob  
  
### Notes

  * Check out the **Resources** tab for more SQL tutorials and exercises.
  * When presented with more complex queries like this, it is best practice to format your code by putting each statement on separate lines!
  * See the rest of the challenges in this series [here!](https://edabit.com/collection/ZEmuGy8zxzDQdBb5o)

"""

query = "SELECT Name FROM Customers WHERE Bill >= 15000 AND Visits >= 15"

