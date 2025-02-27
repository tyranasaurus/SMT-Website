<script>
  import Heading from '$lib/components/Heading.svelte'
  import Dropdown from '$lib/components/Dropdown.svelte'
  import Link from '$lib/components/Link.svelte'
  import Button from '$lib/components/Button.svelte'
  import PageHeader from '$lib/components/PageHeader.svelte'
  import Competition from '$lib/components/Competition.svelte'
  import FlexBox from '$lib/components/FlexBox.svelte'
  import Table from '$lib/components/Table.svelte'
  import PanelBox from '$lib/components/PanelBox.svelte'
  import Image from '$lib/components/Image.svelte'
  let windowWidth
</script>

<svelte:head>
  <title>MMT 2022</title>
</svelte:head>

<svelte:window bind:innerWidth={windowWidth} />

<PageHeader
  title="Join the Mustang Math Team"
  description="Become a part of the herd!"
  button_url="https://tinyurl.com/JoinMMT2023"
  button_text="Join our Team!"
  id="joinTheMustangMathTeam"
/>
<br /> <br />

<Heading text="What is MMT?" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw;">
  <PanelBox>
    <p style="font-size: 1.5em; text-align: center;">
      Mustang Math is a <b style="color: #1B9AAA;">nonprofit organization</b>
      of high school and college volunteers that are dedicated towards providing
      middle schoolers access to challenging, interesting, fun, and collaborative
      math competitions and resources! We are the organizers of the annual
      <b style="color: #1B9AAA;">Mustang Math Tournament</b>
      and we are also working on many new and exciting projects including a community
      Discord server, a YouTube channel, a training platform, and more! Having reached
      <b style="color: #1B9AAA;">over 700 U.S. competitors</b> in our first three
      years, plus an expected 500 more in our international tournament, we are excited
      to expand our team to offer our events to even more mathematically inclined
      students.
    </p>
  </PanelBox>
</div>
<br />

<Heading text="Why should you join Mustang Math?" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw;">
  <PanelBox>
    <p style="font-size: 1.5em; text-align: center;">
      You should join Mustang Math if you are in high school or college and are
      passionate about promoting an interest in competition math to younger
      students!
    </p>
    <p style="font-size: 1.5em; text-align: center;">
      A lot of our members currently cite that they joined Mustang Math because
      they want to share the love they have of <b style="color: #1B9AAA;"
        >competition math</b
      >
      and the <b style="color: #1B9AAA;">community</b> that it provides to other
      students. Additionally, as a non-profit organization on the rise, there
      are numerous opportunities for volunteers to
      <b style="color: #1B9AAA;">share ideas</b>
      and <b style="color: #1B9AAA;">suggest projects</b> that they are
      interested in. Overall, working in the Mustang Math team is both a fun and
      fulfilling experience where volunteers are able to pursue their passion
      all while learning
      <b style="color: #1B9AAA;">real-life skills</b> such as teamwork and time management.
    </p>
  </PanelBox>
</div>
<br />

<Heading text="Our Subteams" size={2.5} />
<Dropdown mainText="Problem Writing" id="showDropdown">
  <p>
    The <b style="color: #1B9AAA;">Problem Writing</b> team is primarily
    responsible for the <b style="color: #1B9AAA;">creation of problems</b>
    used by Mustang Math, and the
    <b style="color: #1B9AAA;">formation of tests</b> used for our annual tournament(s).
    Besides the tournament, you could write problems for our online practice platform
    and other Mustang Math projects! We welcome problem writers with a variety of
    experience.
  </p>
</Dropdown>
<Dropdown mainText="Tech" id="showDropdown">
  <p>
    The <b style="color: #1B9AAA;">Tech</b> team is in charge of ensuring that
    all the various
    <b style="color: #1B9AAA;">technological-related needs</b>
    of Mustang Math as an organization are being met and maintained, as well as
    <b style="color: #1B9AAA;">implementing new projects</b> wherever necessary.
    Currently, the Tech team is working on tasks such as building a Mustang Math
    YouTube, creating an online training platform, and other exciting projects!
  </p>
</Dropdown>
<Dropdown mainText="Design" id="showDropdown">
  <p>
    The <b style="color: #1B9AAA;">Design</b> team ensures that Mustang Math
    maintains a <b style="color: #1B9AAA;">consistent image</b> and
    <b style="color: #1B9AAA;">aesthetic</b> throughout the year. Specific jobs that
    may arise include: Maintaining and rebranding the tournament as necessary, working
    with other teams to ensure that materials are on brand, and taking on other projects
    as necessary.
  </p>
</Dropdown>
<Dropdown mainText="Tournament Development" id="showDropdown">
  <p>
    The <b style="color: #1B9AAA;">Tournament Development</b> team is
    responsible for <b style="color: #1B9AAA;">organization-level</b>
    communication and all communications relating to the tournament. In general,
    this will consist of <b style="color: #1B9AAA;">marketing</b> and
    <b style="color: #1B9AAA;">advertising</b>, working with
    <b style="color: #1B9AAA;">sponsors</b>,
    <b style="color: #1B9AAA;">communicating</b> with registrants of Mustang Math
    Tournament, and making sure that all partners are kept up-to-date with necessary
    information. Additionally, the Tournament Development team plans and manages
    all day-of operations for Mustang Math Tournament’s in-person competition(s).
  </p>
</Dropdown>
<Dropdown mainText="Curriculum Development" id="showDropdown">
  <p>
    The <b style="color: #1B9AAA;">Curriculum Development</b> team is in charge
    of <b style="color: #1B9AAA;">developing content</b> for all Mustang Math
    classes as well as for YouTube videos if needed. This may consist of
    planning lecture material, finding example problems, and
    <b style="color: #1B9AAA;">teaching students</b>. This is a new team this
    year, meaning that there is a large potential for innovation, adaptation,
    and new ideas.
  </p>
</Dropdown>
<Dropdown mainText="Community Engagement" id="showDropdown">
  <p>
    The <b style="color: #1B9AAA;">Community Engagement</b> team is in charge of
    building and engaging the Mustang Math student community. Some of the jobs
    include managing <b style="color: #1B9AAA;">social media</b>
    and
    <b style="color: #1B9AAA;">online presence</b>, such as FaceBook, LinkedIn,
    Instagram, and AoPS. Other responsibilities can include
    <b style="color: #1B9AAA;">planning events</b>, activities, maintaining the
    discord server, and managing the youtube channel.
  </p>
</Dropdown>
<br />
