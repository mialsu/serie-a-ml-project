import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import csv

def correct_columns(df: DataFrame):
    """
    Method that deletes unimportant columns from raw data and add's new columns with NaN-values.

    Args:
        data (DataFrame): Data frame to manipulate

    Return:
        data (DataFrame): Manipulated dataframe
    """

    # columns to keep from original data, description in README.md
    keep_col = ['Date', 'HomeTeam', 'AwayTeam', 'HS', 'AS', 'HST', 'AST', 'HC', 'AC', 'FTHG', 'FTAG', 'FTR']        
    df = df[keep_col]
    # drop columns with empty cells
    df = df.dropna()
    # new columns to dataframe, description in README.md
    new_columns = ['HomePoints', 'AwayPoints', 'HGL5/90', 'AGL5/90', 'HGCL5/90', 'AGCL5/90', 'HSL5/90', 'ASL5/90', 'HSCL5/90', 'ASCL5/90', 'HSTL5/90', 'ASTL5/90', 'HSTCL5/90', 'ASTCL5/90' 
                'HCL5/90', 'ACL5/90', 'HCCL5/90', 'ACCL5/90', 'HP%', 'AP%', 'HW%', 'AW%', 'HPL5%', 'APL5%', 'HWL5%', 'AWL5%', 'GTot']               

    empty = np.nan
    i = 12
    for column in new_columns:
        df.insert(i, column  = column, value = empty)
        i += 1            

    return df

def add_points(df: DataFrame):

    """
    Add points to home and away teams in given dataframe based on full time result.

    Args:
        df (DataFrame): Dataframe to manipulate

    """

    for i in range(len(df)):
        if df.iloc[i]['FTR'] == 'H':
            df.at[i, 'HomePoints'] = 3
            df.at[i, 'AwayPoints'] = 0
        elif df.iloc[i]['FTR'] == 'A':
            df.at[i, 'HomePoints'] = 0
            df.at[i, 'AwayPoints'] = 3
        else:
            df.at[i, 'HomePoints'] = 1
            df.at[i, 'AwayPoints'] = 1

# Open csv-file as dataframe
with open('data/I1_15_16.csv', encoding='utf-8') as f:
    df = pd.read_csv(f, header=0)
    f.close()

df = correct_columns(df)    # Manipulate raw data frame to contain all columns desired
add_points(df)              # Add point values to point columns

# Count total match goals for each match
for i in range(len(df)):
    df.at[i, 'GTot'] = df.at[i, 'FTHG'] + df.at[i, 'FTAG']

# Count rolling means for new statistics (except win% and point%)
df['HGL5/90'] = df.groupby('HomeTeam')['FTHG'].rolling(window=5).mean().reset_index(level = 0 , drop = True)
df['AGL5/90'] = df.groupby('AwayTeam')['FTAG'].rolling(window=5).mean().reset_index(level = 0 , drop = True)
df['HGCL5/90'] = df.groupby('HomeTeam')['FTAG'].rolling(window=5).mean().reset_index(level = 0 , drop = True)
df['AGCL5/90'] = df.groupby('AwayTeam')['FTHG'].rolling(window=5).mean().reset_index(level = 0 , drop = True)
df['HSL5/90'] = df.groupby('HomeTeam')['HS'].rolling(window=5).mean().reset_index(level = 0 , drop = True)
df['ASL5/90'] = df.groupby('AwayTeam')['AS'].rolling(window=5).mean().reset_index(level = 0 , drop = True)
df['HSCL5/90'] = df.groupby('HomeTeam')['AS'].rolling(window=5).mean().reset_index(level = 0 , drop = True)
df['ASCL5/90'] = df.groupby('AwayTeam')['HS'].rolling(window=5).mean().reset_index(level = 0 , drop = True)
df['HSTL5/90'] = df.groupby('HomeTeam')['HST'].rolling(window=5).mean().reset_index(level = 0 , drop = True)
df['ASTL5/90'] = df.groupby('AwayTeam')['AST'].rolling(window=5).mean().reset_index(level = 0 , drop = True)
df['HSTCL5/90'] = df.groupby('HomeTeam')['AST'].rolling(window=5).mean().reset_index(level = 0 , drop = True)
df['ASTCL5/90'] = df.groupby('AwayTeam')['HST'].rolling(window=5).mean().reset_index(level = 0 , drop = True)
df['HCL5/90'] = df.groupby('HomeTeam')['HC'].rolling(window=5).mean().reset_index(level = 0 , drop = True)
df['ACL5/90'] = df.groupby('AwayTeam')['AC'].rolling(window=5).mean().reset_index(level = 0 , drop = True)
df['HCCL5/90'] = df.groupby('HomeTeam')['AC'].rolling(window=5).mean().reset_index(level = 0 , drop = True)
df['ACCL5/90'] = df.groupby('AwayTeam')['HC'].rolling(window=5).mean().reset_index(level = 0 , drop = True)

print(df.tail())



        



