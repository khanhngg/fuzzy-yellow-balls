<script lang="ts">
  // LIBRARIES
  import { scaleOrdinal } from 'd3-scale';

  // COMPONENTS
  import { Tabs, TabItem, Alert } from 'flowbite-svelte';
  import Select from 'svelte-select';
  import { LayerCake, Svg, Html } from 'layercake';

  import Axis from '$lib/radar-chart/Axis.svelte';
  import Chart from '$lib/radar-chart/Chart.svelte';

  import MultilineChart from '$lib/multiline-chart/MultilineChart.svelte';
  import AxisX from '$lib/multiline-chart/AxisX.svelte';
  import AxisY from '$lib/multiline-chart/AxisY.svelte';
  import SharedTooltip from '$lib/multiline-chart/SharedTooltip.svelte';

  // API
  import loadOptions from '$lib/players';

  // DATA
  // chart configuration
  const xKeys = ['1st_in','1st_won','2nd_won','bp_saved','v1st_won','v2nd_won','bp_cnvt','hld_rate','brk_rate'];
  const xKeyNames = ['First Serve In','First Serve Won','Second Serve Won','Break Point Saved','First Serve Return Won','Second Serve Return Won','Break Point Convert','Hold Percentage','Break Point Percentage'];

  // years from 2000-2022
  let years = Array.from({ length: 22 } , (_, i) => ({ value: i + 2000 , label: i + 2000 }))
  let selectedYear;

  let colors = ['#fee14f', '#6f4ffe']

  // players data
  let player1: string;
  let player2: string;
  
  let players = [];
  let alerts = [false, false]
  
  let thePlayerName: string;
  let thePlayerStats = [];

  const xKey = 'year';
  const yKey = 'value';
  const zKey = 'stats';

  const seriesColors = ['#ffe4b8', '#ffb3c0', '#ff7ac7', '#ff00cc', '#4287f5', '#6fed9c', '#ffc859', '#ff4f61', '#c679fc'];

  let dataLong;
  let flatten;

  const selectSinglePlayer = async (
    { detail }: { detail: { index: number; label: string; value: string } },
  ) => {
      thePlayerName = detail.value;
      thePlayerStats = await fetchPlayerStatsAllTime(thePlayerName)

      dataLong = xKeys.map(key => {
        return {
          [zKey]: key,
          values: thePlayerStats.map(d => {
            return {
              [xKey]: d[xKey],
              [zKey]: key,
              [yKey]: d[key],
            };
          })
        };
      })

      console.log(dataLong)
      flatten = thePlayerStats => thePlayerStats.reduce((memo, group) => {
        return memo.concat(group.values);
      }, [])
    };

  const selectPlayer = async (
    { detail }: { detail: { index: number; label: string; value: string } },
    player: number
  ) => {
    switch (player) {
      case 1:
        player1 = detail.value;
        let fetchedPlayer1 = await fetchPlayerStats(player1, selectedYear)
        if (fetchedPlayer1) {
          players[0] = fetchedPlayer1
          alerts[0] = false
        } else if (players.length == 1) {
          players = []
          alerts[0] = true
        } else {
          players.splice(0, 1)
          alerts[0] = true
        }
        break;
      case 2:
        player2 = detail.value;
        let fetchedPlayer2 = await fetchPlayerStats(player2, selectedYear)
        if (fetchedPlayer2) {
          players[1] = fetchedPlayer2
          alerts[1] = false
        } else {
          players.splice(1, 1)
          alerts[1] = true
        }
        break;
      default:
        break;
    }
  };

  const fetchPlayerStats = async (player: string, year: number) => {
    const res = await fetch('/api/players/stats', {
      method: 'POST',
      body: JSON.stringify({player: player, year: year})
    });
    const data = await res.json();
    return data[0]
  }

  const fetchPlayerStatsAllTime = async (player: string) => {
    const res = await fetch('/api/players/stats-all-time', {
      method: 'POST',
      body: JSON.stringify({player: player})
    });
    const data = await res.json();
    return data
  }

  const handleSelectYear = async (e) => {
    selectedYear = e.detail.value
    if (players.length > 0 && selectedYear) {
      let fetchedPlayer1 = await fetchPlayerStats(player1, selectedYear)
      if (fetchedPlayer1) {
          players[0] = fetchedPlayer1
          alerts[0] = false
        } else if (players.length == 1) {
          players = []
          alerts[0] = true
        } else {
          players.splice(0, 1)
          alerts[0] = true
        }
    }
    
    if (players.length > 0 && selectedYear) {
      let fetchedPlayer2 = await fetchPlayerStats(player2, selectedYear)
      console.log('fetchedPlayer2='+fetchedPlayer2)
      if (fetchedPlayer2) {
        players[1] = fetchedPlayer2
        alerts[1] = false
      } else {
        players.splice(1, 1)
        alerts[1] = true
      }
    }
  }
</script>

<svelte:head>
  <title>Players</title>
  <meta name="description" content="Players page" />
</svelte:head>

