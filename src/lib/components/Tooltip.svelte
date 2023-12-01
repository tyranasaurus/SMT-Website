<script>
    export let title = "";
    let isHovered = false;
    let x;
    let y;
  
    function mouseOver(event) {
      isHovered = true;
      x = event.pageX + 5;
      y = event.pageY + 5;
    }
    function mouseMove(event) {
      x = event.pageX + 5;
      y = event.pageY + 5;
      //console.log(x);
      //console.log(y);
    }
    function mouseLeave() {
      isHovered = false;
    }
  </script>
  
  <div
    on:mouseover={mouseOver}
    on:mouseleave={mouseLeave}
    on:mousemove={mouseMove}
    on:focus={mouseOver}
  >
    <slot />
  </div>
  
  {#if isHovered}
    <div style="top: {30}px; left: 0px;" class="tooltip">
      {title}
    </div>
  {/if}
  
  <style>
    .tooltip {
      border: 1px solid #ddd;
      box-shadow: 1px 1px 1px #ddd;
      background: white;
      border-radius: 4px;
      padding: 4px;
      position: absolute;
      z-index: 2;
    }
  
    
  </style>
  