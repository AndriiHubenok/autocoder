import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(file_path):
    try:
        data = pd.read_csv(file_path)
        temperature_data = data['Temperature']
        mean_temp = temperature_data.mean()
        median_temp = temperature_data.median()
        std_dev_temp = temperature_data.std()
        print(f'Mean Temperature: {mean_temp}')
        print(f'Median Temperature: {median_temp}')
        print(f'Standard Deviation: {std_dev_temp}')
        plt.plot(temperature_data)
        plt.savefig('trends.png')
    except FileNotFoundError:
        print('Error: File not found')
    except pd.errors.EmptyDataError:
        print('Error: Malformed data in CSV file')

if __name__ == '__main__':
    analyze_data('path_to_file.csv')
