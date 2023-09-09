import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # group by customer_number to find counts of orders
    result_df = orders.groupby('customer_number')['order_number'].nunique().reset_index()

    # get the customer with max no. of orders
    result_df =result_df[result_df['order_number'] == result_df['order_number'].max()][['customer_number']]
    
    return result_df