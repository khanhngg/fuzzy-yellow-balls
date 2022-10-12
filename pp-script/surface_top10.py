#!/usr/bin/env python3

import csv
import pandas as pd


if __name__ == '__main__':
    for i in range(0, 23):
        for j in ['atp', 'wta']:
            record = {'hard': {}, 'clay': {}, 'grass': {}}
            hard, clay, grass = {'player': [], 'win_rate': []}, {
                'player': [], 'win_rate': []}, {'player': [], 'win_rate': []}
            df = pd.read_csv('tennis_{}/{}_matches_20{:02d}.csv'.format(j,j,i))

            for x in df.index:
                winner = df.loc[x, 'winner_name']
                loser = df.loc[x, 'loser_name']

                if df.loc[x, 'surface'] == 'Hard':
                    try:
                        record['hard'][winner]['win'] += 1
                        record['hard'][winner]['total'] += 1
                    except Exception:
                        record['hard'][winner] = {'win': 1, 'total': 1}
                    try:
                        record['hard'][loser]['total'] += 1
                    except Exception:
                        record['hard'][loser] = {'win': 0, 'total': 1}

                if df.loc[x, 'surface'] == 'Clay':
                    try:
                        record['clay'][winner]['win'] += 1
                        record['clay'][winner]['total'] += 1
                    except Exception:
                        record['clay'][winner] = {'win': 1, 'total': 1}
                    try:
                        record['clay'][loser]['total'] += 1
                    except Exception:
                        record['clay'][loser] = {'win': 0, 'total': 1}

                if df.loc[x, 'surface'] == 'Grass':
                    try:
                        record['grass'][winner]['win'] += 1
                        record['grass'][winner]['total'] += 1
                    except Exception:
                        record['grass'][winner] = {'win': 1, 'total': 1}
                    try:
                        record['grass'][loser]['total'] += 1
                    except Exception:
                        record['grass'][loser] = {'win': 0, 'total': 1}

            for key in record['hard'].keys():
                if record['hard'][key]['total'] > 9:
                    hard['player'].append(key)
                    hard['win_rate'].append(
                        round((record['hard'][key]['win'] / record['hard'][key]['total']) * 100, 2))

            for key in record['clay'].keys():
                if record['clay'][key]['total'] > 9:
                    clay['player'].append(key)
                    clay['win_rate'].append(
                        round((record['clay'][key]['win'] / record['clay'][key]['total']) * 100, 2))

            for key in record['grass'].keys():
                if record['grass'][key]['total'] > 5:
                    grass['player'].append(key)
                    grass['win_rate'].append(
                        round((record['grass'][key]['win'] / record['grass'][key]['total']) * 100, 2))

            hard_df = pd.DataFrame(hard)
            clay_df = pd.DataFrame(clay)
            grass_df = pd.DataFrame(grass)
            # print(hard_df.nlargest(10, 'win_rate'))
            # print(clay_df.nlargest(10, 'win_rate'))
            # print(grass_df.nlargest(10, 'win_rate'))
            hard_df.nlargest(10, 'win_rate').reset_index(drop=True).to_csv(
                './surface_top10_{}/{}_hard_top10_20{:02d}.csv'.format(j,j,i))
            clay_df.nlargest(10, 'win_rate').reset_index(drop=True).to_csv(
                './surface_top10_{}/{}_clay_top10_20{:02d}.csv'.format(j,j,i))
            grass_df.nlargest(10, 'win_rate').reset_index(drop=True).to_csv(
                './surface_top10_{}/{}_grass_top10_20{:02d}.csv'.format(j,j,i))
