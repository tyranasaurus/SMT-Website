<script>
  import PanelBox from '$lib/components/PanelBox.svelte'
  import Link from '$lib/components/Link.svelte'
  import Button from '$lib/components/Button.svelte'

  export let title
  export let imgSource
  export let description
  export let button_url
  export let button_text
  export let location
</script>

<PanelBox width="30em" borderRadius="15px">
  {#if imgSource}
    <div class="competition-img">
      <img alt={title} src={imgSource} />
    </div>
  {/if}
  <p class="title-p"><strong>{title}</strong></p>
  {#if location}
    <p class="loc-p">{location}</p>
  {/if}
  {#if description}
    <p class="desc-p">{description}</p>
  {/if}
  {#if button_url}
    <div class="flex">
      <div class="compbuttons">
        <Link
          url={button_url}
          className="registrationButton2"
          text={button_text}
          textColor="white"
          visitedColor="white"
          id={button_text}
          button_id={button_text}
        />
      </div>
    </div>
  {/if}
  <br />
</PanelBox>

<style>
  .competition-img {
    margin: 10%;
  }
  .title-p {
    font-size: 1.5rem;
    text-align: center;
    padding: 0;
    margin: 0;
  }
  .desc-p {
    font-size: 1rem;
    text-align: center;
  }
  .loc-p {
    font-size: 1.25rem;
    text-align: center;
    padding: 0;
    margin: 0;
  }
  img {
    max-width: 5em;
    margin: auto;
    display: block;
    width: 30%;
  }
</style>
