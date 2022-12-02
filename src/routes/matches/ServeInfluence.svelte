<script lang="ts">
  import * as d3 from 'd3';

  export let player1: string;
  export let player2: string;
  export let match: { value: string; label: string; player1: string; player2: string };

  let p1Initials = player1
    .match(/(\b\S)?/g)
    .join('')
    .toUpperCase();
  let p2Initials = player2
    .match(/(\b\S)?/g)
    .join('')
    .toUpperCase();

  let chart: HTMLDivElement;
  let leg: HTMLDivElement;

  const width = 960;
  const height = 500;
  const margin = 5;
  const padding = 5;
  const adj = 30;

  const fetchServeInfluence = async (m: any) => {
    const res = await fetch('/api/matches/serve_influence', {
      method: 'POST',
      body: JSON.stringify(m.label)
    });
    console.log({ player1, player2, p1Initials, p2Initials });

    const data = await res.json();

    let slices: { id: string; values: { shot: number; influence: number }[] }[] = [];
    data
      .sort(
        (a: { player: number; serve: number }, b: { player: number; serve: number }) =>
          a.player - b.player || a.serve - b.serve
      )
      .forEach((element: any) => {
        slices.push({
          id: `${element['player'] === 1 ? p1Initials : p2Initials} ${
            element['serve'] === 1 ? '1st' : '2nd'
          }`,
          values: [
            { shot: 1, influence: element['won_1'] },
            { shot: 2, influence: element['won_2'] },
            { shot: 3, influence: element['won_3'] },
            { shot: 4, influence: element['won_4'] },
            { shot: 5, influence: element['won_5'] },
            { shot: 6, influence: element['won_6'] },
            { shot: 7, influence: element['won_7'] },
            { shot: 8, influence: element['won_8'] },
            { shot: 9, influence: element['won_9'] },
            { shot: 10, influence: element['won_10'] }
          ]
        });
      });
    console.log(slices);

    const xLabel = ['1+', '2+', '3+', '4+', '5+', '6+', '7+', '8+', '9+', '10+'];

    const svg = d3
      .select(chart)
      .append('svg')
      .attr('preserveAspectRatio', 'xMinYMin meet')
      .attr(
        'viewBox',
        '-' + adj * 2 + ' -' + adj + ' ' + (width + adj * 5) + ' ' + (height + adj * 3)
      )
      .style('padding', padding)
      .style('margin', margin)
      .classed('svg-content', true);

    const xScale = d3.scaleLinear().range([0, width]).domain([1, 10]);
    const yScale = d3.scaleLinear().rangeRound([height, 0]).domain([0, 100]);

    const yaxis = d3.axisLeft(yScale);
    const xaxis = d3.axisBottom(xScale).tickFormat((d, i) => xLabel[i]);

    svg
      .append('g')
      .attr('class', 'axis')
      .attr('transform', 'translate(0,' + height + ')')
      .style('font-size', '1.25rem')
      .call(xaxis);

    svg.append('g').attr('class', 'axis').style('font-size', '1.25rem').call(yaxis);

    const line = d3
      .line()
      .curve(d3.curveLinear)
      .x((d) => xScale(d.shot))
      .y((d) => yScale(d.influence));

    let id = 0;
    const ids = () => `line-${id++}`;

    const lines = svg.selectAll('lines').data(slices).enter().append('g');

    lines
      .append('path')
      .attr('class', ids)
      .attr('d', (d) => line(d.values))
      .style('fill', 'none')
      .style('stroke', '#ed3700')
      .style('stroke-width', '3px');

    d3.select('.line-1').style('stroke-dasharray', 6);
    d3.select('.line-2').style('stroke', 'steelblue');
    d3.select('.line-3').style('stroke', 'steelblue').style('stroke-dasharray', 6);

    lines
      .append('text')
      .attr('class', 'serie_label')
      .datum(function (d) {
        return {
          id: d.id,
          value: d.values[d.values.length - 1]
        };
      })
      .attr('transform', function (d) {
        return (
          'translate(' + (xScale(d.value.shot) + 10) + ',' + (yScale(d.value.influence) + 5) + ')'
        );
      })
      .attr('x', 5)
      .text(function (d) {
        return d.id;
      });

      d3.selectAll('.serie_label').style('color', '#e5e7eb');
  };

  $: {
    fetchServeInfluence(match);
  }
</script>

<h2 class="text-center text-xl text-gray-900 dark:text-gray-200">Serve Influence</h2>
<div bind:this={leg} class="flex" />
<div bind:this={chart} class="container" />

<style>
  .container :global(div) {
    font: 0.75rem sans-serif;
  }
</style>
