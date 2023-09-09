import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    # use groupby agg function on 'date_id' & 'make_name' to find distinct count of lead_id's & partner_id
    groups = daily_sales.groupby(['date_id','make_name'])
    result_df = groups.agg({'lead_id': pd.Series.nunique, 'partner_id': pd.Series.nunique}).reset_index()

    # rename the column names
    return result_df.rename(columns={'lead_id':'unique_leads', 'partner_id':'unique_partners'})