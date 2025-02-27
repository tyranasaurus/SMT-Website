<script>
  import PanelBox from '$lib/components/PanelBox.svelte'

  export let competition
  export let imgSource
  export let description
</script>

<PanelBox width="15em" height="20em" borderRadius="15px">
  <a href="#{competition.toLowerCase()}">
    <div class="competition-img">
      <img alt={competition} src={imgSource} />
    </div>
    <p class="title-p">{competition}</p>
    <p class="desc-p">{description}</p>
  </a>
</PanelBox>

<style>
  a {
    text-decoration: none;
    background-color: green;
  }
  .competition-img {
    margin: 10%;
  }
  .title-p {
    font-size: 1.5rem;
    text-align: center;
  }
  .desc-p {
    font-size: 1rem;
    text-align: center;
  }
  img {
    max-width: 5em;
    margin: auto;
    display: block;
    width: 50%;
  }
</style>
