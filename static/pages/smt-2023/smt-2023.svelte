<script>
  import Heading from '$lib/components/Heading.svelte'
  import Link from '$lib/components/Link.svelte'
  import PageHeader from '$lib/components/PageHeader.svelte'
  import FlexBox from '$lib/components/FlexBox.svelte'
  import Table from '$lib/components/Table.svelte'
  import PanelBox from '$lib/components/PanelBox.svelte'
  import Timeline from '$lib/components/timeline/Timeline.svelte'
  import TimelineElement from '$lib/components/timeline/TimelineElement.svelte'
  import HeaderButton from '$lib/components/HeaderButton.svelte'
  import QA from '$lib/components/FAQitem.svelte'
  import Questions from '$lib/FAQ-smt-2023.json'

  let windowWidth
  const scheduleData = [
    {
      Time: '8:00 AM-8:30 AM',
      Event: 'Event Checkin',
    },
    ['8:30 AM-9:00 AM', 'Opening Ceremony'],
    ['9:10 AM-10:40 AM', 'Power Round (80 min)'],
    ['10:40 AM-11:40 AM', 'Team Round (50 min)'],
    ['11:40 AM-12:30 PM', 'Lunch Break (50 min)'],
    ['12:30 PM-2:30 PM', 'Individual Round(s)'],
    ['2:30 PM-4:00 PM', 'Guts Round (80 min)'],
    ['5:30 PM-6:00 PM', 'Award Ceremony'],
  ]

  const formLink =
    'https://docs.google.com/forms/d/e/1FAIpQLScyywaWqPFLnGATcamhA_XGwfREfsu6qMkB5fx2LLUk9GRKOA/viewform?usp=share_link'
</script>

<svelte:head>
  <title>SMT 2023</title>
</svelte:head>

<svelte:window bind:innerWidth={windowWidth} />

<br /><br />
<Heading
  text="Stanford Math Tournament 2023"
  size={4}
  textColor="var(--heading-color)"
/>
<Heading text="Overview" size={2.5} />
<div class="section-wrapper">
  <PanelBox>
    <div style="padding: 10px;">
      <p>
        <strong>DATE:</strong> April 8, 2023 <br />
        <strong>LOCATION:</strong> Stanford University <br />
        <strong>WHO:</strong> High School students residing within the United
        States <br />
        <strong>TEAM SIZE:</strong> 5-6 <br />
        <strong>COST:</strong> $15 per student (Financial aid available upon
        request!) <br /> <br />
        <i
          ><strong>Note for International Students:</strong>
          Please visit <Link
            url="/competitions/smt-2023-online"
            text="this page."
          />
        </i>
      </p>
      <HeaderButton
        text="Apply for SMT 2023"
        href={formLink}
        isSmall
        centered
      />
    </div>
  </PanelBox>
</div>
<br />

<Heading text="Application Information" size={2.5} />
<div class="section-wrapper">
  <PanelBox>
    <div style="padding: 10px;">
      <p>
        For SMT 2023, Stanford University policy limits us to 42 teams of 5-6
        students from the United States in-person at Stanford’s campus. As such,
        we are now accepting applications for in-person participation from
        United States based schools and established mathematical organizations.
        We will not be accepting individual applications or applications for
        teams of size less than 5. All teams who don’t want to travel or are
        international should participate in our online tournaments.
      </p>
      <p>
        We will be accepting 25 teams from within the Bay Area (defined as
        within 150 mi of Stanford University), and 17 are from other domestic
        locations. Of these, 10 Bay Area teams and 7 Domestic teams will be
        merit-based - selected on performance in previous year’s and other
        relevant tournaments, and the rest will be selected based on a lottery
        system. Note, depdendent on interest, we may cap the number of teams
        participating from an individual organization to 2. The remaining teams
        will not be allowed to come in person and should participate in the
        online tournament happening on April 9, 2023.
      </p>
      <p>
        Do note that these selection criteria are not final and may change as we
        look for a set of criteria that make sense to promote both diversity and
        competition for this year and future ones. Decisions made by SMT
        Organizers are final and non-negotiable.
      </p>
    </div>
  </PanelBox>
</div>

<Heading text="Registration Timeline" size={2.5} />

