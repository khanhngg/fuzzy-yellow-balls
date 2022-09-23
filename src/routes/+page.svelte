<script lang="ts">
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
	$: console.log(anotherData)
</script>

<svelte:head>
  <title>Home</title>
  <meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
  <h1>
    <span class="welcome">
      <picture>
        <source srcset="svelte-welcome.webp" type="image/webp" />
        <img src="svelte-welcome.png" alt="Welcome" />
      </picture>
    </span>

    to your new<br />SvelteKit app
  </h1>

  <h2>
    try editing <strong>src/routes/+page.svelte</strong>
  </h2>

  <!-- TODO: Remove/Update this - Example only -->
  <h2>Example D3 stuff</h2>
  <div bind:this={el} class="chart" />
</section>

<style>
  section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex: 1;
  }

  h1 {
    width: 100%;
  }

  .welcome {
    display: block;
    position: relative;
    width: 100%;
    height: 0;
    padding: 0 0 calc(100% * 495 / 2048) 0;
  }

  .welcome img {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    display: block;
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
