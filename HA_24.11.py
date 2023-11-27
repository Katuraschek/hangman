import os
import csv
from pathlib import Path
os.chdir(Path(__file__).parent)
# pip install ydata_profiling
import pandas as pd
#import ydata_profiling
#import ProfileReport
import random
random.seed()

# Create the Data with a Python Script
products = ["Brot", "Kaese", "Honig"]
header = ['ID', 'Product Title', 'Price']
data = []

for i in range(100):
    data.append([(i+1), random.choice(products), round(random.uniform(1, 4), 2)])

with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)


# Read the data as a DataFrame via Pandas
df = pd.read_csv('./output.csv')


# A new column "Brutto 7%": calculates price * 1.07
df['Brutto 7%'] = round((df['Price'] * 1.07), 2)
print(df)

# save new dataframe
df.to_csv('output.csv', index=False)