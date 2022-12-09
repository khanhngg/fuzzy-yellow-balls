<script>
  import { getContext } from 'svelte';

  import QuadTree from './QuadTree.svelte';

  const { data, width, yScale, zScale, config } = getContext('LayerCake');

  export let offset = -20;

  export let dataset = undefined;

  const w = 150;
  const w2 = w / 2;

  const xKeysMap = {
    '1st_in': 'First Serve In',
    '1st_won': 'First Serve Won',
    '2nd_won': 'Second Serve Won',
    'bp_saved': 'Break Point Saved',
    'v1st_won': 'First Serve Return Won',
    'v2nd_won': 'Second Serve Return Won',
    'bp_cnvt': 'Break Point Convert',
    'hld_rate': 'Hold Percentage',
    'brk_rate': 'Break Point Percentage'
  };

  /* --------------------------------------------
   * Sort the keys by the highest value
   */
  function sortResult(result) {
    if (Object.keys(result).length === 0) return [];
    const rows = Object.keys(result).filter(d => d !== $config.x && d !== 'player' && d !== 'stats_id').map(key => {
      return {
        key,
        value: result[key]
      };
    }).sort((a, b) => b.value - a.value);

    return rows;
  }
</script>

<style>
  .tooltip {
    position: absolute;
    font-size: 13px;
    pointer-events: none;
    border: 1px solid #ccc;
    background: rgba(255, 255, 255, 0.85);
    transform: translate(-50%, -100%);
    padding: 10px;
    min-width: 250px;
    z-index: 15;
    pointer-events: none;
  }
  .line {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 1px;
    border-left: 1px dotted #666;
    pointer-events: none;
  }
  .tooltip,
  .line {
    transition: left 250ms ease-out, top 250ms ease-out;
  }
  .title {
    font-weight: bold;
  }
  .key {
    color: #999;
  }
</style>

<QuadTree
  dataset={dataset || $data}
  y='x'
  let:x
  let:y
  let:visible
  let:found
  let:e
>
  {@const foundSorted = sortResult(found)}
  {#if visible === true}
    <div
      style="left:{x}px;"
      class="line"></div>
    <div
      class="tooltip"
      style="
        width:{w}px;
        display: { visible ? 'block' : 'none' };
        top:{$yScale(foundSorted[8].value) + offset}px;
        left:{Math.min(Math.max(w2, x), $width - w2)}px;"
      >
        <div class="title text-center">Year {found[$config.x]}</div>
        {#each foundSorted as row}
          <div class="row mb-2">
            <span class="mr-2 px-2.5 py-0.5 rounded" style="background-color:{$zScale(row.key)}"></span>
            <span class="key">{xKeysMap[row.key]}:</span> {row.value}%
          </div>
        {/each}
    </div>
  {/if}
</QuadTree>