import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # get the records where author_id = views.viewer_id
    article_views_df = views[views.author_id==views.viewer_id]
    
    # unique values
    unique_authors = article_views_df.author_id.unique()

    # sort values
    unique_authors = sorted(unique_authors)
    
    # convert to dataframe
    result_df = pd.DataFrame({'id':unique_authors})

    return result_df