<div class="content">
  <h1 class="text-gray-700 dark:text-gray-200 pb-6">
    Players
  </h1>

  <Tabs
    class="w-full justify-center"
    contentClass="p-4 mt-4"
    activeClasses="inline-block text-sm font-medium text-center disabled:cursor-not-allowed py-3 px-4 text-white bg-violet-600 rounded-lg"
    inactiveClasses="inline-block text-sm font-medium text-center disabled:cursor-not-allowed py-3 px-4 text-gray-500 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-800 dark:hover:text-white border border-gray-200 dark:border-gray-700"
    divider={false}
  >
    <TabItem open>
      <span slot="title">Skills Comparison</span>

      <!-- Year dropdown -->
      <label for="years" class="block mb-2 text-sm font-medium text-gray-800 dark:text-gray-200">
        Select a year
      </label>
      <Select
        id="years"
        placeholder="Select year..."
        items={years}
        on:select={handleSelectYear}
      />

      <!-- Players autosuggest search -->
      {#if selectedYear}
        <label class="block mt-3 mb-2 text-sm font-medium text-gray-800 dark:text-gray-200">
          1st player:
        </label>
        <Select
        {loadOptions}
        on:select={(e) => selectPlayer(e, 1)}
        placeholder="Search for player"
        />

        {#if players.length > 0 && players[0]}
          <label class="block mt-3 mb-2 text-sm font-medium text-gray-800 dark:text-gray-200">
            2nd player:
          </label>
          <Select
            {loadOptions}
            on:select={(e) => selectPlayer(e, 2)}
            placeholder="Search for player"
          />
        {/if}
      {/if}

      <!-- Alerts -->
      {#each alerts as alert, index}
        {#if alert}
          <Alert color="red" dismissable class="mt-3 mb-3">
            <span slot="icon"><svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"></path></svg>
            </span>
            Player <strong>{index == 0 ? player1 : player2}</strong> not found for year <strong>{selectedYear}</strong>. Please select a different player and/or year.
          </Alert>
        {/if}
      {/each}

      <!-- Chart -->
      {#each players as player, index}
        <div class="mt-3 mb-3">
          <span class="mr-2 px-2.5 py-0.5 rounded" style="background-color:{colors[index]}"></span>
          <span class="text-gray-800 dark:text-gray-300">
            {player.player}
          </span>
        </div>
      {/each}

      {#if players.length > 0}
        <div class="chart-container">
          <LayerCake
            padding={{ top: 100, right: 0, bottom: 7, left: 0 }}
            x={xKeys}
            xDomain={[0, 100]}
            xRange={({ height }) => [0, height]}
            data={players}
          >
            <Svg>
              <Axis />
              <Chart />
            </Svg>
          </LayerCake>
        </div>
      {/if}
    </TabItem>
    <TabItem>
      <span slot="title">Stats Over the Years</span>
      <label class="block mb-2 text-sm font-medium text-gray-800 dark:text-gray-200">
        Player:
      </label>
      <Select
        {loadOptions}
        on:select={(e) => selectSinglePlayer(e)}
        placeholder="Search for player"
      />

      <!-- Chart -->
      {#if thePlayerStats.length > 0}
        <p class="mt-6 text-gray-700 dark:text-gray-200 pb-6 text-center text-xl text-bold">
          Performance stats over the years for {thePlayerName}
        </p>

        <!-- Legends -->
        <div class="mt-6 legend-container">
          {#each xKeyNames as key, index }
            <div class="legend-item">
              <span class="mr-2 px-2.5 py-0.5 rounded" style="background-color:{seriesColors[index]}"></span>
              <span class="text-gray-800 dark:text-gray-300">
                {key}
              </span>
            </div>
          {/each}
        </div>

        <div class="chart-container">
          <LayerCake
            padding={{ top: 50, right: 10, bottom: 20, left: 25 }}
            x={xKey}
            y={yKey}
            z={zKey}
            yDomain={[0, 100]}
            zScale={scaleOrdinal()}
            zRange={seriesColors}
            flatData={flatten(dataLong)}
            data={dataLong}
          >
            <Svg>
              <AxisX
                gridlines={false}
                ticks={thePlayerStats.map(d => d[xKey]).sort((a, b) => a - b)}
                snapTicks={true}
                tickMarks={true}
              />
              <AxisY
                ticks={4}
              />
              <MultilineChart />
            </Svg>
        
            <Html>
              <SharedTooltip
                dataset={thePlayerStats}
              />
            </Html>
          </LayerCake>
        </div>
      {/if}
    </TabItem>
  </Tabs>
</div>

<style>
  .content {
    width: 100%;
    max-width: var(--column-width);
    margin: var(--column-margin-top) auto 0 auto;
    min-height: 120vh;
  }

  .chart-container {
    width: 100%;
    height: 300px;
  }

  .chart-container :global(.layercake-container) {
    top: 4rem;
  }

  .legend-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    row-gap: 10px;
    align-content: space-around;
  }

  .legend-item {
    flex-basis: 25%;
  }
</style>
