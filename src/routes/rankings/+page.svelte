<script lang="ts">
  import type { PageData } from './$types';
  // DATA
  export let data: PageData;
  // console.log(data);
  const { atp, wta } = data;
  // import atp from '$lib/data/rankings_atp/atp_rankings_all.json';
  // import wta from '$lib/data/rankings_wta/wta_rankings_all.json';

  // COMPONENTS
  import { Tabs, TabItem } from 'flowbite-svelte';
  import Chart from '$lib/bar-chart-race/Chart.svelte';
</script>

<svelte:head>
  <title>Rankings</title>
  <meta name="description" content="Rankings page" />
</svelte:head>

<section class="content">
  <h1 class="text-gray-700 dark:text-gray-200 pb-6">Rankings</h1>

  <Tabs
    class="w-full justify-center"
    activeClasses="inline-block text-sm font-medium text-center disabled:cursor-not-allowed py-3 px-4 text-white bg-violet-600 rounded-lg"
    inactiveClasses="inline-block text-sm font-medium text-center disabled:cursor-not-allowed py-3 px-4 text-gray-500 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-800 dark:hover:text-white border border-gray-200 dark:border-gray-700"
    divider={false}
  >
    <TabItem open>
      <span slot="title">Association of Tennis Professionals (ATP)</span>
      <Chart keyframes={atp} />
    </TabItem>
    <TabItem>
      <span slot="title">Women's Tennis Association (WTA)</span>
      <Chart keyframes={wta} />
    </TabItem>
  </Tabs>
</section>

<style>
  .content {
    width: 100%;
    max-width: var(--column-width);
    margin: var(--column-margin-top) auto 0 auto;
  }
</style>
