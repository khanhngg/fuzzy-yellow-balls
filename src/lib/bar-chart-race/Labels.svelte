<script>
  import { getContext } from "svelte";
  import Label from "./Label.svelte";
  const { data } = getContext("Chart");
  export let barCount = 10;
</script>

{#each $data as { points, rank }, i (i)}
  {#if rank <= barCount}
    <Label value="{points}" rank="{rank}" i="{i}" />
  {/if}
{/each}