<Timeline width="60%">
  <TimelineElement>
    <strong>February 13, 2023:</strong> In-person application form opens
    <a
      href="https://docs.google.com/forms/d/e/1FAIpQLScyywaWqPFLnGATcamhA_XGwfREfsu6qMkB5fx2LLUk9GRKOA/viewform?usp=share_link"
      target="_blank">here</a
    >
    <!-- <br /> -->
    <!-- <Link
             url="https://docs.google.com/forms/d/e/1FAIpQLScyywaWqPFLnGATcamhA_XGwfREfsu6qMkB5fx2LLUk9GRKOA/viewform?usp=share_link"
             text="Link to registration form"
             /> -->
  </TimelineElement>
  <TimelineElement>
    <strong>March 12, 2023 at 11:59 PM PT:</strong> Application deadline
  </TimelineElement>
  <TimelineElement>
    <strong>March 16, 2023:</strong> Announcement of teams selected for in-person
    competition
  </TimelineElement>
  <TimelineElement>
    <strong>March 22, 2023:</strong> Deadline for selected teams to register on Eventbrite
  </TimelineElement>
  <TimelineElement>
    <strong>March 29, 2023:</strong> Deadline for proof of travel and housing.
  </TimelineElement>
  <TimelineElement>
    <strong>April 1, 2023:</strong> Deadline for student waiver submission.
  </TimelineElement>
  <TimelineElement>
    <strong>April 8, 2023:</strong> SMT tournament day
  </TimelineElement>
</Timeline>

<Heading text="Contest Schedule" size={2.5} style="margin-top: 5rem" />
<div class="schedule-wrapper section-wrapper">
  <FlexBox>
    <PanelBox>
      <Table
        data={scheduleData}
        width="auto"
        cellPadding={5}
        cellPaddingRight={20}
        tableStyle="margin-left: auto; margin-right: auto"
        overallHeader="Tournament Schedule (8:00 AM-6:00 PM PT)"
      />
      <p style="margin-top: 2px; margin-bottom: 0px;">
        *Schedule subject to change. Note that there is built-in buffer time to
        explain instructions and assist with technical difficulties.*
      </p>
    </PanelBox>
  </FlexBox>
</div>
<br />

<Heading text="Test Information" size={2.5} />

<div class="section-wrapper">
  <PanelBox>
    <p>
      The <strong>Power Round</strong> is a 80-minute exam focused on proof-writing.
      The content of the test focuses on a single subject matter that is usually
      significantly different from traditional competitive math problems.
    </p>
    <p>
      The <strong>Team Round</strong> is a 50-minute exam consisting of 15 short
      answer questions.
    </p>
    <p>
      The <strong>Guts Round</strong> is an 80 minute team exam consisting of 9 series
      of 3 questions each, whereby teams must submit answers to a previous round
      in order to gain access to the next. Subsequent rounds are both harder and
      worth more points than previous rounds.
    </p>
    <p>
      For the individual portion, students may choose to take two subject tests
      in a specific topic or take a single, longer General Test.
    </p>
    <!--
        <p>
            The <strong>Subject Tests</strong> are 50-minute exams consisting of
            10 short answer questions. The subjects offered are
            <strong>
                Algebra, Combinatorics, Number Theory, and Geometry.
            </strong>
        </p>
        
        <p>
            The <strong>General Test</strong> is a 110-minute exam consisting of
            25 short answer questions that is designed for students that have less
            specialized mathematical background.
        </p>
        -->
    <p>
      The <strong>Individual Round(s)</strong> are the rounds taken independent of
      your teams.
    </p>
  </PanelBox>
</div>

<Heading text="COVID-19 Policy" size={2.5} />
<div class="section-wrapper">
  <PanelBox>
    <div style="padding: 10px;">
      <p>
        Proof of Vaccination and Proof of Negative COVID test within 24 hours of
        the start of the program are required. Students looking to request
        exemption from this protocol would have to email <a
          href="mailto:protectminors@stanford.edu">protectminors@stanford.edu</a
        >.
      </p>
    </div>
  </PanelBox>
</div>

<Heading text="FAQ" size={2.5} />
<section>
  <FlexBox wrap={true}>
    {#each Questions as QAitem}
      <QA question={QAitem.question} answer={QAitem.answer} />
    {/each}
  </FlexBox>
</section>
