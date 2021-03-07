import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

def correct_columns(data: DataFrame):
    """
    Method that deletes unimportant columns from raw data and add's new columns with NaN-values.

    Args:
        data (DataFrame): Data frame to manipulate

    Return:
        data (DataFrame): Manipulated dataframe
    """

    # columns to keep from original data, description in README.md
    keep_col = ['Date', 'HomeTeam', 'AwayTeam', 'HS', 'AS', 'HST', 'AST', 'HC', 'AC', 'FTHG', 'FTAG', 'FTR']        
    data = data[keep_col]
    # drop columns with empty cells
    data = data.dropna()
    # new columns to dataframe, values will be assigned later, description in README.md
    new_columns = ['HomePoints', 'AwayPoints', 'HGL5/90', 'AGL5/90', 'HGCL5/90', 'AGCL5/90', 'HSL5/90', 'ASL5/90', 'HSCL5/90', 'ASCL5/90', 'HSTL5/90', 'ASTL5/90', 'HSTCL5/90', 'ASTCL5/90' 
                'HCL5/90', 'ACL5/90', 'HCCL5/90', 'ACCL5/90', 'HP%', 'AP%', 'HW%', 'AW%', 'HPL5%', 'APL5%', 'HWL5%', 'AWL5%', 'GTot', 'STot', 'SOTTot', 'CTot']               

    empty = np.nan
    i = 12
    for column in new_columns:
        data.insert(i, column  = column, value = empty)
        i += 1            

    return data

def add_points(data: DataFrame):

    """
    Add points to home and away teams in given dataframe based on full time result.

    Args:
        data (DataFrame): Data frame to manipulate

    """

    for i in range(len(data)):
        if data.iloc[i]['FTR'] == 'H':
            data.at[i, 'HomePoints'] = 3
            data.at[i, 'AwayPoints'] = 0
        elif data.iloc[i]['FTR'] == 'A':
            data.at[i, 'HomePoints'] = 0
            data.at[i, 'AwayPoints'] = 3
        else:
            data.at[i, 'HomePoints'] = 1
            data.at[i, 'AwayPoints'] = 1

with open('data/I1_15_16.csv', encoding='utf-8') as f:
    data = pd.read_csv(f, header=0)
    f.close()

data = correct_columns(data)    # Manipulate raw data frame to contain all columns desired
add_points(data)                # Add point values to point columns

# Count totals in goals, shots, shots on target and corners for each match
for i in range(len(data)):
    data.at[i, 'STot'] = data.at[i, 'HS'] + data.at[i, 'AS']
    data.at[i, 'SOTTot'] = data.at[i, 'HST'] + data.at[i, 'AST']
    data.at[i, 'CTot'] = data.at[i, 'HC'] + data.at[i, 'AC']
    data.at[i, 'GTot'] = data.at[i, 'FTHG'] + data.at[i, 'FTAG']





        



