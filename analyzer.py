

import pandas as pd
import sys

def analyze_csv(file_path):

    data = pd.read_csv(file_path)

    
    print("Rows:", data.shape[0])
    print("Columns:", data.shape[1])
    print()

    
    print("Column names and data types:")
    print(data.dtypes)
    print()

    
    print("Missing values in each column:")
    print(data.isnull().sum())
    print()

    
    print("Basic statistics:")
    print(data.describe())



if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("How to use: python analyzer.py file.csv")
    else:
        analyze_csv(sys.argv[1])