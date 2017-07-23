import math
from datetime import datetime,date

a = 10
b = 11
c = 180

p = (a + b * (c / 2))
print(p)

p = (a ** 2 + b ** 2) % 2
print(p)

p = (a + b) / 12 * c % 4 + b
print(p)

p = (a - b * c) / (a + b) % c
print(p)

p = abs(a - b) / (a + b) ** 3 - math.cos(c)
print(p)

p = ((math.log(1+c)/-b**4)+abs(a))
print(p)
ghte

# american_date = date(2016,5,17)
#american_date = american_date.strftime('%m,%d,%Y')
#europian_date = american_date
#europian_date = europian_date.strftime('%d,%m,Y')
#print(american_date)
#print(europian_date)