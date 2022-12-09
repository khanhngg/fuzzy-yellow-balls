<script lang="ts">
  import ReturnChart from './ReturnChart.svelte';
  import SplitBarChart from './SplitBarChart.svelte';
  export let player1: string;
  export let player2: string;
  export let matches: any = {};

  let ptsMax: number;
  let winnersMax: number;
  let unforcedMax: number;
  let avgRallyMax: number;
  let passedMax: number;
  let forcedMax: number;

  let p1Pts: { match: any; value: any }[];
  let p1PtsWon: { match: any; value: number; total: any; won: any }[];
  let p1Winner: { match: any; value: any }[];
  let p1Unforced: { match: any; value: any }[];
  let p1Forced: { match: any; value: any }[];
  let p1Passed: { match: any; value: any }[];
  let p1AvgRally: { match: any; value: number }[];
  let p2Pts: { match: any; value: any }[];
  let p2PtsWon: { match: any; value: number; total: any; won: any }[];
  let p2Winner: { match: any; value: any }[];
  let p2Unforced: { match: any; value: any }[];
  let p2Forced: { match: any; value: any }[];
  let p2Passed: { match: any; value: any }[];
  let p2AvgRally: { match: any; value: number }[];

  const fetchNetPoint = async (m: any) => {
    const res = await fetch('/api/matches/netpoint', {
      method: 'POST',
      body: JSON.stringify(Object.keys(m))
    });
    const data: any[] = (await res.json()).sort((a, b) => {
      let x = a.match_id;
      let y = b.match_id;
      if (x < y) return -1;
      if (x > y) return 1;
      return 0;
    });
    console.log(data);

    ptsMax = Math.max(...data.map((value) => value.net_pts));
    unforcedMax = Math.max(...data.map((value) => value.net_unforced));
    winnersMax = Math.max(...data.map((value) => value.net_winner));
    forcedMax = Math.max(...data.map((value) => value.passing_shot_induced_forced));
    passedMax = Math.max(...data.map((value) => value.passed_at_net));
    avgRallyMax = Math.max(
      ...data.map((value) => Math.round((value.total_shots * 100) / value.net_pts) / 100)
    );

    const p1Data = data
      .filter((value) => {
        return matches[value.match_id].player1 === player1
          ? value.player === 1
          : value.player === 2;
      })
      .sort((a, b) => a.match_id - b.match_id);

    const p2Data = data
      .filter((value) => {
        return matches[value.match_id].player1 === player2
          ? value.player === 1
          : value.player === 2;
      })
      .sort((a, b) => a.match_id - b.match_id);

    p1Pts = p1Data.map((value) => {
      return {
        match: value.netpoint_id,
        value: value.net_pts
      };
    });
    p1PtsWon = p1Data.map((value) => {
      return {
        match: value.netpoint_id,
        value: Math.round((100 * value.pts_won) / value.net_pts),
        total: value.net_pts,
        won: value.pts_won
      };
    });
    p1Winner = p1Data.map((value) => {
      return {
        match: value.netpoint_id,
        value: value.net_winner
      };
    });
    p1Unforced = p1Data.map((value) => {
      return {
        match: value.netpoint_id,
        value: value.net_unforced
      };
    });
    p1Forced = p1Data.map((value) => {
      return {
        match: value.netpoint_id,
        value: value.passing_shot_induced_forced
      };
    });
    p1Passed = p1Data.map((value) => {
      return {
        match: value.netpoint_id,
        value: value.passed_at_net
      };
    });
    p1AvgRally = p1Data.map((value) => {
      return {
        match: value.netpoint_id,
        value: Math.round((value.total_shots * 100) / value.net_pts) / 100
      };
    });

    p2Pts = p2Data.map((value) => {
      return {
        match: value.netpoint_id,
        value: value.net_pts
      };
    });
    p2PtsWon = p2Data.map((value) => {
      return {
        match: value.netpoint_id,
        value: Math.round((100 * value.pts_won) / value.net_pts),
        total: value.net_pts,
        won: value.pts_won
      };
    });
    p2Winner = p2Data.map((value) => {
      return {
        match: value.netpoint_id,
        value: value.net_winner
      };
    });
    p2Unforced = p2Data.map((value) => {
      return {
        match: value.netpoint_id,
        value: value.net_unforced
      };
    });
    p2Forced = p2Data.map((value) => {
      return {
        match: value.netpoint_id,
        value: value.passing_shot_induced_forced
      };
    });
    p2Passed = p2Data.map((value) => {
      return {
        match: value.netpoint_id,
        value: value.passed_at_net
      };
    });
    p2AvgRally = p2Data.map((value) => {
      return {
        match: value.netpoint_id,
        value: Math.round((value.total_shots * 100) / value.net_pts) / 100
      };
    });

    // console.log({ ptsMax, unforcedMax, winnersMax, avgRallyMax });
  };

  $: fetchNetPoint(matches);
</script>

<h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Net Points</h2>
<h3 class="text-center text-base">Total Points</h3>
<SplitBarChart p1data={p1Pts} p2data={p2Pts} max={ptsMax} neutral={true} />
<h3 class="text-center text-base">Points Won</h3>
<SplitBarChart p1data={p1PtsWon} p2data={p2PtsWon} percentage={true} />
<h3 class="text-center text-base">Winners</h3>
<SplitBarChart p1data={p1Winner} p2data={p2Winner} max={winnersMax} />
<h3 class="text-center text-base">Unforced Errors</h3>
<SplitBarChart p1data={p1Unforced} p2data={p2Unforced} max={unforcedMax} reverse={true} />
<h3 class="text-center text-base">Passed</h3>
<SplitBarChart p1data={p1Passed} p2data={p2Passed} max={passedMax} reverse={true} />
<h3 class="text-center text-base">Errors from Passing Shots</h3>
<SplitBarChart p1data={p1Forced} p2data={p2Forced} max={forcedMax} reverse={true} />
<h3 class="text-center text-base">Average Rally Length</h3>
<SplitBarChart p1data={p1AvgRally} p2data={p2AvgRally} max={avgRallyMax} neutral={true} />
