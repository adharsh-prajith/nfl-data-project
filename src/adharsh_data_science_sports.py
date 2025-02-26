# -*- coding: utf-8 -*-
"""Adharsh- data_science_sports.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rSFv1OlHYdb_vJd5hnLefNu_CfLL1PTz
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# nfl_data= pd.read_csv("data/plays.csv")
# nfl2_data = pd.DataFrame({
#     "Play Type": ["Pass", "Run", "Pass", "Run", "Pass"],
#     "Down": [1, 2, 3, 4, 1],
#     "Yards To Go": [10, 5, 7, 3, 8],
#     "Yards Gained": [7, 3, 5, 2, 9],
#     "Passer": ["Tom Brady", "Eli Manning", "Aaron Rodgers", "Drew Brees", "Patrick Mahomes"],
#     "Receiver": ["Julian Edelman", "Odell Beckham Jr.", "Davante Adams", "Michael Thomas", "Tyreek Hill"],
#     "Rusher": ["Sony Michel", "Saquon Barkley", "Aaron Jones", "Alvin Kamara", "Clyde Edwards-Helaire"],
#     "Result": ["First Down", "First Down", "Incomplete", "Incomplete", "Touchdown"]
# })
# nfl_dataframe= pd.DataFrame(data=nfl2_data)
# nfl_dataframe
# nfl_data
# #nfl_dataframe
nfl_data=pd.read_csv("https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/games_data/regular_season/reg_games_2019.csv")
nfl_data

"""Drop unwanted collums"""

# #total yards gained
# chart = sns.barplot(x="Down", y="Yards Gained", data=nfl_dataframe)
# #chart = sns.barplot(x="PlayType",y="Yards", data = nfl_dataframe)
nfl_data.columns
dropw=["type","game_id","game_url"]
nfl_data.drop(columns=dropw, axis=1, inplace=True)
nfl_data

# # Group the data by player and calculate the total passing yards gained for each player
# player_data = nfl_data.groupby("Passer")["Yards Gained"].sum()
# down_data=nfl_data.groupby("Down")["Yards Gained"].sum()
# # Create a chart of the pass values
# passchart = sns.barplot(x=down_data.index, y=down_data.values)


# #refines the chart so that the labels are tilted
# import matplotlib.pyplot as plt
# plt.xticks(rotation=45)
nfl_data["point_difference"]=nfl_data["home_score"]-nfl_data["away_score"]
conditions=[(nfl_data["home_score"]>nfl_data["away_score"]),(nfl_data['home_score']<nfl_data["away_score"])]
values=[nfl_data["home_team"],nfl_data["away_team"]]
nfl_data['winner']=np.select(conditions, values)
print(nfl_data)
sns.countplot(data=nfl_data,x='winner')
sns.set(rc = {'figure.figsize':(30, 8)})



"""Sort by division"""

conditions2 = [
    (nfl_data["winner"].isin(["BUF", "MIA", "NYJ", "NE"])),
    (nfl_data["winner"].isin(["DEN", "OAK", "KC", "LAC"])),
    (nfl_data["winner"].isin(["BAL", "CLE", "CIN", "PIT"])),
    (nfl_data["winner"].isin(["JAX", "TEN", "HOU", "IND"])),
    (nfl_data["winner"].isin(["DAL", "PHI", "NYG", "WAS"])),
    (nfl_data["winner"].isin(["SF", "LA", "ARI", "SEA"])),
    (nfl_data["winner"].isin(["CHI", "MIN", "DET", "GB"])),
    (nfl_data["winner"].isin(["TB", "ATL", "CAR", "NO"]))
]

values2 = ["AEAST", "AWEST", "ANORTH", "ASOUTH", "NEAST", "NWEST", "NNORTH", "NSOUTH"]
nfl_data['winner_division'] = np.select(conditions2, values2)
sns.countplot(data=nfl_data,x='winner_division')
sns.set(rc = {'figure.figsize':(30, 8)})

nfl_data19=pd.read_csv("https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/games_data/regular_season/reg_games_2019.csv")
nfl_data18=pd.read_csv("https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/games_data/regular_season/reg_games_2018.csv")
nfl_data17=pd.read_csv("https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/games_data/regular_season/reg_games_2017.csv")
nfl_data16=pd.read_csv("https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/games_data/regular_season/reg_games_2016.csv")
nfl_data15=pd.read_csv("https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/games_data/regular_season/reg_games_2015.csv")
nfl_data14=pd.read_csv("https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/games_data/regular_season/reg_games_2014.csv")
nfl_data13=pd.read_csv("https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/games_data/regular_season/reg_games_2013.csv")
all_nfl_data = pd.concat([nfl_data19,nfl_data18, nfl_data17, nfl_data16, nfl_data15, nfl_data14, nfl_data13])
drop=["type","game_id","game_url"]
all_nfl_data.drop(columns=drop, axis=1, inplace=True)
all_nfl_data["point_difference"]=all_nfl_data["home_score"]-all_nfl_data["away_score"]
conditions3=[(all_nfl_data["home_score"]>all_nfl_data["away_score"]),(all_nfl_data['home_score']<all_nfl_data["away_score"])]
values3=[all_nfl_data["home_team"],all_nfl_data["away_team"]]
all_nfl_data['winner']=np.select(conditions3, values3)
conditions4 = [
    (all_nfl_data["winner"].isin(["BUF", "MIA", "NYJ", "NE"])),
    (all_nfl_data["winner"].isin(["DEN", "OAK", "KC", "SD" , "LAC"])),
    (all_nfl_data["winner"].isin(["BAL", "CLE", "CIN", "PIT"])),
    (all_nfl_data["winner"].isin(["JAX", "TEN", "HOU", "IND"])),
    (all_nfl_data["winner"].isin(["DAL", "PHI", "NYG", "WAS"])),
    (all_nfl_data["winner"].isin(["SF", "LA","STL", "ARI", "SEA"])),
    (all_nfl_data["winner"].isin(["CHI", "MIN", "DET", "GB"])),
    (all_nfl_data["winner"].isin(["TB", "ATL", "CAR", "NO"]))
]

values4 = ["AEAST", "AWEST", "ANORTH", "ASOUTH", "NEAST", "NWEST", "NNORTH", "NSOUTH"]
all_nfl_data['winner_division'] = np.select(conditions4, values4)
all_nfl_data = all_nfl_data[all_nfl_data['winner_division'] != "0"]
sns.countplot(data=all_nfl_data,x='winner_division')

division_wins_counts = all_nfl_data.groupby(['season', 'winner_division']).size().reset_index(name='wins_count')

# Find the worst division (least wins) for each year
worst_divisions = division_wins_counts.loc[division_wins_counts.groupby('season')['wins_count'].idxmin()]

# Create a countplot
plt.figure(figsize=(12, 6))
sns.countplot(x='season', hue='winner_division', data=worst_divisions)
plt.title('Worst Division (Least Wins) Each Year')
plt.xlabel('Season')
plt.ylabel('Count')
plt.legend(title='Division')
plt.show()

"""Graph 1 : as a nfl analyst, I would like to know which nfl divison has the most amount of total wins in a season
Graph 2 : As a nfl analyst, I would llike to ee if there is a trend in strongest divsion in the nfl over many years
Graph: 3: As a nfl analyst, I would like to figure out what changes can be done to balance out the divisions
"""