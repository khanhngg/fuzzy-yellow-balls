<script>
  // LIBRARIES
  import { scaleLinear } from "d3";
  import { setContext } from "svelte";
  import { writable } from "svelte/store";
  import { tweened } from "svelte/motion";

  // COMPONENTS
  import Timer from "./Timer.svelte";
  import Slider from "./Slider.svelte";
  import Bars from "./Bars.svelte";
  import Axis from "./Axis.svelte";
  import Labels from "./Labels.svelte";
  import Ticker from "./Ticker.svelte";

  // PROPS
  export let keyframes = [];

  // CONSTANTS
  const duration = 600; // ms between keyframes
  const barCount = 10; // how many bars to show
  const barMargin = 4; // space between bars

  const keyframeCount = keyframes.length; // number of keyframes
  const names = keyframes[0][1].map((d) => d.player_name); // all players' names

  const dimensions = writable({});
  const scales = writable({});
  const data = tweened(null, { duration });
  const xMax = tweened(null, { duration });

  let figureWidth = 0;
  let figureHeight = 0;
  let currentKeyframe = 0;
  let isEnabled = false;

  // update dimensions
  $: width = figureWidth;
  $: height = figureHeight;
  $: barHeight = height / barCount - barMargin;

  // update current data
  $: isEnabled = currentKeyframe < keyframeCount;
  $: frameIndex = Math.min(currentKeyframe, keyframeCount - 1);
  $: frame = keyframes[frameIndex];
  $: keyframeDate = frame[0];
  $: keyframeData = frame[1];
  $: currentData = names.map((name) => ({
    ...keyframeData.find((d) => d.player_name == name),
  }))

  // update stores and context
  $: data.set(currentData);

  $: dimensions.set({
    width,
    height,
    barHeight,
    barMargin,
  });

  $: xMax.set(Math.max(...keyframeData.map((d) => d.points)));

  $: scales.set({
    x: scaleLinear().domain([0, $xMax]).range([0, $dimensions.width]),
    y: scaleLinear().domain([1, barCount + 1]).range([0, $dimensions.height]), // y=[1, barCount+1] because rank starts from 1
  });

  $: chartContext = { dimensions, scales, data, names };
  $: setContext("Chart", chartContext);
</script>

{#if keyframes}
  <figure bind:offsetWidth="{figureWidth}" bind:offsetHeight="{figureHeight}" class="mt-6">
    <div class="bars">
      <Bars barCount="{barCount}" />
    </div>

    <div class="axis">
      <Axis />
    </div>

    <div class="labels">
      <Labels barCount="{barCount}" />
    </div>

    <div class="ticker">
      <Ticker date="{keyframeDate}" />
    </div>
  </figure>

  <Slider bind:currentKeyframe max="{keyframeCount}" value="{keyframeDate}" elapsedGap="{duration}" />

  <Timer
    bind:currentKeyframe
    keyframeCount="{keyframeCount}"
    duration="{duration}"
    isEnabled="{isEnabled}"
    on:end="{() => (isEnabled = false)}"
  />
{/if}

<style>
  figure {
    display: block;
    position: relative;
    width: 100%;
    height: 50vh;
    min-height: 420px;
    user-select: none;
  }
  figure > * {
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
  }
  .axis {
    overflow: visible;
  }
</style>