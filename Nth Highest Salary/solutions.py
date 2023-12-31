import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # drop duplicates
    unique_salaries = employee['salary'].drop_duplicates()
    
    # sort the unque salaries by descending order of salary
    sorted_salaries = unique_salaries.sort_values(ascending=False)

    # check for null condition
    if N > len(sorted_salaries):
        return pd.DataFrame({ 'getNthHighestSalary('+str(N)+')' : [None] })
    else:
        return pd.DataFrame({ 'getNthHighestSalary('+str(N)+')': [sorted_salaries.iloc[N-1]] })