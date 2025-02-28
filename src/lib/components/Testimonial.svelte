<!-- Component for that shadow box with glow on hover thing -->
<script>
  export let width = 'unset'
  export let height = 'unset'
  export let margin = '10px'
  export let padding = '10px'
  export let borderRadius = '5px'
  export let style = ''
  export let boxSizing = 'border-box'

  export let testimonial = ''
  export let title = ''
</script>

<figure class="snip1157">
  <blockquote>
    {testimonial}
    <h5>{title}</h5>
    <div class="arrow" />
  </blockquote>
</figure>

<style>
  figure.snip1157 {
    position: relative;
    overflow: hidden;
    margin: 10px;
    width: 100%;
    padding-bottom: 25px;
    color: #333;
    text-align: left;
    box-shadow: none !important;
  }
  figure.snip1157 blockquote {
    display: block;
    border-radius: 8px;
    position: relative;
    background-color: #fafafa;
    padding: 25px 50px 30px 50px;
    font-size: 0.8em;
    font-weight: 500;
    margin: 0;
    line-height: 1.6em;
    font-style: italic;
  }
  figure.snip1157 blockquote:before,
  figure.snip1157 blockquote:after {
    content: '\201C';
    position: absolute;
    font-size: 50px;
    opacity: 0.3;
    font-style: normal;
  }
  figure.snip1157 blockquote:before {
    top: 25px;
    left: 20px;
  }
  figure.snip1157 blockquote:after {
    content: '\201D';
    right: 20px;
    bottom: 0;
  }
  figure.snip1157 .arrow {
    top: 100%;
    width: 0;
    height: 0;
    border-left: 0 solid transparent;
    border-right: 25px solid transparent;
    border-top: 25px solid #fafafa;
    margin: 0;
    position: absolute;
  }
  figure.snip1157 h5 {
    opacity: 0.8;
    margin: 0;
    font-weight: 400;
  }
</style>
