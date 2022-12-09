<script lang="ts">
  import SplitBarChart from './SplitBarChart.svelte';
  export let player1: string;
  export let player2: string;
  export let matches: { value: string; label: string; player1: string; player2: string }[] = [];

  let acesMax: number;
  let dfMax: number;
  let winnersMax: number;
  let unforcedMax: number;

  let p1Aces: { match: number; value: number }[];
  let p2Aces: { match: number; value: number }[];
  let p1DoubleFaults: { match: any; value: any }[];
  let p2DoubleFaults: { match: any; value: any }[];
  let p1FirstIn: { match: any; value: number; total: any; won: any }[];
  let p2FirstIn: { match: any; value: number; total: any; won: any }[];
  let p1FirstWon: { match: any; value: number; total: any; won: any }[];
  let p2FirstWon: { match: any; value: number; total: any; won: any }[];
  let p1SecondWon: { match: any; value: number; total: any; won: any }[];
  let p2SecondWon: { match: any; value: number; total: any; won: any }[];
  let p1BreakPointSaved: { match: any; value: number; total: any; won: any }[];
  let p2BreakPointSaved: { match: any; value: number; total: any; won: any }[];
  let p1BreakPointWon: { match: any; value: number; total: any; won: number }[];
  let p2BreakPointWon: { match: any; value: number; total: any; won: number }[];
  let p1Winners: { match: any; value: any }[];
  let p2Winners: { match: any; value: any }[];
  let p1UnforcedErrors: { match: any; value: any }[];
  let p2UnforcedErrors: { match: any; value: any }[];

  const fetchOverview = async (m: any[]) => {
    const res = await fetch('/api/matches/overview', {
      method: 'POST',
      body: JSON.stringify(m.map((value) => value.label))
    });
    const data: any[] = await res.json();
    // console.log(data);

    acesMax = Math.max(...data.map((value) => value.aces));
    dfMax = Math.max(...data.map((value) => value.dfs));
    winnersMax = Math.max(...data.map((value) => value.winners));
    unforcedMax = Math.max(...data.map((value) => value.unforced));

    const p1Overview = data.filter((value, index) => {
      return player1 === m[Math.floor(index / 2)]['player1']
        ? value.player === 1
        : value.player === 2;
    });

    const p2Overview = data.filter((value, index) => {
      return player2 === m[Math.floor(index / 2)]['player1']
        ? value.player === 1
        : value.player === 2;
    });

    p1Aces = p1Overview.map((value) => {
      return {
        match: value.overview_id,
        value: value.aces
      };
    });
    p2Aces = p2Overview.map((value) => {
      return {
        match: value.overview_id,
        value: value.aces
      };
    });

    p1DoubleFaults = p1Overview.map((value) => {
      return {
        match: value.overview_id,
        value: value.dfs
      };
    });
    p2DoubleFaults = p2Overview.map((value) => {
      return {
        match: value.overview_id,
        value: value.dfs
      };
    });

    p1FirstIn = p1Overview.map((value) => {
      return {
        match: value.overview_id,
        value: Math.round((100 * value.first_in) / value.serve_pts),
        total: value.serve_pts,
        won: value.first_in
      };
    });
    p2FirstIn = p2Overview.map((value) => {
      return {
        match: value.overview_id,
        value: Math.round((100 * value.first_in) / value.serve_pts),
        total: value.serve_pts,
        won: value.first_in
      };
    });

    p1FirstWon = p1Overview.map((value) => {
      return {
        match: value.overview_id,
        value: Math.round((100 * value.first_won) / value.first_in),
        total: value.first_in,
        won: value.first_won
      };
    });
    p2FirstWon = p2Overview.map((value) => {
      return {
        match: value.overview_id,
        value: Math.round((100 * value.first_won) / value.first_in),
        total: value.first_in,
        won: value.first_won
      };
    });
    p1SecondWon = p1Overview.map((value) => {
      return {
        match: value.overview_id,
        value: Math.round((100 * value.second_won) / value.second_in),
        total: value.second_in,
        won: value.second_won
      };
    });
    p2SecondWon = p2Overview.map((value) => {
      return {
        match: value.overview_id,
        value: Math.round((100 * value.second_won) / value.second_in),
        total: value.second_in,
        won: value.second_won
      };
    });
    p1BreakPointSaved = p1Overview.map((value) => {
      return {
        match: value.overview_id,
        value: value.bk_pts === 0 ? 0 : Math.round((100 * value.bp_saved) / value.bk_pts),
        total: value.bk_pts,
        won: value.bp_saved
      };
    });
    p2BreakPointSaved = p2Overview.map((value) => {
      return {
        match: value.overview_id,
        value: value.bk_pts === 0 ? 0 : Math.round((100 * value.bp_saved) / value.bk_pts),
        total: value.bk_pts,
        won: value.bp_saved
      };
    });
    p1BreakPointWon = p1Overview.map((value, index) => {
      const total = p2BreakPointSaved[index].total;
      const saved = p2BreakPointSaved[index].won;
      const won = total - saved;
      return {
        match: value.overview_id,
        value: total === 0 ? 0 : Math.round((100 * won) / total),
        total,
        won
      };
    });
    p2BreakPointWon = p2Overview.map((value, index) => {
      const total = p1BreakPointSaved[index].total;
      const saved = p1BreakPointSaved[index].won;
      const won = total - saved;
      return {
        match: value.overview_id,
        value: total === 0 ? 0 : Math.round((100 * won) / total),
        total,
        won
      };
    });

    p1Winners = p1Overview.map((value) => {
      return {
        match: value.overview_id,
        value: value.winners
      };
    });
    p2Winners = p2Overview.map((value) => {
      return {
        match: value.overview_id,
        value: value.winners
      };
    });

    p1UnforcedErrors = p1Overview.map((value) => {
      return {
        match: value.overview_id,
        value: value.unforced
      };
    });
    p2UnforcedErrors = p2Overview.map((value) => {
      return {
        match: value.overview_id,
        value: value.unforced
      };
    });
  };

  $: {
    fetchOverview(matches);
  }
