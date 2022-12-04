<script lang="ts">
  import * as d3 from 'd3';
  export let p1data: any[];
  export let p2data: any[];
  export let max: number = 100;
  export let neutral: boolean = false;
  export let reverse: boolean = false;
  export let percentage: boolean = false;

  let container: HTMLDivElement;
  let p1div: HTMLDivElement;
  let p2div: HTMLDivElement;

  const drawChart = (p1: any[], p2: any[]) => {
    const allData = p1data.map((value, index) => [value, p2data[index]]);
    p1div.innerHTML = '';
    p2div.innerHTML = '';
    // console.log(allData);

    d3.select(p1div)
      .selectAll('div')
      .data(allData)
      .enter()
      .append('div')
      .attr('class', 'flex flex-col justify-center')
      .style('width', (d) => {
        return d[0].value === 0 ? '10px' : `${((d[0].value / max) * container.clientWidth) / 2}px`;
      })
      .style('height', '33px')
      .style('background-color', (d) => {
        return (
          !neutral &&
          (reverse ? d[0].value > d[1].value && 'dimgrey' : d[0].value < d[1].value && 'dimgrey')
        );
      })
      .text((d) => {
        return d[0].value === 0
          ? '0'
          : percentage
          ? `${d[0].value}% (${d[0].won}/${d[0].total})`
          : d[0].value;
      });

    d3.select(p2div)
      .selectAll('div')
      .data(allData)
      .enter()
      .append('div')
      .attr('class', 'flex flex-col justify-center')
      .style('width', (d) => {
        return d[1].value === 0 ? '10px' : `${((d[1].value / max) * container.clientWidth) / 2}px`;
      })
      .style('height', '33px')
      .style('background-color', (d) => {
        return (
          !neutral &&
          (reverse ? d[0].value < d[1].value && 'dimgrey' : d[0].value > d[1].value && 'dimgrey')
        );
      })
      .text((d) => {
        return d[1].value === 0
          ? '0'
          : percentage
          ? `${d[1].value}% (${d[1].won}/${d[1].total})`
          : d[1].value;
      });
  };

  $: {
    // console.log(p1data, p2data);
    if (p1data && p2data && p1div && p2div) {
      drawChart(p1data, p2data);
    }
  }
</script>

<div class="flex justify-center" bind:this={container}>
  <div class="chart-container">
    <div bind:this={p1div} class="chart-p1 flex flex-col items-end text-gray-900" />
  </div>
  <div class="chart-container">
    <div bind:this={p2div} class="chart-p2 flex flex-col items-start text-gray-900" />
  </div>
</div>

<style>
  .chart-container {
    width: 50%;
  }
  .chart-p1 :global(div) {
    font: 0.75rem sans-serif;
    background-color: steelblue;
    text-align: left;
    padding: 3px;
    margin: 1px;
    color: white;
  }
  .chart-p2 :global(div) {
    font: 0.75rem sans-serif;
    background-color: steelblue;
    text-align: right;
    padding: 3px;
    margin: 1px;
    color: white;
  }
</style>
