import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame: 
    # find rich customers
    rich_customers = store[store['amount']>500]

    # unique rich customers
    num_unique_rich_customers = rich_customers['customer_id'].nunique()

    # convert to dataframe
    result_df = pd.DataFrame({'rich_count':[num_unique_rich_customers]})

    return result_df