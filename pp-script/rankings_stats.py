#!/usr/bin/env python3
import pandas as pd
import json

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
        players_map = {}
        for decade in decades:
            # get top 100 players each week (ranking_date)
            all_players_rankings = pd.read_csv(
                '../../tennis_{}/{}_rankings_{}.csv'.format(gender, gender, decade),
                usecols=['ranking_date','rank','player','points'])

            # clean up csv data from 00s
            if gender == 'wta' and decade == '00s':
                all_players_rankings['ranking_date'] = pd.to_datetime(all_players_rankings['ranking_date'], format = '%Y%m%d')
                all_players_rankings.sort_values(by=['ranking_date', 'rank'], ascending=True, inplace = True)

            top_100_players = all_players_rankings.groupby('ranking_date', as_index=False).nth[:10]

            # format ranking_date to yyyy-mm-dd
            top_100_players['ranking_date'] = pd.to_datetime(top_100_players['ranking_date'], format = '%Y%m%d')

            # match player to player_id in players_csv and add new col:
            top_100_players['player_name'] = top_100_players.apply(lambda row: get_player_name(row['player'], gender=gender), axis=1)

            # keep rows that have valid value for 'points'
            top_100_players = top_100_players[top_100_players['points'].notna()]

            top_players_df.append(top_100_players)


        # concat new top players to the main dataframe 'top_players'
        top_players = pd.concat(top_players_df)

        # list of all players' names
        top_players_names = top_players['player_name'].unique().tolist()
        # print(top_players_names)

        # map player's name to player
        for index, row in top_players.iterrows():
            player_name = row['player_name']
            if player_name not in players_map:
                player = {
                    'player': row['player'],
                    'player_name': row['player_name'],
                }
                players_map[player_name] = player
        # output to new csv
        # top_players.to_csv('../rankings_{}/{}_rankings_all.csv'.format(gender, gender), index=False)

        # transform to map {date: [list_players]}
        # transform to nested list [date, [list_players]]
        result_list = []
        current_date = ''
        current_list = []
        current_players_list = []
        current_players_names = []
        for index, row in top_players.iterrows():
            date = row['ranking_date'].strftime('%Y-%m-%d')
            player = {
                'rank': row['rank'],
                'player': row['player'],
                'points': row['points'],
                'player_name': row['player_name'],
            }

            # new date to add, reset current_list and current_players_list
            if current_date != date:
                # add previous list to result
                if current_list: # only add if not empty list
                    # add the remaining players
                    to_add_players_names = list(set(top_players_names) - set(current_players_names))
                    for name in to_add_players_names:
                        newPlayer = players_map[name]
                        newPlayer['rank'] = 123
                        newPlayer['points'] = 0
                        current_players_list.append(newPlayer)
                        current_list = [current_date, current_players_list]

                    # add prev list to result
                    result_list.append(current_list)

                # reset
                current_date = date
                current_players_names = []
                current_players_list = []
                current_list = []

            # keep track of players names
            current_players_names.append(row['player_name'])

            # add new player
            current_players_list.append(player)

            # update players list for this date
            current_list = [current_date, current_players_list]

            # if date in result_map:
            #     result_map[date].append(player)
            # else:
            #     result_map[date] = []
            #     result_map[date].append(player)
 
        # write to json file
        with open('../rankings_{}/{}_rankings_all.json'.format(gender, gender), 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(result_list, indent=4))