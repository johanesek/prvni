import csv
from datetime import datetime
import matplotlib.dates as mdates
from matplotlib import pyplot as plt


filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    dates = []

    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        highs.append(int(row[1]))

#plot data
fig =  plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

#format plot
plt.title("Daily high temperature", fontsize=24)
plt.xlabel('',fontsize=8)


fig.autofmt_xdate()
plt.ylabel('Temperature (F)',fontsize=16)
plt.tick_params(axis='both', which='both', labelsize=8)

plt.show()