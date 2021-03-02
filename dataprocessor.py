import pandas as pd

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
    j = j + 1

data = data.dropna() # Drop rows that contain missing values



