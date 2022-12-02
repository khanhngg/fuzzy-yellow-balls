<script lang="ts">
  // import type { PageData } from './$types';
  // export let data: PageData;
  // import testdata from '$lib/data/rankings_atp/atp_rankings_all.csv?raw'
  import { onMount } from 'svelte';
  import * as d3 from 'd3';
  let data = [30, 86, 168, 281, 303, 365];

  let el;

  onMount(() => {
    d3.select(el)
      .selectAll('div')
      .data(data)
      .enter()
      .append('div')
      .style('width', function (d) {
        return d + 'px';
      })
      .text(function (d) {
        return d;
      });
  });

  // TODO: Example only
  let anotherData;
  onMount(
    async () => {
      // anotherData = await d3.csv('https://raw.githubusercontent.com/JeffSackmann/tennis_MatchChartingProject/master/charting-m-matches.csv')
      anotherData = await d3.csv('../data/data.csv')
    }
  )
  // $: console.log(anotherData)
  // $: console.log(testdata) // todo use papaparse
</script>

<svelte:head>
  <title>Rankings</title>
  <meta name="description" content="Rankings page" />
</svelte:head>

<div class="content">
  <h1 class="text-gray-900 dark:text-gray-200">
    Rankings
  </h1>

  <!-- TODO: Remove/Update this - Example only -->
  <h2>Example D3 stuff</h2>
  <div bind:this={el} class="chart" />
</div>

<style>
  .content {
    width: 100%;
    max-width: var(--column-width);
    margin: var(--column-margin-top) auto 0 auto;
  }

  /* TODO: Example only */
  .chart :global(div) {
    font: 10px sans-serif;
    background-color: steelblue;
    text-align: right;
    padding: 3px;
    margin: 1px;
    color: white;
  }
</style>