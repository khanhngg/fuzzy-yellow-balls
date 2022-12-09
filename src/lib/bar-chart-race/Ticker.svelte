<script>
  import { timeFormat } from "d3-time-format";

  export let date;

  const formatDate = (value) => {
    return timeFormat("%b %Y")(new Date(value.replace(/-/g, '\/')));
    // convert date delimiter from "-" to "/" because JS Date strange behavior
  }
</script>

{#if date}
  <p class="text-gray-700 dark:text-gray-300">{formatDate(date)}</p>
{/if}

<style>
  p {
    position: absolute;
    bottom: 0;
    right: 0;
    margin: 0;
    font-size: 2.5em;
    font-weight: 900;
    font-feature-settings: "tnum" 1;
  }
</style>