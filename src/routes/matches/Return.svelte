<script lang="ts">
  import Select from 'svelte-select';
  import ReturnChart from './ReturnChart.svelte';
  import SplitBarChart from './SplitBarChart.svelte';
  export let player1: string;
  export let player2: string;
  export let matches: any = {};

  const items = ['Overview', 'Return Depth', 'Return Type', 'Serve Type'];
  let filter: number = 0;

  let p1Return: {
    Total: any[];
    v1st: any[];
    v2nd: any[];
    forehand: any[];
    backhand: any[];
    groundStroke: any[];
    Slice: any[];
    shallow: any[];
    deep: any[];
    veryDeep: any[];
    deuce: any[];
    ad: any[];
    deuceWide: any[];
    adWide: any[];
    deuceBody: any[];
    adBody: any[];
    deuceT: any[];
    adT: any[];
  };

  let p2Return: {
    Total: any[];
    v1st: any[];
    v2nd: any[];
    forehand: any[];
    backhand: any[];
    groundStroke: any[];
    Slice: any[];
    shallow: any[];
    deep: any[];
    veryDeep: any[];
    deuce: any[];
    ad: any[];
    deuceWide: any[];
    adWide: any[];
    deuceBody: any[];
    adBody: any[];
    deuceT: any[];
    adT: any[];
  };

  const fetchReturn = async (m: any) => {
    const res = await fetch('/api/matches/return', {
      method: 'POST',
      body: JSON.stringify(Object.keys(m))
    });
    const data: any[] = await res.json();

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

    p1Return = {
      Total: p1Data
        .filter((value) => value.row === 'Total')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      v1st: p1Data
        .filter((value) => value.row === 'v1st')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      v2nd: p1Data
        .filter((value) => value.row === 'v2nd')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      forehand: p1Data
        .filter((value) => value.row === 'fh')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      backhand: p1Data
        .filter((value) => value.row === 'bh')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      groundStroke: p1Data
        .filter((value) => value.row === 'gs')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      Slice: p1Data
        .filter((value) => value.row === 'sl')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      shallow: p1Data
        .filter((value) => value.row === '7')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      deep: p1Data
        .filter((value) => value.row === '89')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      veryDeep: p1Data
        .filter((value) => value.row === '9')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      deuce: p1Data
        .filter((value) => value.row === 'D')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      ad: p1Data
        .filter((value) => value.row === 'A')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      deuceWide: p1Data
        .filter((value) => value.row === '4D')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      adWide: p1Data
        .filter((value) => value.row === '4A')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      deuceBody: p1Data
        .filter((value) => value.row === '5D')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      adBody: p1Data
        .filter((value) => value.row === '5A')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      deuceT: p1Data
        .filter((value) => value.row === '6D')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      adT: p1Data
        .filter((value) => value.row === '6A')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        )
    };
    p2Return = {
      Total: p2Data
        .filter((value) => value.row === 'Total')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      v1st: p2Data
        .filter((value) => value.row === 'v1st')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      v2nd: p2Data
        .filter((value) => value.row === 'v2nd')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      forehand: p2Data
        .filter((value) => value.row === 'fh')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      backhand: p2Data
        .filter((value) => value.row === 'bh')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      groundStroke: p2Data
        .filter((value) => value.row === 'gs')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      Slice: p2Data
        .filter((value) => value.row === 'sl')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      shallow: p2Data
        .filter((value) => value.row === '7')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      deep: p2Data
        .filter((value) => value.row === '89')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      veryDeep: p2Data
        .filter((value) => value.row === '9')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      deuce: p2Data
        .filter((value) => value.row === 'D')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      ad: p2Data
        .filter((value) => value.row === 'A')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      deuceWide: p2Data
        .filter((value) => value.row === '4D')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      adWide: p2Data
        .filter((value) => value.row === '4A')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      deuceBody: p2Data
        .filter((value) => value.row === '5D')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      adBody: p2Data
        .filter((value) => value.row === '5A')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      deuceT: p2Data
        .filter((value) => value.row === '6D')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        ),
      adT: p2Data
        .filter((value) => value.row === '6A')
        .reduce(
          (obj, item) => ({
            ...obj,
            [item.match_id]: {
              pts: item.pts,
              ptsWon: item.pts_won,
              inPlay: item.in_play,
              inPlayWon: item.in_play_won,
              avgRally: Math.round((item.total_shots * 100) / item.pts) / 100
            }
          }),
          {}
        )
    };
    // console.log({ p1Return, p2Return });
  };

  const handleSelect = ({ detail }: { detail: { index: number } }) => {
    filter = detail.index;
  };

  $: {
    fetchReturn(matches);
  }
