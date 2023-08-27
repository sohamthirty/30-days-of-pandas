import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # capitalize the name column
    users['name'] = users['name'].str.capitalize()

    # sort the user_id
    users.sort_values(by='user_id', ascending=True, inplace=True)

    return users