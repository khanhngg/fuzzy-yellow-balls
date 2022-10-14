#!/usr/bin/env python3

from numpy import mean
import pandas as pd


def insert_stats(r, v1, v2, bp, da, fs, fsw, ss, s, p):
    if r['surface'] == 'Hard':
        try:
            if not v1 == float('inf'):
                s['hard'][p]['1st_rt_pt_won'].append(v1)
            if not v2 == float('inf'):
                s['hard'][p]['2nd_rt_pt_won'].append(v2)
            if not bp == float('inf'):
                s['hard'][p]['bp_convert'].append(bp)
            s['hard'][p]['df_to_ace'].append(da)
            if not fs == float('inf'):
                s['hard'][p]['1st_in'].append(fs)
            if not fsw == float('inf'):
                s['hard'][p]['1st_pt_won'].append(fsw)
            if not ss == float('inf'):
                s['hard'][p]['2nd_pt_won'].append(ss)
        except Exception:
            s['hard'][p] = {
                '1st_rt_pt_won': [] if v1 == float('inf') else [v1],
                '2nd_rt_pt_won': [] if v2 == float('inf') else [v2],
                'bp_convert': [] if bp == float('inf') else [bp],
                'df_to_ace': [da],
                '1st_in': [] if fs == float('inf') else [fs],
                '1st_pt_won': [] if fsw == float('inf') else [fsw],
                '2nd_pt_won': [] if ss == float('inf') else [ss],
            }
    if r['surface'] == 'Clay':
        try:
            if not v1 == float('inf'):
                s['clay'][p]['1st_rt_pt_won'].append(v1)
            if not v2 == float('inf'):
                s['clay'][p]['2nd_rt_pt_won'].append(v2)
            if not bp == float('inf'):
                s['clay'][p]['bp_convert'].append(bp)
            s['clay'][p]['df_to_ace'].append(da)
            if not fs == float('inf'):
                s['clay'][p]['1st_in'].append(fs)
            if not fsw == float('inf'):
                s['clay'][p]['1st_pt_won'].append(fsw)
            if not ss == float('inf'):
                s['clay'][p]['2nd_pt_won'].append(ss)
        except Exception:
            s['clay'][p] = {
                '1st_rt_pt_won': [] if v1 == float('inf') else [v1],
                '2nd_rt_pt_won': [] if v2 == float('inf') else [v2],
                'bp_convert': [] if bp == float('inf') else [bp],
                'df_to_ace': [da],
                '1st_in': [] if fs == float('inf') else [fs],
                '1st_pt_won': [] if fsw == float('inf') else [fsw],
                '2nd_pt_won': [] if ss == float('inf') else [ss],
            }
    if r['surface'] == 'Grass':
        try:
            if not v1 == float('inf'):
                s['grass'][p]['1st_rt_pt_won'].append(v1)
            if not v2 == float('inf'):
                s['grass'][p]['2nd_rt_pt_won'].append(v2)
            if not bp == float('inf'):
                s['grass'][p]['bp_convert'].append(bp)
            s['grass'][p]['df_to_ace'].append(da)
            if not fs == float('inf'):
                s['grass'][p]['1st_in'].append(fs)
            if not fsw == float('inf'):
                s['grass'][p]['1st_pt_won'].append(fsw)
            if not ss == float('inf'):
                s['grass'][p]['2nd_pt_won'].append(ss)
        except Exception:
            s['grass'][p] = {
                '1st_rt_pt_won': [] if v1 == float('inf') else [v1],
                '2nd_rt_pt_won': [] if v2 == float('inf') else [v2],
                'bp_convert': [] if bp == float('inf') else [bp],
                'df_to_ace': [da],
                '1st_in': [] if fs == float('inf') else [fs],
                '1st_pt_won': [] if fsw == float('inf') else [fsw],
                '2nd_pt_won': [] if ss == float('inf') else [ss],
            }


