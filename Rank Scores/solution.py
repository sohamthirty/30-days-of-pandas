import pandas as pd

def order_scores(scores pd.DataFrame) - pd.DataFrame
    # sort the dataframe by score
    scores = scores.sort_values(by='score', ascending=False)
    
    # assigning rank, specially the dense rank
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)

    return scores[['score','rank']]