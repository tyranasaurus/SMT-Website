<script>
  import Heading from "$lib/components/Heading.svelte";
  import Dropdown from "$lib/components/Dropdown.svelte";
  import Link from "$lib/components/Link.svelte";
  import Button from "$lib/components/Button.svelte";
  import PageHeader from "$lib/components/PageHeader.svelte";
  import Testimonial from "$lib/components/Testimonial.svelte";
  import Competition from "$lib/components/Competition.svelte";
  import Tournament from "$lib/components/Tournament.svelte";
  import FlexBox from "$lib/components/FlexBox.svelte";
  import Table from "$lib/components/Table.svelte";
  import PanelBox from "$lib/components/PanelBox.svelte";
  import Image from "$lib/components/Image.svelte";
  let windowWidth;
</script>

<svelte:head>
  <title>MMT 2023</title>
</svelte:head>

<svelte:window bind:innerWidth={windowWidth} />

<PageHeader
  title="Mustang Math Tournament (MMT)"
  description="April 29, 2023: 9:00 AM - 4:30 PM PT"
  button_url="#competition"
  button_text="Register for Competition!"
  button_id="registerForCompetition"
  target=""
/>

<br /><br />

<Heading text="What is MMT?" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw;">
  <PanelBox>
    <p style="font-size: 1.5em; text-align: center;">
      The Mustang Math Tournament is a middle school math competition run for
      middle school students around the nation. It is put together by Mustang
      Math, a 501(c)(3) nonprofit organization put together by high school and
      college students, including the directors of the Stanford and Berkeley
      Math Tournaments!<br /><br />
      The tournament is
      <strong>centered around teamwork and collaboration</strong>, incentivizing
      students to work with their teams not only to navigate the
      <strong>challenging but interesting problems</strong>
      of the tournament, but also to develop strategies to master the unique and
      fun game-like rounds. With interesting and fun rounds including a logic-based
      puzzle round, a strategy-filled bingo round, a race-like gallop round, and
      our trademark 'Mystery Mare' round, our tournament is guaranteed to be
      <strong
        >enjoyable for any and all students who have an interest in mathematics</strong
      >.<br /><br />
      Don't believe us? Check out some comments from past participants below!
    </p>
  </PanelBox>
</div>

<br id="competition" />
<Heading text="Competitions" size={2.5} />
<div class="competition-wrapper">
  <FlexBox align="start">
    <Tournament
      imgSource="/competitions/mmt-2023/washington.png"
      title="MMT Washington"
      location="Seattle, WA"
      description="Held in the Eastside Seattle Area and where MM was founded, this event will be WAnderful"
      button_text="MMT WA"
      button_url="/competitions/mmt-2023/mmt-2023-WA"
    />
    <Tournament
      imgSource="/competitions/mmt-2023/california.png"
      title="MMT California"
      location="San Francisco, CA"
      description="Held in either the East or South Bay, the competition at this event will be CAptivating"
      button_text="MMT CA"
      button_url="/competitions/mmt-2023/mmt-2023-CA"
    />
    <Tournament
      imgSource="/competitions/mmt-2023/online.png"
      title="MMT Online"
      location="Online (Discord)"
      description="For whomever the in-person competitions are too far, compete with students around the nation in our online synchronous event"
      button_text="MMT Online"
      button_url="/competitions/mmt-2023/mmt-2023-online"
    />
  </FlexBox>
</div>
<br />

<Heading text="Testimonials" size={2.5} />
<div class="grid-three" style="margin-left: 10vw; margin-right: 10vw;">
  <div>
    <Testimonial
      testimonial="MMT has a unique take on standard math competitions"
      title="2022 Participant"
    />
    <Testimonial
      testimonial="MMT focused less on calculations than other math competitions"
      title="2022 Participant"
    />
    <Testimonial
      testimonial="I think this was a very nice way to spend my day."
      title="2021 Participant"
    />
  </div>

  <div>
    <Testimonial
      testimonial="MMT's style of problems are much better than other tournaments. Unlike other tournaments that has the same style over the years, MMT has new and exciting styles of problems that makes it more fun to try and solve it on the spot"
      title="2022 Participant"
    />
    <Testimonial
      testimonial="MMT had people captivated even before the tournament started with their Discord server and problems of the day"
      title="2022 Participant"
    />
  </div>

  <div>
    <Testimonial
      testimonial="I really appreciate all that MMT has done and I look forward to the competition that is held next year! I must say that the MMT was an impressive execution of math competitions unlike anything I've seen before!"
      title="2022 Participant"
    />
    <Testimonial
      testimonial="My favorite memory from MMT was the teamwork - both chaotically and organizedly working with each other to solve the problems"
      title="2022 Participant"
    />
  </div>
</div>
<br />

<br /><br />

<style>
  li {
    list-style-type: disc;
    margin-left: 20px;
  }
</style>
