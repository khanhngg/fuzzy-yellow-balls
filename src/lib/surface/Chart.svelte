<script lang="ts">
  import * as d3 from 'd3';
  import { onMount } from 'svelte';
  const years = [...Array(23).keys()].map((i) => i + 2000);

  export let tour = 'atp';
  let surface = 'clay';
  let year = 2022;

  let chart: SVGSVGElement;

  let data: { player: string; surface: string; metric: string; value: number }[];

  const drawSurfaceChart = async (t: string, s: string, ye: number) => {
    chart.innerHTML = '';

    let rawData = (await import(`./../surface_stats_json/${t}_${s}_top10_${ye}.json`)).default;
    data = rawData.reduce(
      (
        total: { player: string; surface: string; metric: string; value: number }[],
        current: {
          player: string;
          win_rate: number;
          surface: string;
          '1st_rt_pt_won': number;
          '2nd_rt_pt_won': number;
          bp_convert: number;
          hld_rate: number;
          brk_rate: number;
          '1st_pt_won': number;
          '2nd_pt_won': number;
        }
      ) => [
        ...total,
        {
          player: current.player,
          surface: current.surface,
          metric: '1st Serve Return Point Won',
          value: current['1st_rt_pt_won']
        },
        {
          player: current.player,
          surface: current.surface,
          metric: '2nd Serve Return Point Won',
          value: current['2nd_rt_pt_won']
        },
        {
          player: current.player,
          surface: current.surface,
          metric: 'Break Point Convert',
          value: current.bp_convert
        },
        {
          player: current.player,
          surface: current.surface,
          metric: 'Break Percentage',
          value: current.brk_rate
        },
        {
          player: current.player,
          surface: current.surface,
          metric: '1st Serve Point Won',
          value: current['1st_pt_won']
        },
        {
          player: current.player,
          surface: current.surface,
          metric: '2nd Serve Point Won',
          value: current['2nd_pt_won']
        },
        {
          player: current.player,
          surface: current.surface,
          metric: 'Hold Percentage',
          value: current.hld_rate
        }
      ],
      []
    );

    const parameters = {
      groups: {
        key: 'metric',
        values: [
          '1st Serve Return Point Won',
          '2nd Serve Return Point Won',
          'Break Point Convert',
          'Break Percentage',
          '1st Serve Point Won',
          '2nd Serve Point Won',
          'Hold Percentage'
        ]
      },
      categories: { key: 'surface', values: ['clay', 'hard', 'grass'] },
      values: { key: 'value' }
    };
    // console.log(parameters);
    let margin = { top: 10, right: 130, bottom: 180, left: 40 },
      width = 992 - margin.left - margin.right,
      height = 700 - margin.top - margin.bottom;

    // create the svg object
    let svg = d3
      .select(chart)
      // .attr('width', width).attr('height', height);
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom);

    // let g = svg.append('g');
    let g = svg.append('g').attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

    let groups = parameters.groups.values;
    let categories = parameters.categories.values;

    let sumstat = groups.map((group) => {
      let e: {
        key: string;
        value: {
          key: string;
          value: {
            interQuantileRange: number;
            max: number;
            median: number;
            min: number;
            q1: number;
            q3: number;
          };
        }[];
      } = { key: '', value: [] };
      e.key = group;
      e.value = categories.map((cat) => {
        let f: {
          key: string;
          value: {
            interQuantileRange: number;
            max: number;
            median: number;
            min: number;
            q1: number;
            q3: number;
          };
        } = { key: '', value: { interQuantileRange: 0, max: 0, median: 0, min: 0, q1: 0, q3: 0 } };
        f.key = cat;
        let subData = data.filter(
          (d) =>
            d[parameters.categories.key] == cat && d[parameters.groups.key] == group && d.value > 0
        );

        // console.log(subData);

        let q1 = d3.quantile(subData.map((d) => d[parameters.values.key]).sort(d3.ascending), 0.25);
        let median = d3.quantile(
          subData.map((d) => d[parameters.values.key]).sort(d3.ascending),
          0.5
        );
        let q3 = d3.quantile(subData.map((d) => d[parameters.values.key]).sort(d3.ascending), 0.75);
        let interQuantileRange = q3 - q1;
        // let min = Math.min(...subData.map((value) => value.value));
        // let max = Math.max(...subData.map((value) => value.value));
        let min = q1 - 1.5 * interQuantileRange;
        let max = q3 + 1.5 * interQuantileRange;

        f.value = {
          q1: q1,
          median: median,
          q3: q3,
          interQuantileRange: interQuantileRange,
          min: min > 0 ? min : 0,
          max: max <= 100 ? max : 100
        };

        return f;
      });
    //   console.log(e);

      return e;
    });

    // Create the X scale
    let x = d3.scaleBand().range([0, width]).domain(groups);
    // Show the X scale
    g.append('g')
      .attr('transform', 'translate(0,' + height + ')')
      .call(d3.axisBottom(x))
      .attr('font-size', '.75rem')
      .selectAll('text')
      .attr('class', 'dark:fill-gray-200')
      .attr('y', 9)
      .attr('x', 9)
      .attr('transform', 'rotate(45)')
      .style('text-anchor', 'start');

    // Create the X cat scale
    let xCat = d3.scaleBand().range([0, x.bandwidth()]).domain(categories);
    // Create the color scale
    let color = d3
      .scaleOrdinal()
      .range(['chocolate', 'CornflowerBlue', 'ForestGreen'])
      .domain(categories);

    // Create the Y scale
    let y = d3.scaleLinear().domain([0, 100]).range([height, 0]);

    // Show the Y scale
    g.append('g')
      .call(d3.axisLeft(y).ticks(4))
      .attr('font-size', '.75rem')
      .selectAll('text')
      .attr('class', 'dark:fill-gray-200');

    g.selectAll('line').attr('class', 'dark:stroke-gray-200');
    g.selectAll('.domain').attr('class', 'dark:stroke-gray-200');

    // Create groups of boxplots
    let boxGroups = g
      .selectAll('groups')
      .data(sumstat)
      .enter()
      .append('g')
      .attr('transform', (d) => 'translate(' + x(d.key) + ', 0)')
      .attr('class', 'groups');

    // Rectangle for the main box
    let boxmargin = 10;
    boxGroups
      .selectAll('boxes')
      .data((d) => d.value)
      .enter()
      .append('rect')
      .attr('x', (d) => xCat(d.key) + boxmargin)
      .attr('y', (d) => y(d.value.q3))
      .attr('height', (d) => y(d.value.q1) - y(d.value.q3))
      .attr('width', xCat.bandwidth() - 2 * boxmargin)
      .style('fill', (d) => color(d.key))
      .attr('fill-opacity', 0.3)
      .attr('stroke', (d) => color(d.key));

    // Show the main vertical line
    boxGroups
      .selectAll('vertLines')
      .data((d) => d.value)
      .enter()
      .append('line')
      .attr('x1', (d) => xCat(d.key) + xCat.bandwidth() / 2)
      .attr('x2', (d) => xCat(d.key) + xCat.bandwidth() / 2)
      .attr('y1', (d) => y(d.value.min))
      .attr('y2', (d) => y(d.value.max))
      .attr('stroke', (d) => color(d.key));

    // Show the median
    boxGroups
      .selectAll('medianLines')
      .data((d) => d.value)
      .enter()
      .append('line')
      .attr('x1', (d) => xCat(d.key) + boxmargin)
      .attr('x2', (d) => xCat(d.key) + xCat.bandwidth() - boxmargin)
      .attr('y1', (d) => y(d.value.median))
      .attr('y2', (d) => y(d.value.median))
      .attr('stroke', (d) => color(d.key));

    // Add individual points
    groups.forEach(function (group) {
      g.selectAll('point')
        .data(data.filter((d) => d[parameters.groups.key] == group && d.value !== 0))
        .enter()
        .append('circle')
        .attr('cx', (d) => x(group) + xCat(d[parameters.categories.key]) + xCat.bandwidth() / 2)
        .attr('cy', (d) => y(d[parameters.values.key]))
        .attr('r', 4)
        .style('fill', (d) => color(d[parameters.categories.key]))
        .attr('opacity', 0.3)
        .attr('stroke', (d) => color(d[parameters.categories.key]));
    });

    // Add the legend
    let legend = g
      .append('g')
      .attr('transform', 'translate(' + width + ', 0)')
      .attr('text-anchor', 'end')
      .attr('font-size', '.75rem');

    let catLegends = legend
      .selectAll('g')
      .data(categories)
      .enter()
      .append('g')
      .attr('transform', (d, i) => 'translate(0,' + i * 30 + ')');

    catLegends
      .append('rect')
      .attr('x', 60)
      .attr('width', 20)
      .attr('y', 5)
      .attr('height', 20)
      .style('fill', (d) => color(d))
      .attr('fill-opacity', 0.3)
      .attr('stroke', (d) => color(d));

    catLegends
      .append('text')
      .attr('x', 50)
      .attr('y', 5 + 10)
      .attr('dominant-baseline', 'middle')
      .attr('text-align', 'right')
      .attr('font-size', '.75rem')
      .attr('class', 'dark:fill-gray-200')
      .text((d) => `${d.charAt(0).toUpperCase()}${d.slice(1)}`);

    return svg.node();
  };

  onMount(() => {
    year = 2022;
  });

  $: if (chart) drawSurfaceChart(tour, surface, year);
</script>

<label for="year" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
  >Select top players on</label
>
<select
  id="year"
  class="mb-3 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
  bind:value={surface}
>
  <option value={'clay'}>Clay court</option>
  <option value={'hard'}>Hard court</option>
  <option value={'grass'}>Grass court</option>
</select>
<label for="year" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
  >Select a year</label
>
<select
  id="year"
  class="mb-3 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
  bind:value={year}
>
  {#each years as y}
    <option value={y}>{y}</option>
  {/each}
</select>
<div class="w-full">
  <svg bind:this={chart} />
</div>
