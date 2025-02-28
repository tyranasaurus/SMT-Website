<script>
  import { tweened } from 'svelte/motion'
  import { cubicOut } from 'svelte/easing'
  import { slide } from 'svelte/transition'
  import PanelBox from '$lib/components/PanelBox.svelte'

  export let mainText // The text you always see and click on
  export let id = ''

  export let showContent = false
  let imageSrc = 'right-arrow.png'
  let start = showContent ? 0 : -90
  const rotateImage = tweened(start, {
    duration: 400,
    easing: cubicOut,
  })
  function toggleContent() {
    if (!showContent) {
      showContent = true
      rotateImage.set(0)
    } else {
      showContent = false
      rotateImage.set(-90)
    }
  }
</script>

<div class="dropdown" on:click={toggleContent} {id}>
  <PanelBox
    width="88%"
    margin="0.3em 5vw"
    padding="10px 10px 10px 20px"
    borderRadius="15px"
  >
    <svg
      class="dropdown-image"
      version="1.1"
      id="Capa_1"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      x="0px"
      y="0px"
      width="199.404px"
      height="199.404px"
      viewBox="0 0 199.404 300.404"
      style="enable-background:new 0 0 199.404 199.404;"
      xml:space="preserve"
    >
      <g>
        <polygon
          points="199.404,63.993 171.12,35.709 99.702,107.127 28.284,35.709 0,63.993 99.702,163.695"
          transform="rotate({$rotateImage} 99.702 99.702)"
        />
      </g>
    </svg>
    {mainText}
  </PanelBox>
</div>

{#if showContent}
  <div
    style="display: block;"
    class="hidden-content"
    transition:slide|local={{ duration: 500 }}
  >
    <PanelBox width="88%" margin="0 5vw" borderRadius="25px">
      <slot />
    </PanelBox>
  </div>
{/if}

<style>
  .dropdown {
    font-size: 2em;
    cursor: grab;
  }
  .hidden-content {
    font-size: 1em;
  }
  .dropdown-image {
    width: 0.5em;
    height: 0.5em;
  }
</style>
