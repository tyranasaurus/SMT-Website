<script>
  export let text;
  export let textColor = "var(--bold-color)";
  export let bold = true;
  export let italic = false;
  export let boxed = false;
  export let size = 2.5;
  export let marginLeft = "";
  export let align = "center";
  export let className = "";
  export let padding = "";
</script>

<h1
  style="text-align: {align}; margin-left: {marginLeft}; color:{textColor}; font-weight:{bold
    ? 'bold'
    : 'normal'}; font-style: {italic ? 'italic' : 'normal'}; {size !== ''
    ? 'font-size: ' + size + 'em;'
    : ''}; padding: {padding};"
  class="{boxed ? 'boxed' : ''} {className}"
>
  {text}
</h1>

<style>
  .boxed {
    padding: 10px;
    border: 2px solid black;
  }
  h1 {
    margin: 0.1em;
  }
</style>
