<script>
  import PageHeader from '$lib/components/PageHeader.svelte'
  import Section from '$lib/components/Section.svelte'
  import Heading from '$lib/components/Heading.svelte'
  import FlexBox from '$lib/components/FlexBox.svelte'
  import Image from '$lib/components/Image.svelte'
  import PanelBox from '$lib/components/PanelBox.svelte'
  import Link from '$lib/components/Link.svelte'
  import sponsorTiers from '$lib/sponsorTiers'
</script>

<svelte:head>
  <title>Donate</title>
</svelte:head>

<PageHeader
  title="Donate"
  description="Help improve our tournaments, classes, and more!"
  button_url="
https://link.mustangmath.com/donate"
  button_text="Donate to Mustang Math!"
  button_id="donateMM"
/>

<Section>
  <br /> <br />
  <Heading text="Why Donate to Mustang Math?" size={4} />
  <FlexBox>
    <PanelBox width="60%" style="min-width: 360px;">
      <p style="font-size: 1.2em; margin: 5px">
        Mustang Math is a <b>501(c)(3) nonprofit</b> organization composed
        entirely of <b>high school and college volunteers</b>. We are incredibly
        passionate about providing middle school students with access to
        collaborative, challenging, and creative math tournaments, events, and
        classes. However, while our volunteers put countless hours of time into
        Mustang Math, in order to provide high quality events and enable our
        resources to be accessed by as many students as possible, we have a
        multitude of costs, including but not limited to venue booking,
        technology services, and teaching resources. Your donation will be
        attributed directly towards these costs allowing us to work towards our
        goal of
        <b>charging minimal to no registration fees</b> for our services.
      </p>
    </PanelBox>
  </FlexBox>
  <br />

  <Heading text="How to Donate" size={4} />
  <FlexBox>
    <PanelBox width="60%" style="min-width: 360px;">
      <p style="font-size: 1.2em; margin: 5px">
        All donations made to Mustang Math may be tax-deductible. Any donations
        upwards of $250 will be provided a receipt (contemporaneous written
        acknowledgement) for presentation to the IRS. You can either donate
        through <a href="link.mustangmath.com/donate">PayPal</a>, or by mailing
        a check made out to Mustang Math at
        <b>8139 231st PL NE, Redmond WA 98053</b>. If you have any questions,
        don't hesitate to
        <a href="mailto:contact@mustangmath.com">email us</a>.
      </p>
    </PanelBox>
  </FlexBox>
  <br />
  <br />
</Section>
