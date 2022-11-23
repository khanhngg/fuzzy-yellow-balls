<script lang="ts">
  import type { PageData } from './$types';
  export let data: PageData;
</script>

<svelte:head>
  <title>Matches</title>
  <meta name="description" content="Matches page" />
</svelte:head>

<div class="content">
  <h1 class="text-gray-900 dark:text-gray-200">Matches</h1>

</div>

<style>
  .content {
    width: 100%;
    max-width: var(--column-width);
    margin: var(--column-margin-top) auto 0 auto;
  }
  </style>