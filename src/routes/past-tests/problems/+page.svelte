<script>
  import Heading from '$lib/components/Heading.svelte'
  import Link from '$lib/components/Link.svelte'
  import PageHeader from '$lib/components/PageHeader.svelte'
  import PanelBox from '$lib/components/PanelBox.svelte'

  const supportedYears = [
    2011, 2012, 2013, 2014, 2018, 2019, 2020, 2021, 2022, 2023, 2024,
  ]

  let yearLinks = []
  for (let i of supportedYears) {
    yearLinks.push({
      year: i,
      url: `/past-tests/${i}`,
    })
  }
</script>

<br /><br />
<div style="min-height: 100vh">
  <Heading text="Past Tournaments" size={4} textColor="var(--heading-color)" />
  <div class="flex" style="max-width: 100vw;">
    <PanelBox>
      <div
        class="flex"
        style="flex-direction: row; flex-basis: 0; flex-wrap: wrap;"
      >
        {#each yearLinks as link}
          <div class="year-link">
            <a href={link.url}>{link.year}</a>
          </div>
        {/each}
      </div>
    </PanelBox>
  </div>
</div>

<style>
  .year-link {
    margin-left: 10px;
    margin-right: 10px;
    font-size: 20px;
    font-weight: bold;
    flex-wrap: wrap;
  }
</style>
