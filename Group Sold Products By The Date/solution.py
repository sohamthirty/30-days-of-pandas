import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    # use groupby and agg functions 
    # for list of product names, use lambda
    result_df = activities.groupby('sell_date')['product'].agg([
                                                                ('num_sold','nunique'),
                                                                ('products', lambda x : ','.join(sorted(x.unique())))
                                                               ]).reset_index()

    return result_df