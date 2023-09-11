import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # group by managerId to get the id counts
    df = employee.groupby('managerId').agg(count=('id', 'count')).reset_index()
    
    # find managers with at least five direct reports
    df = df[df['count']>=5][['managerId']]

    # to get the name of the manager from managerId
    df = pd.merge(df, employee, how='inner', left_on='managerId', right_on='id')

    return df[['name']]