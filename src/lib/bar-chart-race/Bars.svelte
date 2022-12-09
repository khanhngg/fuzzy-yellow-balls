<script>
  import { getContext } from "svelte";
  import Bar from "./Bar.svelte";
  const { data } = getContext("Chart");
  export let barCount;

  // Convert string to hex color code
  const hashCode = (str) => {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
        hash = str.charCodeAt(i) + ((hash << 5) - hash);
    }

    let color = '#';
    for (let i = 0; i < 3; i++) {
        let value = (hash >> (i * 8)) & 0xFF;
        color += ('00' + value.toString(16)).slice(-2);
    }

    return color;
  }
</script>

{#each $data as { points, rank, player_name }, i (i)}
  {#if rank <= barCount}
    <Bar value="{points}" rank="{rank}" fill="{hashCode(player_name)}" />
  {/if}
{/each}