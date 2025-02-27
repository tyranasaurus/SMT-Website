<script>
  export let url
  export let text = url
  export let textColor = 'var(--accent-color)'
  export let visitedColor = 'red'
  export let className = ''
  export let target = '_self'
</script>

<a
  href={url}
  style="--normal-color: {textColor}; --visited-color: {visitedColor}"
  class={className}
  {target}
>
  <slot>
    {text}
  </slot>
</a>

<style>
  a {
    color: var(--normal-color);
  }
  a:visited {
    color: var(--visited-color);
  }
</style>
