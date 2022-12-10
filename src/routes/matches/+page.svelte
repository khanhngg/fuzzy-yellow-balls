<script lang="ts">
  import Icon from '@iconify/svelte';
  import { Button, Input, Tabs, TabItem } from 'flowbite-svelte';
  import Select from 'svelte-select';
  import Overview from './Overview.svelte';
  import Serve from './Serve.svelte';
  import ServeInfluence from './ServeInfluence.svelte';
  import Return from './Return.svelte';
  import NetPoint from './NetPoint.svelte';
  import ShotDirection from './ShotDirection.svelte';
  import loadOptions from '$lib/players';

  let player1: string;
  let player2: string;

  let matches: any[] = [];
  let results: any[] = [];
  let selectedMatches: any[] = [];

  const getMatches = async () => {
    matches = [];
    selectedMatches = [];
    const res = await fetch(`/matches?player1=${player1}&player2=${player2}`);
    const data = await res.json();

    // console.log(data);
    if (data.length) {
      if (data[0]['Player_1'].toLowerCase().includes(player1.toLowerCase())) {
        player1 = data[0]['Player_1'];
        player2 = data[0]['Player_2'];
      } else {
        player1 = data[0]['Player_2'];
        player2 = data[0]['Player_1'];
      }

      matches = data.map((element: { match_id: any; Player_1: any; Player_2: any }) => {
        return {
          value: element.match_id,
          label: element.match_id,
          player1: element.Player_1,
          player2: element.Player_2
        };
      });
    }
  };

  const handleSelect = (event: any) => {
    if (event.detail) {
      selectedMatches = event.detail;
      fetchMetches(
        event.detail.map((value: { label: any }) => value.label).sort(),
        player1,
        player2
      );
    } else {
      selectedMatches = [];
      results = [];
    }
  };

  const selectPlayer = (
    { detail }: { detail: { index: number; label: string; value: string } },
    player: number
  ) => {
    // console.log({ detail, player });
    switch (player) {
      case 1:
        player1 = detail.value;
        break;
      case 2:
        player2 = detail.value;
        break;
      default:
        break;
    }
  };

  const fetchMetches = async (matches: any, player1: string, player2: string) => {
    const res = await fetch('/api/matches/search', {
      method: 'POST',
      body: JSON.stringify({ matches, player1, player2 })
    });
    results = (await res.json()).sort((a, b) => a.match_id - b.match_id);
    // console.log(results);
  };
</script>

<svelte:head>
  <title>Matches</title>
  <meta name="description" content="Matches page" />
</svelte:head>

<div class="content text-gray-900 dark:text-gray-200">
  <h1 class="text-gray-900 dark:text-gray-200">Matches</h1>
  <form on:submit|preventDefault={getMatches} class="">
    <div class="flex flex-row gap-3 justify-between items-center mb-3">
      <div class="w-full text-gray-900">
        <Select
          {loadOptions}
          on:select={(e) => selectPlayer(e, 1)}
          placeholder="Search for player"
        />
        <!-- <Input type="text" bind:value={player1} placeholder="Player 1" /> -->
      </div>
      <div>VS</div>
      <div class="w-full text-gray-900">
        <Select
          {loadOptions}
          on:select={(e) => selectPlayer(e, 2)}
          placeholder="Search for player"
        />
        <!-- <Input type="text" bind:value={player2} placeholder="Player 2" /> -->
      </div>
      <Button type="submit" btnClass="text-center font-medium focus:ring-4 focus:outline-none inline-flex items-center justify-center px-5 py-2.5 text-sm bg-violet-700 hover:bg-violet-800 focus:ring-violet-300 dark:bg-violet-600 dark:hover:bg-violet-700 dark:focus:ring-violet-800 rounded-lg text-white bg-violet-600">Search</Button>
    </div>
  </form>
  {#if matches.length}
    <div class="mb-3">
      <label for="selectedMatches">Select matches (up to 3)</label>
      <div class="text-gray-700">
        <Select items={matches} isMulti={true} on:select={handleSelect} />
      </div>
    </div>
  {/if}
  {#if 0 < results.length && results.length < 4}
    <div class="flex flex-col flex-start items-center">
      {#each results as result}
        <div class="text-xl">{result.match_id}</div>
        <div class="w-full flex flex-row justify-between mb-3 text-lg">
          <div style={`visibility: ${result.winner === player2 && 'hidden'};`}>
            <Icon icon="charm:trophy" color="lime" />
          </div>
          <div>{result.score}</div>
          <div style={`visibility: ${result.winner === player1 && 'hidden'};`}>
            <Icon icon="charm:trophy" color="lime" />
          </div>
        </div>
      {/each}
    </div>
  {/if}
  {#if 0 < selectedMatches.length && selectedMatches.length < 4}
    <Tabs
      class="w-full justify-center"
      contentClass="p-4 mt-4"
      activeClasses="inline-block text-sm font-medium text-center disabled:cursor-not-allowed py-3 px-4 text-white bg-violet-600 rounded-lg"
      inactiveClasses="inline-block text-sm font-medium text-center disabled:cursor-not-allowed py-3 px-4 text-gray-500 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-800 dark:hover:text-white border border-gray-200 dark:border-gray-700"
      divider={false}
    >
      <TabItem open>
        <span slot="title">Overview</span>
        <Overview {player1} {player2} matches={selectedMatches} />
      </TabItem>
      <TabItem>
        <span slot="title">Serve</span>
        <Serve {player1} {player2} matches={selectedMatches} />
      </TabItem>
      {#if selectedMatches.length === 1}
        <TabItem>
          <span slot="title">Serve Influence</span>
          <ServeInfluence {player1} {player2} match={selectedMatches[0]} />
        </TabItem>
      {/if}

      <TabItem>
        <span slot="title">Return</span>

        <Return
          {player1}
          {player2}
          matches={selectedMatches
            .sort((a, b) => a.label - b.label)
            .reduce(
              (obj, item) => ({
                ...obj,
                [item.value]: { player1: item.player1, player2: item.player2 }
              }),
              {}
            )}
        />
      </TabItem>
      <TabItem>
        <span slot="title">Net Points</span>
        <NetPoint
          {player1}
          {player2}
          matches={selectedMatches
            .sort((a, b) => a.label - b.label)
            .reduce(
              (obj, item) => ({
                ...obj,
                [item.value]: { player1: item.player1, player2: item.player2 }
              }),
              {}
            )}
        />
      </TabItem>
      {#if selectedMatches.length === 1}
        <TabItem>
          <span slot="title">Shot Direction</span>
          <ShotDirection {player1} {player2} match={selectedMatches[0]} />
        </TabItem>
      {/if}
    </Tabs>
  {/if}
</div>

<style>
  .content {
    width: 100%;
    max-width: 100vw;
    margin: var(--column-margin-top) auto 0 auto;
  }
</style>
