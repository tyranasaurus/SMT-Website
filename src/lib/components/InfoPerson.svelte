<script>
  export let pic
  export let name
  export let description
  export let width = '98%'
  export let left = false
  export let windowWidth

  import Text from '$lib/components/Text.svelte'
  import Heading from '$lib/components/Heading.svelte'
  import PanelBox from '$lib/components/PanelBox.svelte'
</script>

<PanelBox {width}>
  <div
    class="person-flex"
    style={windowWidth < 650
      ? 'display: grid;grid-template-columns: 100%;'
      : left
      ? 'display: grid;grid-template-columns: 35% 65%;'
      : 'display: grid;grid-template-columns: 65% 35%;'}
  >
    {#if left}
      <div class="person-pic flex">
        <div>
          <div class="flex">
            <img
              class="person-img"
              src={pic}
              alt={name}
              width="130"
              height="130"
              style="object-fit: cover; border-radius: 9999px;"
            />
          </div>
          <p
            style="color: black; font-size: 1.2em;font-weight:500;margin:0;padding:0;text-align: center;"
          >
            {name}
          </p>
        </div>
      </div>
    {/if}
    <div class="person-details">
      <div>
        {#if description}
          <p
            style="color: black; font-size: 1em;font-weight:300;margin:0;padding:0;text-align:left;"
          >
            {description}
          </p>
        {/if}
      </div>
    </div>
    {#if !left}
      <div class="person-pic flex">
        <div>
          <div class="flex">
            <img
              class="person-img"
              src={pic}
              alt={name}
              width="130"
              height="130"
              style="object-fit: cover; border-radius: 9999px;"
            />
          </div>
          <p
            style="color: black; font-size: 1.2em;font-weight:500;margin:0;padding:0;text-align: center;"
          >
            {name}
          </p>
        </div>
      </div>
    {/if}
  </div>
</PanelBox>

<style>
  .person-img {
    margin: 3px;
    max-height: 100%;
  }
  .person-pic {
    min-width: 0;
  }
  .person-details {
    display: flex;
    flex-basis: 0;
    flex-grow: 1;
    align-items: center;
    justify-content: center;
    padding-left: 5px;
    text-align: center;
  }
  .person-pic {
    min-width: 0;
  }
</style>
