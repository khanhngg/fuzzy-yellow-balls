#!/usr/bin/env python3
import pandas as pd
import os
import glob

'''
Get the top 100 tennis players for every week through decades 90s -> current
ATP for male and WTA for female players

CSV needed:
1. Players data (player_id,name_first,name_last)
- ./tennis_atp/atp_players.csv
- ./tennis_wta/wta_players.csv

2. Rankings data (ranking_date,rank,player,points)
- ./tennis_atp/atp_rankings_90s.csv
- ./tennis_atp/atp_rankings_00s.csv
- ./tennis_atp/atp_rankings_10s.csv
- ./tennis_atp/atp_rankings_20s.csv
- ./tennis_atp/atp_rankings_current.csv
(similarly for WTA rankings)

Sources:
https://github.com/JeffSackmann/tennis_atp
https://github.com/JeffSackmann/tennis_wta
'''

# make a dictionary for all ATP players
all_atp_players = pd.read_csv(
    '../../tennis_atp/atp_players.csv', index_col='player_id')
all_atp_players = all_atp_players[['name_first', 'name_last']]
all_atp_players_dict = all_atp_players.to_dict(orient='index')

all_wta_players = pd.read_csv(
    '../../tennis_wta/wta_players.csv', index_col='player_id')
all_wta_players = all_wta_players[['name_first', 'name_last']]
all_wta_players_dict = all_wta_players.to_dict(orient='index')

# get full name of player by id
def get_player_name(player_id, gender):
    player = all_atp_players_dict[player_id] if gender == 'atp' else all_wta_players_dict[player_id]
    return player['name_first'] + ' ' + player['name_last']

# MAIN
if __name__ == '__main__':
    genders = ['atp', 'wta']
    decades = ['90s', '00s', '10s', '20s', 'current']

    for gender in genders:
        top_players = pd.DataFrame(columns = ['ranking_date','rank','player','points','player_name'])
        top_players_df = []
        for decade in decades:
            # get top 100 players each week (ranking_date)
            all_players_rankings = pd.read_csv(
                '../../tennis_{}/{}_rankings_{}.csv'.format(gender, gender, decade),
                usecols=['ranking_date','rank','player','points'])
            top_100_players = all_players_rankings.groupby('ranking_date', as_index=False).nth[:100]

            # format ranking_date to yyyy-mm-dd
            top_100_players['ranking_date'] = pd.to_datetime(top_100_players['ranking_date'], format = '%Y%m%d')

            # match player to player_id in players_csv and add new col:
            top_100_players['player_name'] = top_100_players.apply(lambda row: get_player_name(row['player'], gender=gender), axis=1)

            top_players_df.append(top_100_players)

        # output to new csv
        top_players = pd.concat(top_players_df)
        top_players.to_csv('../rankings_{}/{}_rankings_all.csv'.format(gender, gender), index=False)