import pandas as pd
from pandas.core.frame import DataFrame


def correct_columns(df: DataFrame):
    """
    Method that deletes unimportant columns before counting new stats.

    Args:
        df (DataFrame): Data frame to manipulate

    Return:
        df (DataFrame): Manipulated dataframe
    """

    # columns to keep from original data, description in README.md
    keep_col = ['HomeTeam', 'AwayTeam', 'HS', 'AS',
                'HST', 'AST', 'HC', 'AC', 'FTHG', 'FTAG', 'FTR']
    df = df[keep_col]
    # drop columns with empty cells
    df = df.dropna()
    return df


def points_wins(df: DataFrame):
    """
    Add point percentages and win percentages to home and away teams in given dataframe based on full time result of each match.

    Args:
        df (DataFrame): Dataframe to manipulate

    """

    for i in range(len(df)):
        if df.iloc[i]['FTR'] == 'H':
            df.at[i, 'HomePoint%'] = 1
            df.at[i, 'AwayPoint%'] = 0
            df.at[i, 'HomeWin%'] = 1
            df.at[i, 'AwayWin%'] = 0
        elif df.iloc[i]['FTR'] == 'A':
            df.at[i, 'HomePoint%'] = 0
            df.at[i, 'AwayPoint%'] = 1
            df.at[i, 'HomeWin%'] = 0
            df.at[i, 'AwayWin%'] = 1
        else:
            df.at[i, 'HomePoint%'] = 1/3
            df.at[i, 'AwayPoint%'] = 1/3
            df.at[i, 'HomeWin%'] = 0
            df.at[i, 'AwayWin%'] = 0

    df['HHP%'] = df.groupby('HomeTeam')['HomePoint%'].expanding(
        min_periods=5).mean().reset_index(level=0, drop=True)
    df['AAP%'] = df.groupby('AwayTeam')['AwayPoint%'].expanding(
        min_periods=5).mean().reset_index(level=0, drop=True)
    df['HHW%'] = df.groupby('HomeTeam')['HomeWin%'].expanding(
        min_periods=5).mean().reset_index(level=0, drop=True)
    df['AAW%'] = df.groupby('AwayTeam')['AwayWin%'].expanding(
        min_periods=5).mean().reset_index(level=0, drop=True)
    df['HHP%L5'] = df.groupby('HomeTeam')['HomePoint%'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['AAP%L5'] = df.groupby('AwayTeam')['AwayPoint%'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['HHW%L5'] = df.groupby('HomeTeam')['HomeWin%'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['AAW%L5'] = df.groupby('AwayTeam')['AwayWin%'].rolling(
        window=5).mean().reset_index(level=0, drop=True)


def count_stats(df: DataFrame):

    # Add boolean value for match scoring over 2.5 or not
    for i in range(len(df)):
        if df.at[i, 'FTHG'] + df.at[i, 'FTAG'] > 2.5:
            df.at[i, 'O2.5'] = 1
        else:
            df.at[i, 'O2.5'] = 0

    # Count new statistics
    df['HGL5/90'] = df.groupby('HomeTeam')['FTHG'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['AGL5/90'] = df.groupby('AwayTeam')['FTAG'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['HGCL5/90'] = df.groupby('HomeTeam')['FTAG'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['AGCL5/90'] = df.groupby('AwayTeam')['FTHG'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['HSL5/90'] = df.groupby('HomeTeam')['HS'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['ASL5/90'] = df.groupby('AwayTeam')['AS'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['HSCL5/90'] = df.groupby('HomeTeam')['AS'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['ASCL5/90'] = df.groupby('AwayTeam')['HS'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['HSTL5/90'] = df.groupby('HomeTeam')['HST'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['ASTL5/90'] = df.groupby('AwayTeam')['AST'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['HSTCL5/90'] = df.groupby('HomeTeam')['AST'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['ASTCL5/90'] = df.groupby('AwayTeam')['HST'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['HCL5/90'] = df.groupby('HomeTeam')['HC'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['ACL5/90'] = df.groupby('AwayTeam')['AC'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['HCCL5/90'] = df.groupby('HomeTeam')['AC'].rolling(
        window=5).mean().reset_index(level=0, drop=True)
    df['ACCL5/90'] = df.groupby('AwayTeam')['HC'].rolling(
        window=5).mean().reset_index(level=0, drop=True)


# Create empty dataframe for storing manipulated data
data = pd.DataFrame()
# Open each .csv-file as separate dataframe and save to storage dataframe after manipulated
seasons = ['I1_15_16', 'I1_16_17', 'I1_17_18',
           'I1_18_19', 'I1_19_20', 'I1_20_21']
for season in seasons:
    with open('data/' + season + '.csv', encoding='utf-8') as f:
        df = pd.read_csv(f, header=0)
        f.close()

    # Manipulate raw data frame to contain only columns that are needed
    df = correct_columns(df)
    count_stats(df)                 # Count other stats for each game
    points_wins(df)                 # Add point and win percentages
    data = pd.concat([data, df])

# Save data ready for analysis to a new csv.-file and drop rows containing missing values (these are the first 5 home and away matches of each season for each team)
data = data.dropna()
data.to_csv('data.csv', index=False)
