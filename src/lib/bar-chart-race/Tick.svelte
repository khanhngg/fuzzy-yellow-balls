<script>
  import { fade } from "svelte/transition";
  export let value;
  export let x;
  const duration = 250;
</script>

<div
  transition:fade="{{ duration }}"
  class="tick"
  style="transform: translate({x}px, 0);"
>
  <div class="line bg-white dark:bg-gray-800"></div>
  <p class="value">{value}</p>
</div>

<style>
  .tick {
    position: absolute;
    height: 100%;
    top: 0;
    left: 0;
  }

  .line {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 1px;
    opacity: 0.5;
  }

  .value {
    margin: 0;
    transform: translate(-50%, -100%);
    font-size: 0.75em;
    color: #666;
    font-feature-settings: "tnum" 1;
  }
</style>