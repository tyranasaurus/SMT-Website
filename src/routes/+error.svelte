<script context="module">
  /** @type {import('@sveltejs/kit').Load} */
  export function load({ error, status }) {
    console.log(error, status)
    return {
      props: { error, status },
    }
  }
  import { page } from '$app/stores'
</script>

<script>
  /** @type {number} */
  export let status

  /** @type {Error & {frame?: string} & {loc?: object}} */
  export let error

  import PageHeader from '$lib/components/PageHeader.svelte'
</script>

<html lang="">
  <PageHeader
    title="Error: {$page.status}"
    description={$page.error.message}
    button_url="/"
    button_text="Come back to charted territory!"
    button_id="homeButton"
  />
</html>

<!-- TODO figure out what to do with frames/stacktraces in prod -->
<!-- frame is populated by Svelte in its CompileError and is a Rollup/Vite convention -->
<!--
{#if error.frame}
	<pre>{error.frame}</pre>
{/if}
{#if error.stack}
	<pre>{error.stack}</pre>
{/if} 
-->

<style>
</style>
