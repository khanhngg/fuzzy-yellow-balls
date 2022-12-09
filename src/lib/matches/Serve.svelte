<script lang="ts">
  import SplitBarChart from './SplitBarChart.svelte';
  export let player1: string;
  export let player2: string;
  export let matches: { value: string; label: string; player1: string; player2: string }[] = [];

  let totalMax: number;
  let acesMax: number;
  let forcedMax: number;

  let p1Total: { match: any; value: any }[];
  let p2Total: { match: any; value: any }[];
  let p1Won: { match: any; value: number; total: any; won: any }[];
  let p2Won: { match: any; value: number; total: any; won: any }[];
  let p1WonLessThan3: { match: any; value: number; total: any; won: any }[];
  let p2WonLessThan3: { match: any; value: number; total: any; won: any }[];
  let p1Aces: { match: any; value: any }[];
  let p2Aces: { match: any; value: any }[];
  let p1ForcedErrors: { match: any; value: any }[];
  let p2ForcedErrors: { match: any; value: any }[];
  let p1T: { match: any; value: any }[];
  let p2T: { match: any; value: any }[];
  let p1Body: { match: any; value: any }[];
  let p2Body: { match: any; value: any }[];
  let p1Wide: { match: any; value: any }[];
  let p2Wide: { match: any; value: any }[];

  const fetchServe = async (m: any[]) => {
    console.log(JSON.stringify(m.map((value) => value.label)))
    const res = await fetch('/api/matches/serve', {
      method: 'POST',
      body: JSON.stringify(m.map((value) => value.label))
    });
    const data: any[] = (await res.json()).sort((a, b) => {
      let x = a.match_id;
      let y = b.match_id;
      if (x < y) return -1;
      if (x > y) return 1;
      return 0;
    });
    // console.log(data);

    totalMax = Math.max(...data.map((value) => value.pts));
    acesMax = Math.max(...data.map((value) => value.aces));
    forcedMax = Math.max(...data.map((value) => value.forced_err));

    const p1Serve = data.filter((value, index) => {
      return player1 === matches[Math.floor(index / 2)]['player1']
        ? value.player === 1
        : value.player === 2;
    });

    const p2Serve = data.filter((value, index) => {
      return player2 === matches[Math.floor(index / 2)]['player1']
        ? value.player === 1
        : value.player === 2;
    });

    p1Total = p1Serve.map((value) => {
      return {
        match: value.overview_id,
        value: value.pts
      };
    });
    p2Total = p2Serve.map((value) => {
      return {
        match: value.overview_id,
        value: value.pts
      };
    });

    p1Won = p1Serve.map((value) => {
      return {
        match: value.overview_id,
        value: Math.round((100 * value.pts_won) / value.pts),
        total: value.pts,
        won: value.pts_won
      };
    });
    p2Won = p2Serve.map((value) => {
      return {
        match: value.overview_id,
        value: Math.round((100 * value.pts_won) / value.pts),
        total: value.pts,
        won: value.pts_won
      };
    });

    p1WonLessThan3 = p1Serve.map((value, index) => {
      const total = p1Won[index].won;
      const won = value.pts_won_lte_3_shots;
      return {
        match: value.overview_id,
        value: Math.round((100 * won) / total),
        total,
        won
      };
    });
    p2WonLessThan3 = p2Serve.map((value, index) => {
      const total = p2Won[index].won;
      const won = value.pts_won_lte_3_shots;
      return {
        match: value.overview_id,
        value: Math.round((100 * value.pts_won) / value.pts),
        total,
        won
      };
    });

    p1Aces = p1Serve.map((value) => {
      return {
        match: value.overview_id,
        value: value.aces
      };
    });
    p2Aces = p2Serve.map((value) => {
      return {
        match: value.overview_id,
        value: value.aces
      };
    });
    p1ForcedErrors = p1Serve.map((value) => {
      return {
        match: value.overview_id,
        value: value.forced_err
      };
    });
    p2ForcedErrors = p2Serve.map((value) => {
      return {
        match: value.overview_id,
        value: value.forced_err
      };
    });

    p1T = p1Serve.map((value) => {
      return {
        match: value.overview_id,
        value: value.t
      };
    });
    p2T = p2Serve.map((value) => {
      return {
        match: value.overview_id,
        value: value.t
      };
    });

    p1Body = p1Serve.map((value) => {
      return {
        match: value.overview_id,
        value: value.body
      };
    });
    p2Body = p2Serve.map((value) => {
      return {
        match: value.overview_id,
        value: value.body
      };
    });
    p1Wide = p1Serve.map((value) => {
      return {
        match: value.overview_id,
        value: value.wide
      };
    });
    p2Wide = p2Serve.map((value) => {
      return {
        match: value.overview_id,
        value: value.wide
      };
    });
  };

  $: {
    fetchServe(matches);
  }
</script>

<h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Serve</h2>
<h3 class="text-center text-base">Total Points</h3>
<SplitBarChart p1data={p1Total} p2data={p2Total} max={totalMax} neutral={true} />
<h3 class="text-center text-base">Points Won</h3>
<SplitBarChart p1data={p1Won} p2data={p2Won} percentage={true} />
<h3 class="text-center text-base">Points Won Under 3 Shots</h3>
<SplitBarChart p1data={p1WonLessThan3} p2data={p2WonLessThan3} percentage={true} />
<hr class="mt-3 mb-3" />
<h3 class="text-center text-base">Aces</h3>
<SplitBarChart p1data={p1Aces} p2data={p2Aces} max={acesMax} />
<h3 class="text-center text-base">Forced Errors</h3>
<SplitBarChart p1data={p1ForcedErrors} p2data={p2ForcedErrors} max={forcedMax} />
<hr class="mt-3 mb-3" />
<h3 class="text-center text-base">T</h3>
<SplitBarChart p1data={p1T} p2data={p2T} max={totalMax} neutral={true} />
<h3 class="text-center text-base">Body</h3>
<SplitBarChart p1data={p1Body} p2data={p2Body} max={totalMax} neutral={true} />
<h3 class="text-center text-base">Wide</h3>
<SplitBarChart p1data={p1Wide} p2data={p2Wide} max={totalMax} neutral={true} />