if __name__ == '__main__':
    for year in range(0, 23):
        for surface in ['hard', 'clay', 'grass']:
            for gender in ['atp', 'wta']:
                players = pd.read_csv(
                    './surface_top10_{}/{}_{}_top10_20{:02d}.csv'.format(gender, gender, surface, year))
                matches = pd.read_csv(
                    './tennis_{}/{}_matches_20{:02d}.csv'.format(gender, gender, year))

                stats = {'hard': {}, 'clay': {}, 'grass': {}}

                st_rt_pt_won = []
                nd_rt_pt_won = []
                bp_convert = []
                df_to_ace = []
                st_in = []
                st_pt_won = []
                nd_pt_won = []

                new_stats = {
                    'hard': {
                        '1st_rt_pt_won': [],
                        '2nd_rt_pt_won': [],
                        'bp_convert': [],
                        'df_to_ace': [],
                        '1st_in': [],
                        '1st_pt_won': [],
                        '2nd_pt_won': [],
                    },
                    'clay': {
                        '1st_rt_pt_won': [],
                        '2nd_rt_pt_won': [],
                        'bp_convert': [],
                        'df_to_ace': [],
                        '1st_in': [],
                        '1st_pt_won': [],
                        '2nd_pt_won': [],
                    },
                    'grass': {
                        '1st_rt_pt_won': [],
                        '2nd_rt_pt_won': [],
                        'bp_convert': [],
                        'df_to_ace': [],
                        '1st_in': [],
                        '1st_pt_won': [],
                        '2nd_pt_won': [],
                    }
                }

                matches.dropna(subset=['w_svpt'], inplace=True)

                for i, r in players.iterrows():
                    player = r['player']
                    for index, row in matches.iterrows():
                        v1st, v2nd, bpcnv, df2a, fsin, fswon, sswon = 0, 0, 0, 0, 0, 0, 0

                        if row['winner_name'].strip() == player:
                            v1st = float('inf') if row['l_1stIn'] == 0 else round(
                                (1 - row['l_1stWon'] / row['l_1stIn']) * 100, 2)
                            v2nd = float('inf') if (row['l_svpt'] - row['l_1stIn']) == 0 else round(
                                (1 - row['l_2ndWon'] / (row['l_svpt'] - row['l_1stIn'])) * 100, 2)
                            bpcnv = float('inf') if row['l_bpFaced'] == 0 else round(
                                (1 - row['l_bpSaved'] / row['l_bpFaced']) * 100, 2)
                            df2a = row['w_df'] if row['w_ace'] == 0 else round(
                                (row['w_df'] / row['w_ace']) * 100, 2)
                            fsin = float('inf') if row['w_svpt'] == 0 else round(
                                100*row['w_1stIn']/row['w_svpt'], 2)
                            fswon = float('inf') if row['w_1stIn'] == 0 else round(
                                (row['w_1stWon'] / row['w_1stIn']) * 100, 2)
                            sswon = float('inf') if (row['w_svpt'] - row['w_1stIn']) == 0 else round(
                                (row['w_2ndWon'] / (row['w_svpt'] - row['w_1stIn'])) * 100, 2)
                            insert_stats(row, v1st, v2nd, bpcnv, df2a,
                                         fsin, fswon, sswon, stats, player)

                        if row['loser_name'].strip() == player:
                            v1st = float('inf') if row['w_1stIn'] == 0 else round(
                                (1 - row['w_1stWon'] / row['w_1stIn']) * 100, 2)
                            v2nd = float('inf') if (row['w_svpt'] - row['w_1stIn']) == 0 else round(
                                (1 - row['w_2ndWon'] / (row['w_svpt'] - row['w_1stIn'])) * 100, 2)
                            bpcnv = float('inf') if row['w_bpFaced'] == 0 else round(
                                (1 - row['w_bpSaved'] / row['w_bpFaced']) * 100, 2)
                            df2a = row['l_df'] if row['l_ace'] == 0 else round(
                                (row['l_df'] / row['l_ace']) * 100, 2)
                            fsin = float('inf') if row['l_svpt'] == 0 else round(
                                100*row['l_1stIn']/row['l_svpt'], 2)
                            fswon = float('inf') if row['l_1stIn'] == 0 else round(
                                (row['l_1stWon'] / row['l_1stIn']) * 100, 2)
                            sswon = float('inf') if (row['l_svpt'] - row['w_1stIn']) == 0 else round(
                                (row['l_2ndWon'] / (row['l_svpt'] - row['w_1stIn'])) * 100, 2)
                            insert_stats(row, v1st, v2nd, bpcnv, df2a,
                                         fsin, fswon, sswon, stats, player)

                for i in stats.keys():
                    for j in players['player']:
                        try:
                            new_stats[i]['1st_rt_pt_won'].append(0 if len(
                                stats[i][j]['1st_rt_pt_won']) == 0 else round(mean(stats[i][j]['1st_rt_pt_won']), 2))
                            new_stats[i]['2nd_rt_pt_won'].append(0 if len(
                                stats[i][j]['2nd_rt_pt_won']) == 0 else round(mean(stats[i][j]['2nd_rt_pt_won']), 2))
                            new_stats[i]['bp_convert'].append(0 if len(
                                stats[i][j]['bp_convert']) == 0 else round(mean(stats[i][j]['bp_convert']), 2))
                            new_stats[i]['df_to_ace'].append(0 if len(
                                stats[i][j]['df_to_ace']) == 0 else round(mean(stats[i][j]['df_to_ace']), 2))
                            new_stats[i]['1st_in'].append(0 if len(
                                stats[i][j]['1st_in']) == 0 else round(mean(stats[i][j]['1st_in']), 2))
                            new_stats[i]['1st_pt_won'].append(0 if len(
                                stats[i][j]['1st_pt_won']) == 0 else round(mean(stats[i][j]['1st_pt_won']), 2))
                            new_stats[i]['2nd_pt_won'].append(0 if len(
                                stats[i][j]['2nd_pt_won']) == 0 else round(mean(stats[i][j]['2nd_pt_won']), 2))
                        except KeyError:
                            new_stats[i]['1st_rt_pt_won'].append(0)
                            new_stats[i]['2nd_rt_pt_won'].append(0)
                            new_stats[i]['bp_convert'].append(0)
                            new_stats[i]['df_to_ace'].append(0)
                            new_stats[i]['1st_in'].append(0)
                            new_stats[i]['1st_pt_won'].append(0)
                            new_stats[i]['2nd_pt_won'].append(0)

                    st_rt_pt_won.extend(new_stats[i]['1st_rt_pt_won'])
                    nd_rt_pt_won.extend(new_stats[i]['2nd_rt_pt_won'])
                    bp_convert.extend(new_stats[i]['bp_convert'])
                    df_to_ace.extend(new_stats[i]['df_to_ace'])
                    st_in.extend(new_stats[i]['1st_in'])
                    st_pt_won.extend(new_stats[i]['1st_pt_won'])
                    nd_pt_won.extend(new_stats[i]['2nd_pt_won'])

                top_players = pd.concat([players]*3, ignore_index=True)
                if not year == 20:
                    top_players['surface'] = ['hard' for j in range(
                        10)]+['clay' for j in range(10)]+['grass' for j in range(10)]

                top_players['1st_rt_pt_won'] = st_rt_pt_won
                top_players['2nd_rt_pt_won'] = nd_rt_pt_won
                top_players['bp_convert'] = bp_convert
                top_players['df_to_ace'] = df_to_ace
                top_players['1st_in'] = st_in
                top_players['1st_pt_won'] = st_pt_won
                top_players['2nd_pt_won'] = nd_pt_won

                top_players.pop('Unnamed: 0')
                top_players.to_csv('./surface_top10_{}/{}_{}_top10_20{:02d}.csv'.format(
                    gender, gender, surface, year), index=False)
                # print(top_players)
