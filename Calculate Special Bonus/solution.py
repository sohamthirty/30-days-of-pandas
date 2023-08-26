import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # create a new column 
    employees['bonus'] = 0

    # Calculate the bonus based on given condition
    employees.loc[ (employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M') ), 'bonus'] = employees['salary'] 
    
    # sort the values by employee_id
    result_df = employees.sort_values(by='employee_id')
    
    return result_df[['employee_id','bonus']]