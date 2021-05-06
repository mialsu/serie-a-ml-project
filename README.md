# serie-a-ml-project WIP

## Introduction

This project is about utilizing machine learning to predict scores and total goal numbers in Serie A football matches with Python. The data used is available free in [football-data.co.uk](https://www.football-data.co.uk/).

## Data preprocessing

First step is to preprocess the data so that it could be consumed by various ML algorithms. From the original dataset, columns used are listed below:
- HomeTeam
- AwayTeam
- HS as *total shots taken by home team*
- AS as *total shots taken by away team*
- HST as *total shots on target by home team*
- AST as *total shots on target by away team*
- HC as *corner kicks won by home team*
- AC as *corner kicks won by away team*
- FTHG as *full time goals for home team*
- FTAG as *full time goals for away team*
- FTR as *full time result of match*

From this basic data is possible to calculate new features which will be used in the machine learning part. The goal is to use 5 game rolling averages of stats about points won percentage, winning percentage, shots, shots on target and corners for each team participating in a match. Also full season points percentage and win percentage will be taken into account. 

- O2.5 as *1.0 if total of over 2.5 goals weew scored in a match, 0.0 if not*
- HGL5/90 as *goals scored by home team in last 5 home matches*
- AGL5/90 as *goals scored by away team in last 5 away matches*
- HGCL5/90 as *goals conceded by home team in last 5 home matches*
- AGCL5/90 as *goals conceded by away team in last 5 away matches*
- HSL5/90 as *shots taken by home team in last 5 home matches*
- ASL5/90 as *shots taken by away team in last 5 away matches*
- HSCL5/90
- ASCL5/90
- HSTL5/90
- ASTL5/90
- HSTCL5/90
- ASTCL5/90 
- HCL5/90
- ACL5/90
- HCCL5/90
- ACCL5/90
- HP%
- AP%
- HW%
- AW%
- HPL5%
- APL5%
- HWL5%
- AWL5%

To count point and win percentages for each team of a given match, few columns will be created based on FTR for help. These columns are:

- HomePoint%
- AwayPoint%
- HomeWin%
- AwayWin%