</script>

<h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Return</h2>
<label for="selectedMatches">Select a category</label>
<div class="text-gray-900 px-3 my-3">
  <Select {items} on:select={handleSelect} />
</div>
{#if filter === 0}
  <h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Total</h2>
  <ReturnChart p1Data={p1Return && p1Return.Total} p2Data={p2Return && p2Return.Total} {matches} />
  <hr class="mt-3 mb-3" />
  <h2 class="text-center text-xl text-gray-900 dark:text-gray-200">VS 1st Serve</h2>
  <ReturnChart p1Data={p1Return && p1Return.v1st} p2Data={p2Return && p2Return.v1st} {matches} />
  <hr class="mt-3 mb-3" />
  <h2 class="text-center text-xl text-gray-900 dark:text-gray-200">VS 2nd Serve</h2>
  <ReturnChart p1Data={p1Return && p1Return.v2nd} p2Data={p2Return && p2Return.v2nd} {matches} />
{:else if filter === 1}
  <h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Shallow</h2>
  <ReturnChart
    p1Data={p1Return && p1Return.shallow}
    p2Data={p2Return && p2Return.shallow}
    {matches}
  />
  <hr class="mt-3 mb-3" />
  <h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Deep</h2>
  <ReturnChart p1Data={p1Return && p1Return.deep} p2Data={p2Return && p2Return.deep} {matches} />
  <hr class="mt-3 mb-3" />
  <h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Very Deep</h2>
  <ReturnChart
    p1Data={p1Return && p1Return.veryDeep}
    p2Data={p2Return && p2Return.veryDeep}
    {matches}
  />
{:else if filter === 2}
  <h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Forehand</h2>
  <ReturnChart
    p1Data={p1Return && p1Return.forehand}
    p2Data={p2Return && p2Return.forehand}
    {matches}
  />
  <hr class="mt-3 mb-3" />
  <h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Backhand</h2>
  <ReturnChart
    p1Data={p1Return && p1Return.backhand}
    p2Data={p2Return && p2Return.backhand}
    {matches}
  />
  <hr class="mt-3 mb-3" />
  <h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Ground Stroke</h2>
  <ReturnChart
    p1Data={p1Return && p1Return.groundStroke}
    p2Data={p2Return && p2Return.groundStroke}
    {matches}
  />
  <hr class="mt-3 mb-3" />
  <h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Slice</h2>
  <ReturnChart p1Data={p1Return && p1Return.Slice} p2Data={p2Return && p2Return.Slice} {matches} />
{:else if filter === 3}
  <h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Deuce Wide</h2>
  <ReturnChart
    p1Data={p1Return && p1Return.deuceWide}
    p2Data={p2Return && p2Return.deuceWide}
    {matches}
  />
  <hr class="mt-3 mb-3" />
  <h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Ad Wide</h2>
  <ReturnChart
    p1Data={p1Return && p1Return.adWide}
    p2Data={p2Return && p2Return.adWide}
    {matches}
  />
  <hr class="mt-3 mb-3" />
  <h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Deuce Body</h2>
  <ReturnChart
    p1Data={p1Return && p1Return.deuceBody}
    p2Data={p2Return && p2Return.deuceBody}
    {matches}
  />
  <hr class="mt-3 mb-3" />
  <h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Ad Body</h2>
  <ReturnChart
    p1Data={p1Return && p1Return.adBody}
    p2Data={p2Return && p2Return.adBody}
    {matches}
  />
  <hr class="mt-3 mb-3" />
  <h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Deuce T</h2>
  <ReturnChart
    p1Data={p1Return && p1Return.deuceT}
    p2Data={p2Return && p2Return.deuceT}
    {matches}
  />
  <hr class="mt-3 mb-3" />
  <h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Ad T</h2>
  <ReturnChart p1Data={p1Return && p1Return.adT} p2Data={p2Return && p2Return.adT} {matches} />
{/if}
