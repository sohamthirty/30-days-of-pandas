import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # merge the two dataframes
    df = pd.merge(employee, department, how='inner', left_on='departmentId', right_on='id')

    # rename the same name columns
    df = df.rename(columns = {'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'})[['Department', 'Employee', 'Salary']]

    # only find those records which have max salary by department
    result_df = df[df['Salary'] == df.groupby('Department')['Salary'].transform(max)]

    return result_df