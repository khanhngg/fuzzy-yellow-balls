<script lang="ts">
  import type { PageData } from './$types';
  import { Button, Input, Tabs, TabItem } from 'flowbite-svelte';
  import Select from 'svelte-select';

  let player1: string;
  let player2: string;

  let matches: string[] | any[] = [];
  let selectedMatches: string[] | any[] = [];

  const getMatches = async () => {
    const res = await fetch(`/matches?player1=${player1}&player2=${player2}`);
    matches = await res.json();
    // console.log(matches);
  };

  const handleSelect = (event: any) => {
    selectedMatches = event.detail.map((value: { value: any }) => value.value);
  };
</script>

<svelte:head>
  <title>Matches</title>
  <meta name="description" content="Matches page" />
</svelte:head>

<div class="content">
  <h1>Matches</h1>
  <form on:submit|preventDefault={getMatches} class="">
    <div class="flex flex-row gap-3 justify-between items-center mb-3">
      <div class="w-full">
        <Input type="text" bind:value={player1} placeholder="Player 1" />
      </div>
      <div>VS</div>
      <div class="w-full">
        <Input type="text" bind:value={player2} placeholder="Player 2" />
      </div>
      <Button type="submit">Search</Button>
    </div>
  </form>
  {#if matches.length}
    <div class="mb-3">
      <label for="selectedMatches">Select matches (up to 3)</label>
      <Select items={matches} isMulti={true} on:select={handleSelect} />
    </div>
  {/if}
  {#if 0 < selectedMatches.length && selectedMatches.length < 4}
    <Tabs>
      <TabItem open>
        <span slot="title">Overview</span>
      </TabItem>
      <TabItem>
        <span slot="title">Serve</span>
      </TabItem>
      {#if selectedMatches.length === 1}
        <TabItem>
          <span slot="title">Serve Influence</span>
        </TabItem>
      {/if}

      <TabItem>
        <span slot="title">Return</span>
      </TabItem>
      <TabItem>
        <span slot="title">Net Points</span>
      </TabItem>
      <TabItem>
        <span slot="title">Key Points</span>
      </TabItem>
      {#if selectedMatches.length === 1}
        <TabItem>
          <span slot="title">Shot Direction</span>
        </TabItem>
      {/if}
    </Tabs>
  {/if}
</div>

<style>
  .content {
    width: 100%;
    max-width: var(--column-width);
    margin: var(--column-margin-top) auto 0 auto;
  }
</style>
