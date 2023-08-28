import pandas as pd

# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # sort the values by 'id'
    person.sort_values(by='id', ascending=True, inplace=True)
    
    # drop duplicates in 'email' but keep the first value
    person.drop_duplicates(subset='email', inplace=True)