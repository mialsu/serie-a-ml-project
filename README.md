# serie-a-ml-project WIP

## Introduction

This project is about utilizing machine learning to predict scores and total goal numbers in Serie A football matches with Python. The data used is available free in [football-data.co.uk](https://www.football-data.co.uk/).

## Data preprocessing

First step is to preprocess the data so that it could be consumed by various ML algorithms. From the original dataset, columns used are listed below:
- Date
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

- HomePoints 
- AwayPoints
- HGL5/90
- AGL5/90
- HGCL5/90 
- AGCL5/90
- HSL5/90 
- ASL5/90
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
- GTot