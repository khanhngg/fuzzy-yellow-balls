<script>
  import { getContext } from "svelte";
  import Tick from "./Tick.svelte";
  const { scales } = getContext("Chart");
  $: ticks = $scales.x.ticks(5);
</script>

{#each ticks as value (value)}
  <Tick x="{$scales.x(value)}" value="{value}" />
{/each}