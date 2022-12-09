<script lang="ts">
  import * as d3 from 'd3';
  import * as d3sankey from 'd3-sankey';

  export let player1: string;
  export let player2: string;
  export let match: { value: string; label: string; player1: string; player2: string };

  let filter: boolean;

  let data: { hand: string; direction: string; outcome: string; value: number }[];
  const dimensions = ['hand', 'direction', 'outcome'];

  let chart: SVGSVGElement;
  let leg: HTMLDivElement;

  const width = 1080;
  const height = 640;
  const margin = 5;
  const padding = 5;
  const adj = 30;

  const fetchShotDirection = async (m: any, i: boolean) => {
    data = [];
    const player = match.player1 === player1 ? filter : !filter;
    const res = await fetch('/api/matches/shot_direction', {
      method: 'POST',
      body: JSON.stringify({ match: m.label, player1: player })
    });

    const { outcome } = await res.json();

    /*
    direction : {
      crosscourt
      down_middle
      down_the_line
      inside_in
      inside_out
    }

    outcome: {
      direction
      hand
      shots
      pt_ending
      shots_in_pts_lost
      shots_in_pts_won
    }
    */
    outcome.forEach((element: { [x: string]: any }) => {
      chart.innerHTML = '';
      const unresolve = element['shots'] - element['pt_ending'];
      let direction: string = element['direction']
        .split('_')
        .reduce(
          (total: string, current: string) =>
            `${total} ${current.charAt(0).toUpperCase()}${current.slice(1)}`,
          ''
        )
        .trim();
      data.push({
        hand: element['hand'],
        direction,
        outcome: 'Unresolve',
        value: unresolve
      });
      data.push({
        hand: element['hand'],
        direction,
        outcome: 'Lost',
        value: element['shots_in_pts_lost']
      });
      data.push({
        hand: element['hand'],
        direction,
        outcome: 'Won',
        value: element['shots_in_pts_won']
      });
    });

    console.log(createGraph());

    //{hand, direction, outcome}[]
    // const svg = html(`<svg width=${width} height=${height}></svg>`);
    chart = parsets();
  };

  const createGraph = () => {
    let index = -1;
    const nodes = [];
    const nodeByKey = new Map();
    const indexByKey = new Map();
    const links = [];

    for (const k of dimensions) {
      for (const d of data) {
        const key = JSON.stringify([k, d[k]]);
        if (nodeByKey.has(key)) continue;
        const node = { name: d[k] };
        nodes.push(node);
        nodeByKey.set(key, node);
        indexByKey.set(key, ++index);
      }
    }

    for (let i = 1; i < dimensions.length; ++i) {
      const a = dimensions[i - 1];
      const b = dimensions[i];
      const prefix = dimensions.slice(0, i + 1);
      const linkByKey = new Map();
      for (const d of data) {
        const names = prefix.map((k: string | number) => d[k]);
        const key = JSON.stringify(names);
        const value = d.value || 1;
        let link = linkByKey.get(key);
        if (link) {
          link.value += value;
          continue;
        }
        link = {
          source: indexByKey.get(JSON.stringify([a, d[a]])),
          target: indexByKey.get(JSON.stringify([b, d[b]])),
          names,
          value
        };
        links.push(link);
        linkByKey.set(key, link);
      }
    }

    return { nodes, links };
  };

  const parsets = () => {
    const sankey = d3sankey
      .sankey()
      .nodeSort((a, b) => a.name - b.name)
      .linkSort(null)
      .nodeWidth(4)
      .nodePadding(20)
      .extent([
        [0, 5],
        [width, height - 5]
      ]);
    const graph = createGraph();

    const svg = d3.select(chart).attr('viewBox', [0, 0, width, height]);

    const { nodes, links } = sankey({
      nodes: graph.nodes.map((d) => Object.assign({}, d)),
      links: graph.links.map((d) => Object.assign({}, d))
    });

    svg
      .append('g')
      .selectAll('rect')
      .data(nodes)
      .join('rect')
      .attr('class', 'dark:fill-gray-200')
      .attr('x', (d) => d.x0)
      .attr('y', (d) => d.y0)
      .attr('height', (d) => d.y1 - d.y0)
      .attr('width', (d) => d.x1 - d.x0)
      .append('title')
      .text((d) => `${d.name}\n${d.value.toLocaleString()}`);

    svg
      .append('g')
      .attr('fill', 'none')
      .selectAll('g')
      .data(links)
      .join('path')
      .attr('d', d3sankey.sankeyLinkHorizontal())
      .attr('stroke', (d) => color(d.names[0]))
      .attr('stroke-width', (d) => d.width)
      .attr('class', 'mix-blend-hard-light dark:mix-blend-lighten')
      // .attr('class', 'opacity-75')
      .append('title')
      .text((d) => `${d.names.join(' → ')}\n${d.value.toLocaleString()}`);

    svg
      .append('g')
      .style('font', '10px sans-serif')
      .selectAll('text')
      .data(nodes)
      .join('text')
      .attr('x', (d) => (d.x0 < width / 2 ? d.x1 + 6 : d.x0 - 6))
      .attr('y', (d) => (d.y1 + d.y0) / 2)
      .attr('dy', '0.35em')
      .attr('text-anchor', (d) => (d.x0 < width / 2 ? 'start' : 'end'))
      .attr('class', 'text-xl font-extrabold stroke-white stroke-[0.25] dark:font-[1000] fill-gray-900 dark:fill-gray-100 dark:stroke-black dark:stroke-[0.6]')
      .text((d) => d.name)
      .append('tspan')
      .text((d) => ` ${d.value.toLocaleString()}`);

    return svg.node();
  };

  $: {
    console.log(filter);
    if (match && filter !== undefined) fetchShotDirection(match, filter);
  }

  const color = d3
    .scaleOrdinal(['Forehand', 'Backhand', 'Slice'], ['#1f77b4', '#d62728', '#2ca02c'])
    .unknown('#ccc');
</script>

<h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Shot Direction</h2>
<label for="selectedMatches">Select Player</label>
<div class="text-gray-900 px-3 my-3">
  <select
    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    id="category"
    bind:value={filter}
  >
    <option value={true}>{player1}</option>
    <option value={false}>{player2}</option>
  </select>
</div>
<div class="w-full">
  <svg bind:this={chart} viewBox={`0,0,${width},${height}`} />
</div>
