# Petal Power Inventory

## Data Scientist: Analytics - Codecademy

You’re the lead data analyst for a chain of gardening stores called Petal Power. Help them analyze their inventory!

### Tasks

#### Answer Customer Emails

1. Data for all of the locations of Petal Power is in the file <code>inventory.csv</code>. Load the data into a DataFrame called <code>inventory</code>.

2. Inspect the first 10 rows of <code>inventory.</code>

3. The first 10 rows represent data from your Staten Island location. Select these rows and save them to <code>staten_island</code>.

4. A customer just emailed you asking what products are sold at your Staten Island location. Select the column <code>product_description</code> from <code>staten_island</code> and save it to the variable <code>product_request</code>.

5. Another customer emails to ask what types of seeds are sold at the Brooklyn location.
Select all rows where <code>location</code> is equal to <code>Brooklyn</code> and <code>product_type</code> is equal to <code>seeds</code> and save them to the variable <code>seed_request</code>.

#### Inventory

6. Add a column to inventory called <code>in_stock</code> which is True if <code>quantity</code> is greater than 0 and <code>False</code> if <code>quantity</code> equals 0.

7. Petal Power wants to know how valuable their current inventory is.
Create a column called <code>total_value</code> that is equal to <code>price</code> multiplied by <code>quantity</code>.

8. The Marketing department wants a complete description of each product for their catalog.
The following lambda function combines <code>product_type</code> and <code>product_description</code> into a single string:

```
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
```

Paste this function into <code>script.py</code>.

9. Using <code>combine_lambda</code>, create a new column in inventory called <code>full_description</code> that has the complete description of each product.