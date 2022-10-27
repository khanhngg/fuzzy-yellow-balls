<script lang="ts">
  import { Card } from 'flowbite-svelte';
  import Icon from '@iconify/svelte';
</script>

<svelte:head>
  <title>Home</title>
  <meta name="description" content="Fuzzy Yellow Balls Homepage" />
</svelte:head>

<section>
  <h1>
    Explore interactive tennis visualizations
  </h1>
</section>

<section class="grid gap-4 grid-cols-2 grid-rows-2">
  <Card class="text-center" size="md" href="/players">
    <Icon icon="map:tennis" class="icon" />
    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Players</h5>
    <p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight">
      View and compare player(s) skills chart
    </p>
  </Card>
  <Card class="text-center" size="md" href="/matches">
    <Icon icon="ci:tennis-match" class="icon" />
    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Matches</h5>
    <p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight">
      View and compare matches stats between 2 players
    </p>
  </Card>
  <Card class="text-center" size="md" href="/surfaces">
    <Icon icon="game-icons:tennis-court" class="icon" />
    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Surfaces</h5>
    <p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight">
      See how top players one each surfaces perform
    </p>
  </Card>
  <Card class="text-center" size="md" href="/rankings">
    <Icon icon="fa6-solid:chart-bar" class="icon" />
    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Rankings</h5>
    <p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight">
      See the top players per week
    </p>
  </Card>
</section>

<style>
  h1 {
    width: 100%;
    margin: var(--column-margin-top) auto;
  }

  section :global(.icon) {
    font-size: 69px;
    margin: 10px auto;
  }
</style>
