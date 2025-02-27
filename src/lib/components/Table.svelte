<script>
  export let data
  export let headerColor = 'var(--table-header-color)'
  export let rowColors = ['var(--table-color-1)', 'var(--table-color-2)']
  export let width = '100%'
  export let headerSize = 2
  export let textSize = 2.0
  export let cellPadding = 0
  export let cellPaddingRight = cellPadding
  export let includeHeader = true
  export let cellStyle = ''
  export let tableStyle = ''
  export let headerStyle = ''
  export let tableRowStyle = ''
  export let overallHeader = ''

  let windowWidth

  let columnCount = Object.values(Object.values(data)[0])[0]?.length

  if (windowWidth < 800) {
    textSize = 1.6
  }
</script>

<svelte:window bind:innerWidth={windowWidth} />

<table style="width: {width}; {tableStyle}">
  {#if overallHeader}
    <tr>
      <th
        colspan={columnCount}
        style="background-color: {headerColor}; font-size: {headerSize}em; {tableRowStyle}"
        >{overallHeader}</th
      >
    </tr>
  {/if}
  {#if includeHeader}
    <tr
      style="background-color: {headerColor}; font-size: {headerSize}em; {tableRowStyle}"
    >
      {#each Object.keys(data[0]) as heading}
        <th style={headerStyle}>{heading}</th>
      {/each}
    </tr>
  {/if}
  {#each Object.values(data) as row, i}
    <tr
      style="background-color: {rowColors[
        i % rowColors.length
      ]}; font-size: {textSize}em; {tableRowStyle}"
    >
      {#each Object.values(row) as cell}
        <td
          style="padding: {cellPadding}px; padding-right: {cellPaddingRight}px; {cellStyle}"
          >{@html cell}</td
        >
      {/each}
    </tr>
  {/each}
</table>

<style>
  th {
    padding: 5px;
  }

  @media only screen and (max-width: 800px) {
    td,
    th {
      font-size: 22px !important;
    }
  }
</style>
