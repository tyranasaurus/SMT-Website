<script>
  export let year
  export let tests // Should be a list in the form of [["Test 1", "path/to/test1.pdf"], ["Test 2", "path/to/test2.pdf"]], etc.
  export let answers
  export let results
  export let id = ''

  import { tweened } from 'svelte/motion'
  import { cubicOut } from 'svelte/easing'
  import Dropdown from '$lib/components/Dropdown.svelte'

  let showContent = 'none'
  const rotateImage = tweened(-90, {
    duration: 400,
    easing: cubicOut,
  })
  function toggleContent() {
    if (showContent === 'none') {
      showContent = 'block'
      rotateImage.set(0)
    } else {
      showContent = 'none'
      rotateImage.set(-90)
    }
  }
</script>

<Dropdown mainText={year} {id}>
  <table>
    {#each tests as test}
      <tr>
        {#each test as item}
          {#if item.length == 1}
            <td><strong>{item[0]}</strong></td>
          {:else}
            <td
              ><a target="_blank" sveltekit:prefetch href={item[1]}>{item[0]}</a
              ></td
            >
          {/if}
        {/each}
      </tr>
    {/each}
  </table>
</Dropdown>

<style>
  table {
    border-spacing: 1em;
  }
</style>
