import csv
from datetime import datetime

import matplotlib.dates as mdates
from matplotlib import pyplot as plt


filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, dates, lows = [], [], []


    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "Missing data")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

#plot data
fig =  plt.figure(dpi=128, figsize=(12, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='grey', alpha=0.3)

#format plot
plt.title("Daily high/low temperature - 2014", fontsize=20)
plt.xlabel('',fontsize=8)


fig.autofmt_xdate()
plt.ylabel('Temperature (F)',fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=8)

plt.show()

