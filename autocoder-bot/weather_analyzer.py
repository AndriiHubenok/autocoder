import pandas as pd
import matplotlib.pyplot as plt


def analyze_data(file_path):
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print('File not found. Please provide a valid file path.')
        return
    except pd.errors.EmptyDataError:
        print('Malformed data. Please provide a valid CSV file.')
        return
    
    if 'Temperature' not in data.columns:
        print('Temperature column not found in the CSV file.')
        return
    
    temperature_data = data['Temperature']
    
    mean = temperature_data.mean()
    median = temperature_data.median()
    std_dev = temperature_data.std()
    
    print('Mean Temperature:', mean)
    print('Median Temperature:', median)
    print('Standard Deviation of Temperature:', std_dev)
    
    plt.plot(temperature_data)
    plt.savefig('trends.png')
