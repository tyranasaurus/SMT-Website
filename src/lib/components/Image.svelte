<script>
  export let url
  export let alt
  export let link = ''
  export let height = ''
  export let width = ''
  export let target = '_self'
  export let className = ''
</script>

<!-- Warning: spaghetti code -->

{#if link === ''}
  {#if height === '' && width === ''}
    <img src={url} {alt} class={className} />
  {:else if height === ''}
    <img src={url} {alt} {width} class={className} />
  {:else if width === ''}
    <img src={url} {alt} {height} class={className} />
  {:else}
    <img src={url} {alt} {width} {height} class={className} />
  {/if}
{:else if height === '' && width === ''}
  <a href={link} {target} class={className}>
    <img src={url} {alt} class={className} />
  </a>
{:else if height === ''}
  <a href={link} {target} class={className}>
    <img src={url} {alt} {width} class={className} />
  </a>
{:else if width === ''}
  <a href={link} {target} class={className}>
    <img src={url} {alt} {height} class={className} />
  </a>
{:else}
  <a href={link} {target} class={className}>
    <img src={url} {alt} {width} {height} class={className} />
  </a>
{/if}

<style>
  img {
    max-width: 100%;
  }
</style>