</script>

<h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Overview</h2>
<h3 class="text-center text-base">Aces</h3>
<SplitBarChart p1data={p1Aces} p2data={p2Aces} max={acesMax} />
<h3 class="text-center text-base">Double Faults</h3>
<SplitBarChart p1data={p1DoubleFaults} p2data={p2DoubleFaults} max={dfMax} reverse={true} />
<hr class="mt-3 mb-3" />
<h3 class="text-center text-base">1st Serve In</h3>
<SplitBarChart p1data={p1FirstIn} p2data={p2FirstIn} percentage={true} />
<h3 class="text-center text-base">1st Serve Points Won</h3>
<SplitBarChart p1data={p1FirstWon} p2data={p2FirstWon} percentage={true} />
<h3 class="text-center text-base">2nd Serve Points Won</h3>
<SplitBarChart p1data={p1SecondWon} p2data={p2SecondWon} percentage={true} />
<hr class="mt-3 mb-3" />
<h3 class="text-center text-base">Break Points Saved</h3>
<SplitBarChart p1data={p1BreakPointSaved} p2data={p2BreakPointSaved} percentage={true} />
<h3 class="text-center text-base">Break Points Won</h3>
<SplitBarChart p1data={p1BreakPointWon} p2data={p2BreakPointWon} percentage={true} />
<hr class="mt-3 mb-3" />
<h3 class="text-center text-base">Winners</h3>
<SplitBarChart p1data={p1Winners} p2data={p2Winners} max={winnersMax} />
<h3 class="text-center text-base">Unforced Errors</h3>
<SplitBarChart
  p1data={p1UnforcedErrors}
  p2data={p2UnforcedErrors}
  max={unforcedMax}
  reverse={true}
/>

<style>

</style>
