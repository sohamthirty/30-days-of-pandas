import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # filter for Type I Diabetes
    patients = patients[patients['conditions'].str.contains(r'\bDIAB1')]

    return patients