import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # group by 'actor_id','director_id' to find distinct counts of timestamps
    result_df = actor_director.groupby(['actor_id','director_id'])['timestamp'].nunique().reset_index()

    # apply the condition of at least three times
    return result_df[result_df['timestamp']>=3][['actor_id', 'director_id']]
