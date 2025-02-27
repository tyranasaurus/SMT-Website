<script>
  export let color = 'white'
  export let height = 60
  export let width = 60
</script>

<div style="background-color: {color}; height: {height}px; width: {width}px;">
  <slot />
</div>
