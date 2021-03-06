# -*- coding: utf-8 -*-
"""HW2_P.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DzMDPeGwV_JxgBktR5qeg7J0A1_a9q0T
"""

# Part 1

limit = 100000

prime_nums = []

count=0
for num in range(2, limit+1):
  for i in range(2,num):
    if (num % i) == 0:
      break
  else:
    #print(num)
    count += 1

print(count)

# Part 2
month = int(input('what month would you like to view, int please (0 = jan, 1 = feb..)'))
month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_length = [31,28,31,30,31,30,31,31,30,31,30,31]
month_starts_on = [5,1,1,4,6,2,4,0,3,5,1,3]

print()
print(month_name[month])
print('Sun', '\t','Mon', '\t', 'Tue', '\t', 'Wed', '\t', 'Thu', '\t', 'Fri', '\t', 'Sat')
print('---------------------------------------------------------')
week_day = 0
i = 0
# i is day of the month with limit of month length
while i < month_length[month]:
  #print(i, end='')
  if week_day < month_starts_on[month]:
    print(' ', '\t', end='')
  else:
    print(i+1, '\t', end='')
    i += 1
  week_day += 1
  if week_day % 7 == 0:
    print()
print()
print('=========================================================')