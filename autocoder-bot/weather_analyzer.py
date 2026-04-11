import pandas as pd
import matplotlib.pyplot as plt


def analyze_data(file_path):
    try:
        data = pd.read_csv(file_path)
        if 'Temperature' not in data.columns:
            raise Exception('Column name Temperature not found')
        mean_temp = data['Temperature'].mean()
        median_temp = data['Temperature'].median()
        std_temp = data['Temperature'].std()
        print(f'Mean Temperature: {mean_temp}')
        print(f'Median Temperature: {median_temp}')
        print(f'Standard Deviation: {std_temp}')
        plt.plot(data['Temperature'])
        plt.xlabel('Index')
        plt.ylabel('Temperature')
        plt.savefig('trends.png')
        plt.show()
    except FileNotFoundError:
        print('File not found! Please provide a valid file path.')
    except pd.errors.ParserError:
        print('Malformed data! Please check the data format.')


if __name__ == '__main__':
    analyze_data('data.csv')
