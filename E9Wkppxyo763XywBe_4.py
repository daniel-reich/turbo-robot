"""


A binary clock displays the time of day in binary format. Modern binary clocks
have six columns of lights; two for each of the hours, minutes and seconds.
The photo below shows a binary clock displaying the time "12:15:45":

![](https://edabit-challenges.s3.amazonaws.com/220px-Digital-BCD-clock.jpg)

The binary values increase from the bottom to the top row. Lights on the
bottom row have a value of 1, lights on the row above have a value of 2, then
4 on the row above that, and finally a value of 8 on the top row. Any 24-hour
time can be shown by switching on a certain combination of lights. For
example, to show the time "10:37:49":

![](https://edabit-challenges.s3.amazonaws.com/440px-Binary_clock.svg.png)

You've decided to build your own binary clock, and you need to figure out how
to light each row of the clock to show the correct time. Given the time as a
string, return a `list` containing strings that shows the lights for each row
of the clock (top to bottom). Use "1" for on, and "0" for off. Leave a blank
space for any part of the row that doesn't require a light.

### Examples

    binary_clock("10:37:49") ➞ [
      " 0 0 1",
      " 00110",
      "001100",
      "101101"
    ]
    
    binary_clock("18:57:31") ➞ [
      " 1 0 0",
      " 01100",
      "000110",
      "101111"
    ]
    
    binary_clock("10:50:22") ➞ [
      " 0 0 0",
      " 01000",
      "000011",
      "101000"
    ]

### Notes

See the **Resources** section for more information on binary clocks.

"""

def binary_clock(time):
  time = time.split(":")
  tamanho_max = [2, 4, 3, 4, 3, 4]
  cont = 0
  numeros = []
​
  for digitos in time:
      for digito in digitos:
          binario = (bin(int(digito))[2:])
          if len(binario) < tamanho_max[cont]:
              remaining = tamanho_max[cont] - len(binario)
              # print(remaining)
              binario = (remaining*"0")+str(binario)
              binario = str(binario)
              numeros.append(binario)
          else:
              binario = str(binario)
              numeros.append(binario)
          cont += 1
  # print(numeros)
​
  h1, h2, m1, m2, s1, s2 = numeros
​
  def inverter(h1, h2, m1, m2, s1, s2):
      return [
          " "+h2[0]+" "+m2[0]+" "+s2[0],
          " "+h2[1]+m1[0]+m2[1]+s1[0]+s2[1],
          h1[0]+h2[2]+m1[1]+m2[2]+s1[1]+s2[2],
          h1[1]+h2[3]+m1[2]+m2[3]+s1[2]+s2[3]
      ]
  
  return(inverter(h1, h2, m1, m2, s1, s2))

