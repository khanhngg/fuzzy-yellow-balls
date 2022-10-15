from numpy import mean
import pandas as pd


def get_stats_from_match(match, player):
    st_in = 0 if match['{}_svpt'.format(player)] == 0 else round(
        100 * match['{}_1stIn'.format(player)] / match['{}_svpt'.format(player)], 2)
    st_won = 0 if match['{}_1stIn'.format(player)] == 0 else round(
        100 * match['{}_1stWon'.format(player)] / match['{}_1stIn'.format(player)], 2)
    nd_won = 0 if match['{}_svpt'.format(player)] - match['{}_1stIn'.format(player)] == 0 else round(
        100 * match['{}_2ndWon'.format(player)] / (match['{}_svpt'.format(player)] - match['{}_1stIn'.format(player)]), 2)
    bp_saved = 0 if match['{}_bpFaced'.format(player)] == 0 else round(
        100 * match['{}_bpSaved'.format(player)] / match['{}_bpFaced'.format(player)], 2)
    v1st_won = round(100 - st_won, 2)
    v2nd_won = round(100 - nd_won, 2)
    bp_cnvt = 0 if match['{}_bpFaced'.format(player)] == 0 else round(
        100 * (match['{}_bpFaced'.format(player)] - match['{}_bpSaved'.format(player)]) / match['{}_bpFaced'.format(player)], 2)
    brk_rate = 0 if match['{}_bpFaced'.format(player)] == 0 or match['{}_SvGms'.format(player)] == 0 else round(
        100 * (match['{}_bpFaced'.format(player)] - match['{}_bpSaved'.format(player)]) / match['{}_SvGms'.format(player)], 2)
    hld_rate = round(100 - brk_rate, 2)

    return (st_in, st_won, nd_won, bp_saved, v1st_won, v2nd_won, bp_cnvt, hld_rate, brk_rate)


def append_stats(player, st_in, st_won, nd_won, bp_saved, v1st_won, v2nd_won, bp_cnvt, hld_rate, brk_rate, s):
    try:
        s[player]['1st_in'].append(st_in)
        s[player]['1st_won'].append(st_won)
        s[player]['2nd_won'].append(nd_won)
        s[player]['bp_saved'].append(bp_saved)
        s[player]['v1st_won'].append(v1st_won)
        s[player]['v2nd_won'].append(v2nd_won)
        s[player]['bp_cnvt'].append(bp_cnvt)
        s[player]['hld_rate'].append(hld_rate)
        s[player]['brk_rate'].append(brk_rate)
    except Exception:
        s[player] = {
            '1st_in': [st_in],
            '1st_won': [st_won],
            '2nd_won': [nd_won],
            'bp_saved': [bp_saved],
            'v1st_won': [v1st_won],
            'v2nd_won': [v2nd_won],
            'bp_cnvt': [bp_cnvt],
            'hld_rate': [hld_rate],
            'brk_rate': [brk_rate],
        }


if __name__ == '__main__':
    for i in ['atp', 'wta']:
        dfs = []

        for j in range(0, 23):
            '''
                'player name': {
                    1st_in
                    1st_won
                    2nd_won
                    bp_saved
                    v1st_won
                    v2nd_won
                    bp_cnvt
                    brk_rate
                    hld_rate
                }
            '''
            stats = {}

            matches = pd.read_csv(
                './tennis_{}/{}_matches_20{:02d}.csv'.format(i, i, j))

            players = pd.DataFrame({
                'player': [],
                'year': [],
                '1st_in': [],
                '1st_won': [],
                '2nd_won': [],
                'bp_saved': [],
                'v1st_won': [],
                'v2nd_won': [],
                'bp_cnvt': [],
                'hld_rate': [],
                'brk_rate': [],
            })

            matches.dropna(subset=['w_svpt'], inplace=True)

            for index, r in matches.iterrows():
                w_1st_in, w_1st_won, w_2nd_won, w_bp_saved, l_v1st_won, l_v2nd_won, l_bp_cnvt, w_hld_rate, l_brk_rate = get_stats_from_match(
                    r, 'w')
                l_1st_in, l_1st_won, l_2nd_won, l_bp_saved, w_v1st_won, w_v2nd_won, w_bp_cnvt, l_hld_rate, w_brk_rate = get_stats_from_match(
                    r, 'l')

                append_stats(r['winner_name'], w_1st_in, w_1st_won, w_2nd_won, w_bp_saved,
                             w_v1st_won, w_v2nd_won, w_bp_cnvt, w_hld_rate, w_brk_rate, stats)
                append_stats(r['loser_name'], l_1st_in, l_1st_won, l_2nd_won, l_bp_saved,
                             l_v1st_won, l_v2nd_won, l_bp_cnvt, l_hld_rate, l_brk_rate, stats)

            for player in stats.keys():
                players.loc[len(players.index)] = [
                    player.strip(),
                    '20{:02d}'.format(j),
                    round(mean(stats[player]['1st_in']), 2),
                    round(mean(stats[player]['1st_won']), 2),
                    round(mean(stats[player]['2nd_won']), 2),
                    round(mean(stats[player]['bp_saved']), 2),
                    round(mean(stats[player]['v1st_won']), 2),
                    round(mean(stats[player]['v2nd_won']), 2),
                    round(mean(stats[player]['bp_cnvt']), 2),
                    round(mean(stats[player]['hld_rate']), 2),
                    round(mean(stats[player]['brk_rate']), 2),
                ]

            dfs.append(players.sort_values('player'))
            # players.to_csv('./atp_2019_stats.csv', index=False)
        all_time = pd.concat(dfs, ignore_index=True)
        all_time.to_csv('./{}_player_stats.csv'.format(i), index=False)
