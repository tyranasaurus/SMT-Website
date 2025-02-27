<script>
  export let text
  export let textColor = 'black'
  export let align = 'left'
  export let bold = false
  export let italic = false
  export let boxed = false
  export let fontWeight = 400
  export let size = ''
  export let pxsize = ''
  export let marginLeft = ''
  export let marginTop = ''
</script>

<p
  style="
    margin-left: {marginLeft}em; 
    margin-top: {marginTop}px; 
    color:{textColor}; 
    text-align: {align}; 
    {bold ? 'font-weight: bold;' : ''} 
    {italic ? 'font-style: italic;' : ''} 
    {size !== ''
    ? 'font-size: ' + size.toString() + 'em;'
    : pxsize !== ''
    ? 'font-size: ' + size.toString() + 'px;'
    : ''} 
    font-weight: {fontWeight};"
  class={boxed ? 'boxed' : ''}
>
  {text}
</p>

<style>
  .boxed {
    padding: 10px;
    border: 2px solid black;
  }
</style>
