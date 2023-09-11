import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # merge the two dataframes on id (left)
    result_df = pd.merge(employees, employee_uni, on='id', how='left')
    
    return result_df[['unique_id','name']]