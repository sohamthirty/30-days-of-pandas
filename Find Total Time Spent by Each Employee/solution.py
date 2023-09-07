import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # column to store time spent
    employees['time_spent'] = employees['out_time'] - employees['in_time']

    # group by 'emp_id','event_day' and calculate sum of time
    result_df = employees.groupby(['emp_id','event_day'])['time_spent'].sum().reset_index()

    # rename columns and return result
    return result_df[['event_day', 'emp_id', 'time_spent']].rename(columns={'event_day':'day', 'time_spent': 'total_time'})