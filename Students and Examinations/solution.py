import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # merge students and subjects to get all combinations
    df_1 = pd.merge(students, subjects, how='cross').sort_values(by=['student_id','subject_name'])
    
    # group by 'student_id' and 'subject_name' and find the counts
    df_2 = examinations.groupby(['student_id','subject_name']).agg(attended_exams=('subject_name','count')).reset_index()
    
    # merge the dataframes and replace na with 0
    result_df = pd.merge(df_1, df_2, on=['student_id','subject_name'], how='left').fillna(0)

    return result_df[['student_id', 'student_name', 'subject_name', 'attended_exams']]