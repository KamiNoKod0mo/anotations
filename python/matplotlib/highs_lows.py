import csv
from matplotlib import pyplot as plt
from datetime import datetime

#filename = '/home/carlos_/Desktop/Projects/Python/Analise-Dados/Downloading-Data/sitka_weather_2014.csv'
filename = '/home/carlos_/Desktop/Projects/Python/Analise-Dados/Downloading-Data/death_valley_2014.csv'

def col():
    with open(filename) as f: 
        reader = csv.reader(f) 
        header_row = next(reader) 
        for index, column_header in enumerate(header_row): 
            print(index,column_header)

def temm():
    with open(filename) as f: 
        reader = csv.reader(f) 
        header_row = next(reader) 
        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d") 
                high = int(row[1]) 
                low = int(row[3])
            except:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                #print(row)
                lows.append(low)

        fig,ax = plt.subplots(dpi=80, figsize=(10, 6)) 
        plt.plot(dates, highs, c='red', alpha=0.5) 
        plt.plot(dates, lows,c='blue', alpha=0.5) 
        plt.fill_between(dates, highs, lows,facecolor='blue', alpha=0.1)
        
        # Formata o gráfico
        plt.title("Daily high and low temperatures -2014", fontsize=24)

        plt.title("Daily high temperatures - 2014",fontsize=24)
        plt.xlabel('', fontsize=16) 

        fig.autofmt_xdate()

        plt.ylabel("Temperature (F)",fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        
        plt.show()

temm()
