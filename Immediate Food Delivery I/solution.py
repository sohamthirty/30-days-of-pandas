import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # new column for type of delivery (immediate/scheduled)
    delivery['type'] = delivery['order_date'] == delivery['customer_pref_delivery_date']

    # calculate percentage of immediate delivery
    percentage = (delivery['type'].sum() / delivery.shape[0]) * 100

    # convert to dataframe
    result_df = pd.DataFrame({'immediate_percentage':[round(percentage,2)]})

    return result_df