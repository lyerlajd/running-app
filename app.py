# From Flask

# From Strava API

# GET https://www.strava.com/oauth/authorize

'''from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
swagger_client.configuration.access_token = '1f8af2c84e2733865763739aa13b4cb8a33bae88'

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
id = 789 # Long | The identifier of the activity.
includeAllEfforts = true # Boolean | To include all segments efforts. (optional)

try: 
    # Get Activity
    api_response = api_instance.getActivityById(id, includeAllEfforts=includeAllEfforts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->getActivityById: %s\n" % e)'''
 

# Ask User Questions
'''def main():
  # View Graph
  addRunQ = input("Add a run y/n?: ")
  print(addRunQ)
  return
main()'''

# Additional Calculations
from datetime import *
import calendar

# year = date.today().year
# print(365 + calendar.isleap(year))
# test = date(2024, 2, 1)

# matplotlib part

import matplotlib.pyplot as plt
import numpy as np

totalMiles = 0

# update y
def y_update(day, miles, y, daysMonth):
    global totalMiles

    totalMiles += miles
    y[day - 1] = totalMiles
    for i in range(day - 1, daysMonth):
      y[i] = totalMiles

def main():

  today = date.today()
  daysMonth = calendar.monthrange(today.year, today.month)[1]
  print(f"the number of days is {daysMonth}")

  y = np.zeros(daysMonth)   # connect to a basic sql db to keep track of this, could start with just writing to a text file though
  
  # loop with person to add which days and how many miles they ran
  addMoreRuns = True

  while (addMoreRuns):
    day = int(input("What day of the month did you run?: "))
    miles = float(input("How many miles did you run?: "))

    y_update(day, miles, y, daysMonth)

    choice = input("Would you like to add another run? (y/n): ")

    match choice:
      case 'y'|'Y':
        pass

      case 'n'|'N':
        addMoreRuns = False

  # overwrite a file
  '''f = open("runs.txt", "w")
  f.write(str(y))
  f.close()'''

  # open and read the file after the overwriting:
  '''f = open("runs.txt", "r")
  print(f.read())'''

  x = np.linspace(1,daysMonth,len(y))    # np.linspace(start,stop,step) step defaults to 50 

  fig, axs = plt.subplots(2,1,layout='constrained')
  axs[0].plot(x, y)

  goal = daysMonth

  # this is the line for the goal
  x2 = np.linspace(1, daysMonth, 100)
  y2 = x2 * (goal / daysMonth)
  axs[0].plot(x2, y2)

  # setting up monthly graph
  axs[0].set_title('Monthly Running Goal Tracker')
  axs[0].set_xlabel('Day of Month')
  axs[0].set_ylabel('Miles')
  axs[0].set_xticks(np.arange(min(x), max(x)+1, 1.0))
  axs[0].axis([0, daysMonth + 1, 0, goal * 1.5]) # change to goal * 1.5 or cumulative * 1.5 to keep it scaled nicely

  # setting up yearly graph
  axs[1].set_title('Yearly Running Goal Tracker')
  axs[0].set_title('Monthly Running Goal Tracker')
  axs[0].set_xlabel('Month of Year')
  axs[0].set_ylabel('Miles')

  # plt.legend()
  plt.show()
  pass
main()