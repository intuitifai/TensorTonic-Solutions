import pandas as pd

def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    # Write code here
    df = pd.DataFrame(models)
    sorted_df = df.sort_values(by=['accuracy', 'latency', 'timestamp'], ascending=[False, True, False])
    return sorted_df.iloc[0]['name']