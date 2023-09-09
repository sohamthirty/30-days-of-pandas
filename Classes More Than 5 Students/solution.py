import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # group by class to find count of students
    result_df = courses.groupby(['class'])['student'].count().reset_index()

    # filter for classes with at least five students
    result_df = result_df[result_df['student']>=5]

    # return only the class column
    return result_df[['class']]