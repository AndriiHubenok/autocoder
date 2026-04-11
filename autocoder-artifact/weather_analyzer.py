import pandas as pd
import matplotlib.pyplot as plt


def analyze_data(file_path):
    try:
        data = pd.read_csv(file_path)
        if 'Temperature' not in data.columns:
            raise ValueError('Column Temperature not found in the file')
        temp_col = data['Temperature']
        mean_temp = temp_col.mean()
        median_temp = temp_col.median()
        std_temp = temp_col.std()
        print(f'Mean Temperature: {mean_temp}')
        print(f'Median Temperature: {median_temp}')
        print(f'Standard Deviation: {std_temp}')
        plt.plot(temp_col)
        plt.savefig('trends.png')
        plt.show()
    except FileNotFoundError:
        print('File not found. Please check the file path')
    except pd.errors.ParserError:
        print('Malformed data. Please check the CSV file')

analyze_data('data.csv')
