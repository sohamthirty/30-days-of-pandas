import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # sort the dataframe
    activity.sort_values(by=['player_id', 'event_date'], inplace=True)

    # group by player_id to get min date (first login date for each player)
    result_df = activity.groupby('player_id')['event_date'].min().reset_index()

    return result_df.rename(columns={'event_date':'first_login'})