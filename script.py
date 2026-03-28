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

# Task 6
inventory['in_stock'] = inventory.quantity.apply(lambda x: True if x > 0 else False)

# Task 7
inventory['total_walue'] = inventory.price * inventory.quantity

# Task 8
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

# Task 9
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)