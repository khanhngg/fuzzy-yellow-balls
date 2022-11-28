<script>
  import { getContext } from "svelte";
  export let value;
  export let rank;
  export let i;
  const { names, scales, dimensions } = getContext("Chart");
  $: x = $scales.x(value);
  $: y = $scales.y(rank) + $dimensions.barMargin / 2;
  $: height = $dimensions.barHeight;
  const roundNumber = (d) => Math.round(d);
</script>

<div
  class="label"
  style="height: {height}px; transform: translate({x}px, {y}px);"
>
  <div class="inner">
    <p class="name text-gray-700 dark:text-gray-300">{names[i]}</p>
    <p class="value text-gray-700 dark:text-gray-300">
      {roundNumber(value)} <span class="font-bold text-gray-700 dark:text-gray-300">#{roundNumber(rank)}</span>
    </p>
  </div>
</div>

<style>
  .label {
    position: absolute;
    left: 0;
    top: 0;
  }

  .inner {
    transform: translate(-100%, 0);
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding-right: 0.9em;
    height: 100%;
  }

  p {
    margin: 0;
    font-size: 1em;
    text-align: right;
  }

  .name {
    font-weight: 600;
  }

  .value {
    font-size: 0.75em;
    font-feature-settings: "tnum" 1;
  }
</style>