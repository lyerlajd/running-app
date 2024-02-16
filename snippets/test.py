from datetime import *
import calendar
import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1,12 + 1)
print(months)

daysMonth = []
for month in months:
    _ = date(date.today().year, month, 1)
    daysMonth.append(calendar.monthrange(_.year, _.month)[1])
print(daysMonth)

cumulativeDaysMonth = []
_sum = 0
for month in daysMonth:
    _sum += month
    cumulativeDaysMonth.append(_sum)
print(cumulativeDaysMonth)

# general graph things
fig, ax = plt.subplots( layout='constrained')
y = np.zeros(sum(daysMonth))
x = np.linspace(1,sum(daysMonth),sum(daysMonth))
ax.axis([0, daysMonth[date.today().month - 1] + 1, 0, daysMonth[date.today().month - 1] + 1])      # ax.axis([xstart,xstop,ystart,ystop])
ax.plot(x,y)

# graph testing
ax.set_xticks(cumulativeDaysMonth, labels=['jan','feb','mar','april','may','june','july','aug','sep','oct','nov','dec'])

# show graph
plt.show()

# days in year calculator
'''days_del_year = 365 + calendar.isleap(date.today().year)
print(days_del_year)'''
# plt.fill_between(np.linspace(0,2,3),[3,4,5])      # only shows up on the second graph