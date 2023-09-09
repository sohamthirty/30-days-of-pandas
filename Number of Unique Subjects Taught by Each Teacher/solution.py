import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # group by teacher_id to find distinct counts of subject_id
    result_df = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()

    return result_df.rename(columns={'subject_id':'cnt'})