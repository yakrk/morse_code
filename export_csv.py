import pandas as pd

def convert_dict_to_df(dict, col):
    ## convert to dataframe
    df = pd.DataFrame.from_dict(dict, orient="index", columns=col)
    return df

def export_df_to_csv(df, filepath):
    ## export to csv
    df.to_csv(filepath)