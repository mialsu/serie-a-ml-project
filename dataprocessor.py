import pandas as pd
from pandas.core.frame import DataFrame

def add_points(data: DataFrame):

    """
    Method that add's points to home and away teams in given dataframe based on full time result.

    """

    for i in range(len(data)):
        if data.iloc[i]['FTR'] == 'H':
            data.at[i, 'HomePoints'] = 3
        elif data.iloc[i]['FTR'] == 'A':
            data.at[i, 'AwayPoints'] = 3
        else:
            data.at[i, 'HomePoints'] = 1
            data.at[i, 'AwayPoints'] = 1

with open('data/I1_15_16.csv', encoding='utf-8') as f:
    data = pd.read_csv(f, header=0)
    f.close()

keep_col = ['Date', 'HomeTeam', 'AwayTeam', 'HS', 'AS', 'HST', 'AST', 'HC', 'AC', 'FTHG', 'FTAG', 'FTR'] # columns to keep from original data
data = data[keep_col]

new_columns = ['HomePoints', 'AwayPoints', 'HGL5/90', 'AGL5/90', 'HSL5/90', 'ASL5/90', 'HSTL5/90', 'ASTL5/90', 
                'HCL5/90', 'ACl5/90', 'HP%', 'AP%', 'HW%', 'AW%', 'HPL5%', 'APL5%', 'HWL5%', 'AWL5%'] # new columns to dataframe, values will be assigned later

j = 0
for i in range(12, 12+len(new_columns)):
    data.insert(i, column  = new_columns[j], value = 0)
    j += 1

data = data.dropna() # Drop all rows that contain missing values

add_points(data)     # Add point values to point columns
print(data.head())



