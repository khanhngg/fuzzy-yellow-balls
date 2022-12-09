<script lang="ts">
  import SplitBarChart from './SplitBarChart.svelte';

  export let p1Data: any;
  export let p2Data: any;
  export let matches: any;

  let pointMax: number = 0;
  let avgRallyMax: number = 0;

  let p1Point: { match: number; value: number }[];
  let p2Point: { match: number; value: number }[];
  let p1PointWon: { match: number; value: number; total: number; won: number }[];
  let p2PointWon: { match: number; value: number; total: number; won: number }[];
  let p1InPlay: { match: number; value: number; total: number; won: number }[];
  let p2InPlay: { match: number; value: number; total: number; won: number }[];
  let p1InPlayWon: { match: number; value: number; total: number; won: number }[];
  let p2InPlayWon: { match: number; value: number; total: number; won: number }[];
  let p1AvgRally: { match: number; value: number }[];
  let p2AvgRally: { match: number; value: number }[];

  const populateData = (m: any) => {
    // console.log({ m, p1Data, p2Data });
    const matchIDs = Object.keys(m);
    p1Point = [];
    p2Point = [];
    p1PointWon = [];
    p2PointWon = [];
    p1InPlay = [];
    p2InPlay = [];
    p1InPlayWon = [];
    p2InPlayWon = [];
    p1AvgRally = [];
    p2AvgRally = [];

    for (let i = 0; i < matchIDs.length; i++) {
      const match = matchIDs[i];

      if (p1Data[match]) {
        if (p1Data[match].pts > pointMax) pointMax = p1Data[match].pts;
        if (p1Data[match].avgRally > avgRallyMax) avgRallyMax = p1Data[match].avgRally;

        p1Point.push({ match: i, value: p1Data[match].pts });
        p1PointWon.push({
          match: i,
          value: Math.round((p1Data[match].ptsWon * 100) / p1Data[match].pts),
          total: p1Data[match].pts,
          won: p1Data[match].ptsWon
        });
        p1InPlay.push({
          match: i,
          value: Math.round((p1Data[match].inPlay * 100) / p1Data[match].pts),
          total: p1Data[match].pts,
          won: p1Data[match].inPlay
        });
        p1InPlayWon.push({
          match: i,
          value: Math.round((p1Data[match].inPlayWon * 100) / p1Data[match].inPlay),
          total: p1Data[match].inPlay,
          won: p1Data[match].inPlayWon
        });
        p1AvgRally.push({ match: i, value: p1Data[match].avgRally });
      } else {
        p1Point.push({ match: i, value: 0 });
        p1PointWon.push({ match: i, value: 0, total: 0, won: 0 });
        p1InPlay.push({ match: i, value: 0, total: 0, won: 0 });
        p1InPlayWon.push({ match: i, value: 0, total: 0, won: 0 });
        p1AvgRally.push({ match: i, value: 0 });
      }

      if (p2Data[match]) {
        if (p2Data[match].pts > pointMax) pointMax = p2Data[match].pts;
        if (p2Data[match].avgRally > avgRallyMax) avgRallyMax = p2Data[match].avgRally;

        p2Point.push({ match: i, value: p2Data[match].pts });
        p2PointWon.push({
          match: i,
          value: Math.round((p2Data[match].ptsWon * 100) / p2Data[match].pts),
          total: p2Data[match].pts,
          won: p2Data[match].ptsWon
        });
        p2InPlay.push({
          match: i,
          value: Math.round((p2Data[match].inPlay * 100) / p2Data[match].pts),
          total: p2Data[match].pts,
          won: p2Data[match].inPlay
        });
        p2InPlayWon.push({
          match: i,
          value: Math.round((p2Data[match].inPlayWon * 100) / p2Data[match].inPlay),
          total: p2Data[match].inPlay,
          won: p2Data[match].inPlayWon
        });
        p2AvgRally.push({ match: i, value: p2Data[match].avgRally });
      } else {
        p2Point.push({ match: i, value: 0 });
        p2PointWon.push({ match: i, value: 0, total: 0, won: 0 });
        p2InPlay.push({ match: i, value: 0, total: 0, won: 0 });
        p2InPlayWon.push({ match: i, value: 0, total: 0, won: 0 });
        p2AvgRally.push({ match: i, value: 0 });
      }
    }
  };

  $: if (p1Data && p2Data) populateData(matches);
</script>

<h3 class="text-center text-base">Total Points</h3>
<SplitBarChart p1data={p1Point} p2data={p2Point} max={pointMax} neutral={true} />
<h3 class="text-center text-base">Points Won</h3>
<SplitBarChart p1data={p1PointWon} p2data={p2PointWon} percentage={true} />
<h3 class="text-center text-base">In Play</h3>
<SplitBarChart p1data={p1InPlay} p2data={p2InPlay} percentage={true} />
<h3 class="text-center text-base">In Play Won</h3>
<SplitBarChart p1data={p1InPlayWon} p2data={p2InPlayWon} percentage={true} />
<h3 class="text-center text-base">Average Rally Length</h3>
<SplitBarChart p1data={p1AvgRally} p2data={p2AvgRally} max={avgRallyMax} neutral={true} />
