<script>
  // LIBRARIES
  import { getContext } from 'svelte';
  import { line, curveCardinalClosed } from 'd3-shape';
  import { fade } from "svelte/transition";

  // DATA + CONTEXT
  const { data, width, height, xGet, config } = getContext('LayerCake');

  // CHART CONFIG
  export let fill = ['#fee14f', '#6f4ffe']
  export let fillOpacity = [0.35, 0.35]
  export let stroke = ['#fee14f', '#6f4ffe']
  export let strokeWidth = 2

  export let r = 4.5;
  export let circleFill = ['#fee14f', '#6f4ffe'];
  export let circleStroke = "#fff";
  export let circleStrokeWidth = 1;

  $: angleSlice = (Math.PI * 2) / $config.x.length;

  $: path = line()
    .curve(curveCardinalClosed)
    .x((d, i) => d * Math.cos(angleSlice * i - Math.PI / 2))
    .y((d, i) => d * Math.sin(angleSlice * i - Math.PI / 2));

  const duration = 500;

  let showLabel = [false, false]
</script>

<g
  transform="translate({ $width / 2 }, { $height / 2 })"
>
<!-- The curved path for each data points -->
  {#each $data as row, index}
    {@const xVals = $xGet(row)}
    <path
      in:fade="{{duration}}"
      class='path-line'
      d='{path(xVals)}'
      stroke="{stroke[index]}"
      stroke-width="{strokeWidth}"
      fill="{fill[index]}"
      fill-opacity="{fillOpacity[index]}"
      on:mouseover={() => {
        if (index == 0) {
          fillOpacity[0] = 0.75
          fillOpacity[1] = 0.1
          showLabel[0] = true
          showLabel[1] = false
        } else {
          fillOpacity[0] = 0.1
          fillOpacity[1] = 0.75
          showLabel[0] = false
          showLabel[1] = true
        }
      }}
      on:mouseout={() => {
        fillOpacity[0] = 0.35
        fillOpacity[1] = 0.35
        showLabel[0] = false
        showLabel[1] = false
      }}
    ></path>

    <!-- The dots for each data points -->
    {#each xVals as circleR, i}
      {@const thisAngleSlice = angleSlice * i - Math.PI / 2}
      <circle
        in:fade="{{duration : duration / 2}}"
        cx={circleR * Math.cos(thisAngleSlice)}
        cy={circleR * Math.sin(thisAngleSlice)}
        r="{r}"
        fill="{circleFill[index]}"
        stroke="{circleStroke}"
        stroke-width="{circleStrokeWidth}"
      ></circle>

      <!-- The label for each data point -->
      {#if showLabel[index]}
        <text
          in:fade="{{duration : duration / 2}}"
          out:fade="{{duration : duration / 2}}"
          x={circleR * Math.cos(thisAngleSlice) - 15}
          y={circleR * Math.sin(thisAngleSlice) - 10}
          font-size="0.8rem"
          class="fill-gray-800 stroke-gray-100 dark:fill-gray-100 dark:stroke-gray-900 stroke-[0.1px]"
        >
          {$data[index][$config.x[i]]}%
        </text>
      {/if}
    {/each}
  {/each}
</g>

<style>
  .path-line {
    stroke-linejoin: round;
    stroke-linecap: round;
  }
</style>