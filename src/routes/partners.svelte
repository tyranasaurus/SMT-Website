<script>
  import PageHeader from "$lib/components/PageHeader.svelte";
  import Section from "$lib/components/Section.svelte";
  import Heading from "$lib/components/Heading.svelte";
  import FlexBox from "$lib/components/FlexBox.svelte";
  import Image from "$lib/components/Image.svelte";
  import PanelBox from "$lib/components/PanelBox.svelte";
  import Link from "$lib/components/Link.svelte";
  import sponsorTiers from "$lib/sponsorTiers";
</script>

<svelte:head>
  <title>Partners</title>
</svelte:head>

<Section>
  <br /> <br />
  <Heading text="Partners" size={4} textColor="var(--heading-color)"/>
  <div style="margin-left: 10vw; margin-right: 10vw;">
    <PanelBox style="min-width: 360px;">
      <p style="font-size: 1.2em; margin: 5px">
        The SMT website is a clone of <a href = "https://mustangmath.com">Mustang Math</a>. Mustang Math is a 501(c)(3) nonprofit organization of committed high school & college volunteers who aim to foster collaborative problem solving skills among middle school students around the world. We highly recommend you check out <a href = "https://mustangmath.com/">their website</a>.
      </p>
      <p style="font-size: 1.2em; margin: 5px">
        SMT has a long-standing collaboration with our friends at the <a href = "https://bmt.berkeley.edu">Berkeley Math Tournament</a>. BMT is a college-run tournament that runs a wonderful high school and middle school tournament yearly.
      </p>
    </PanelBox>
  </div>
</Section>

{#each sponsorTiers as lvl}
  <Section>
    <br /> <br />
    <Heading text={lvl.name} size={3} textColor={lvl.headerColor} />
    <FlexBox wrap={true} align="stretch">
      {#if lvl.sponsors.length > 0}
        {#each lvl.sponsors as sponsor}
          <PanelBox
            borderRadius="20px"
            width="40%"
            style="max-width: 300px; min-height: 250px; min-width: 250px;"
          >
            <a
              target="_blank"
              href={sponsor.link}
              style="height: 100%; display: flex; align-items: center;"
            >
              <img
                src={sponsor.url}
                alt={sponsor.alt}
                style="max-width: 100%;"
                
              />
              
            </a>
            
          </PanelBox>
          
        {/each}
      {:else}
        <p>Become our first {lvl.singular}!</p>
      {/if}
    </FlexBox>
  </Section>
{/each}
