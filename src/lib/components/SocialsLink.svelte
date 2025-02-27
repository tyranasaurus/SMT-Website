<script>
  import Fa from 'svelte-fa'
  export let url
  export let icon
  export let text = false
</script>

<a
  href={url}
  target="_blank"
  rel="noopener noreferrer"
  class="social-link"
  class:text
>
  <Fa {icon} />
</a>

<style>
  .social-link {
    padding: 10px;
    color: white;
    opacity: 0.6;
  }

  @media screen and (max-width: 900px) {
    .social-link {
      padding: 4px;
    }
  }

  .social-link:hover {
    text-decoration: underline;
    opacity: 0.8;
  }

  .text {
    font-size: 1.2rem;
    font-weight: bold;
  }
</style>
