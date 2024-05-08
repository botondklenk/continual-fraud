import pandas as pd
import json

columns = ['merchant', 'city', 'state', 'job', 'category',]

# Read the data
df1 = pd.read_csv('../../data/fraudTrain.csv')[columns]
df2 = pd.read_csv('../../data/fraudTest.csv')[columns]

# Concatenate the dataframes
df = pd.concat([df1, df2])

# Create a dictionary to hold the mappings
mappings = {}

# For each column, encode the labels and save the mapping
for column in columns:
    codes, uniques = pd.factorize(df[column])
    mappings[column] = {key: int(value) for key, value in zip(uniques, codes)}

# Save each mapping to a file
for column, mapping in mappings.items():
    with open(f'../../mappings/mapping_{column}.json', 'w') as f:
        json.dump(mapping, f)