<script>
  import Icon from '@iconify/svelte';
  import { createEventDispatcher } from "svelte";
  import { timer, elapsed } from "./timer.js";
  export let currentKeyframe = 0;
  export let keyframeCount = 0;
  export let duration = 1000;
  export let isEnabled = false;
  const dispatch = createEventDispatcher();
  const onReset = () => {
    currentKeyframe = 0;
    timer.reset();
  };

  $: if (isEnabled) currentKeyframe = Math.floor($elapsed / duration);
  $: if (currentKeyframe === keyframeCount) dispatch("end");
  $: isEnabled ? timer.start() : timer.stop();
</script>

<div>
  <button on:click="{() => (isEnabled = true)}">
    <Icon icon="material-symbols:play-circle-rounded" height="1.6em" />
  </button>
  <button on:click="{() => (isEnabled = false)}">
    <Icon icon="ic:round-pause-circle" height="1.6em" />
  </button>
  <button on:click="{onReset}">
    <Icon icon="material-symbols:replay-circle-filled-rounded" height="1.6em" />
  </button>
</div>

<style>
  div {
    display: flex;
    justify-content: center;
  }

  button {
    margin: 0.5em;
    padding: 0.5em;
    border: none;
    background: #ccc;
    border-radius: 4px;
    cursor: pointer;
  }
</style>