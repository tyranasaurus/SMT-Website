<script>
  export let direction = 'row'
  export let reverse = false
  export let wrap = true
  export let align = 'center'
  export let justify = 'center'
  export let indent
  export let size

  let alignMap = {
    start: 'flex-start',
    center: 'center',
    end: 'flex-end',
    stretch: 'stretch',
  }
  let justifyMap = {
    start: 'flex-start',
    center: 'center',
    end: 'flex-end',
    around: 'space-around',
    between: 'space-between',
    evenly: 'space-evenly',
  }
  let finalDirection = reverse ? 'reverse-' + direction : direction
  let finalWrap = wrap ? 'wrap' : 'nowrap'

  function nullFunction() {
    let x = 0
  }
  export let onClick = nullFunction
</script>

<div
  style="display: flex; flex-direction: {finalDirection}; flex-wrap: {finalWrap}; align-items: {alignMap[
    align
  ]}; justify-content: {justifyMap[
    justify
  ]}; padding-left: {indent}; font-size: {size}"
  on:click={onClick}
>
  <slot />
</div>
