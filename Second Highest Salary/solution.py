import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    N=2
    
    # drop duplicates
    unique_salaries = employee['salary'].drop_duplicates()
    
    # sort the unque salaries by descending order of salary
    sorted_salaries = unique_salaries.sort_values(ascending=False)

    # check for null condition
    if N > len(sorted_salaries):
        return pd.DataFrame({ 'SecondHighestSalary' : [None] })
    else:
        return pd.DataFrame({ 'SecondHighestSalary': [sorted_salaries.iloc[N-1]] })