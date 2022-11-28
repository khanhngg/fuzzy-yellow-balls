<script>
  import { elapsed } from "./timer.js";
  export let value;
  export let currentKeyframe = 0;
  export let elapsedGap;
  export let max;

  const years = ['1990', '2000', '2010', '2020']
  const monthsInDecade = 120;
  const totalMonths = monthsInDecade * 3 + 32; // = 392 (32 months from 1/2020 to 8/2022)

  const handleChange = (event) => {
    let newKeyFrame = event.target.valueAsNumber;
    let newElapsedGap = elapsedGap * (newKeyFrame - currentKeyframe); 
    currentKeyframe = newKeyFrame;
    elapsed.update(e => e + newElapsedGap);
  };
</script>

<input
  id="minmax-range"
  type="range"
  max="{max}"
  value="{currentKeyframe}"
  on:input={handleChange}
  class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700 mt-6 mb-2"
>

<div class="ticker">
  {#each Array(totalMonths) as _, index (index)}
    <div class="tick text-gray-700 dark:text-gray-400">
      {#if index % (monthsInDecade + 1) == 0}
        <div class="tick-line border border-l border-gray-700 dark:border-gray-400"></div>
        <span>{years[Math.floor(index / 100)]}</span>
      {/if}
    </div>
  {/each}
</div>

<style>
  #minmax-range::-webkit-slider-thumb {
    -webkit-appearance: none;
    background: var(--accent-complement-color);
  }

  .ticker {
    --total-months: 392;
    display: grid;
    grid-template-columns: repeat(var(--total-months), auto);
    bottom: 0;
    left: 0;
    justify-content: space-between;
}

  .tick {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    font-size: 0.5rem;
    text-decoration: none;
  }

  .tick-line {
    height: 8px;
    border-width: 0.5px
  }
</style>