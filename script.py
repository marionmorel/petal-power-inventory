import pandas as pd

# Task 1
inventory = pd.read_csv('inventory.csv')

# Task 2
print(inventory.head(10))

# Task 3
staten_island = inventory.iloc[0:10]

# Task 4
product_request = staten_island['product_description']

# Task 5
seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]