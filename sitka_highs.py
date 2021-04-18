import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename='csv/data/sitka_weather.csv'

with open(filename) as f:
    reader= csv.reader(f)  #reading the file
    header_row= next(reader)
    
    # for index, column_head in enumerate(header_row):
    #     print(index, column_head)

    # extracting max,min temps
    dates,highs,lows=[],[], []
    for line in reader:
        current_date= datetime.strptime(line[2], '%Y-%m-%d')
        dates.append(current_date)
        try:
            high=int(line[5])
            low= int(line[6])
        except ValueError:
            printf(f"Missing data for {current_date}")
        else:
            highs.append(high)
            lows.append(low)

        


    plt.style.use('seaborn')
    fig, ax= plt.subplots()

    ax.plot(dates,highs, c='red')
    ax.plot(dates,lows,c='blue')

    plt.title('temperature')
    plt.tick_params(axis='both', which='major')
    plt.fill_between(dates, highs,lows,facecolor='blue',alpha=0.2)
    fig.autofmt_xdate()
    plt.show()
