<script>
  export let color = 'black'
  export let bgcolor = 'inherit'
</script>

<div
  style="padding: 10px; border: 2px solid {color}; margin: 50px; background-color: {bgcolor}"
>
  <slot />
</div>
