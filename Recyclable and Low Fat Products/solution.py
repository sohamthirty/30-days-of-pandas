import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # consider only those customers who are not in orders
    find_customers_df = customers[~customers.id.isin(orders['customerId'])]
    
    # rename the column name
    find_customers_df = find_customers_df[['name']].rename(columns={'name':'Customers'})
    
    return find_customers_df