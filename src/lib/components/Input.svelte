<script>
  export let type = 'text'
  export let placeholder = ''
  export let placeholderColor = 'gray'
  export let placeholderOpacity = 0.2
  export let backgroundColor = 'orange'
</script>

<input
  {type}
  {placeholder}
  style="--placeholder-color:{placeholderColor}; --placeholder-opacity:{placeholderOpacity}; --background-color:{backgroundColor}"
/>

<style>
  ::placeholder {
    color: var(--placeholder-color);
    opacity: var(--placeholder-opacity);
    background-color: var(--background-color);
  }
</style>
