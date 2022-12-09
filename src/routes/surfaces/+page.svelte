<script lang="ts">
  import Chart from '$lib/surface/Chart.svelte';
  import { TabItem, Tabs } from 'flowbite-svelte';
  const years = [...Array(23).keys()].map((i) => i + 2000);

  let tour = 'atp';
  let surface = 'clay';
  let year = 2022;

  let data;

  const drawSurfaceChart = async (t: string, s: string, y: number) => {
    data = (await import(`./../../lib/surface_stats_json/${t}_${s}_top10_${y}.json`)).default;
  };
  $: drawSurfaceChart(tour, surface, year);
</script>

<svelte:head>
  <title>Surfaces</title>
  <meta name="description" content="Surfaces page" />
</svelte:head>

<div class="content">
  <h1 class="text-gray-900 dark:text-gray-200">Surfaces</h1>
  <Tabs
    class="w-full justify-center"
    activeClasses="inline-block text-sm font-medium text-center disabled:cursor-not-allowed py-3 px-4 text-white bg-violet-600 rounded-lg"
    inactiveClasses="inline-block text-sm font-medium text-center disabled:cursor-not-allowed py-3 px-4 text-gray-500 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-800 dark:hover:text-white border border-gray-200 dark:border-gray-700"
    divider={false}
  >
    <TabItem open>
      <span slot="title"> Association of Tennis Professionals (ATP)</span>
      <Chart tour={'atp'} />
    </TabItem>
    <TabItem>
      <span slot="title"> Association of Tennis Professionals (ATP)</span>
      <Chart tour={'wta'} />
    </TabItem>
  </Tabs>
</div>

<style>
  .content {
    width: 100%;
    max-width: var(--column-width);
    margin: var(--column-margin-top) auto 0 auto;
  }
</style>
