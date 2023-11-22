<script>
    import Heading from "$lib/components/Heading.svelte";
    import Link from "$lib/components/Link.svelte";
    import PageHeader from "$lib/components/PageHeader.svelte";
    import FlexBox from "$lib/components/FlexBox.svelte";
    import Table from "$lib/components/Table.svelte";
    import PanelBox from "$lib/components/PanelBox.svelte";
    import Timeline from "$lib/components/timeline/Timeline.svelte";
    import TimelineElement from "$lib/components/timeline/TimelineElement.svelte";
    import HeaderButton from "$lib/components/HeaderButton.svelte";
    import QA from "$lib/components/FAQitem.svelte";
    import Questions from "$lib/FAQ-smt-2024.json";

    let windowWidth;
    const scheduleData = [
        {
            Time: "8:00 AM-8:30 AM",
            Event: "Event Checkin",
        },
        ["8:30 AM-9:00 AM", "Opening Ceremony"],
        ["9:10 AM-10:40 AM", "Power Round (80 min)"],
        ["10:40 AM-11:40 AM", "Team Round (50 min)"],
        ["11:40 AM-12:30 PM", "Lunch Break (50 min)"],
        [
            "12:30 PM-2:30 PM",
            "Individual Round(s)",
        ],
        ["2:30 PM-4:00 PM", "Guts Round (80 min)"],
        ["5:30 PM-6:00 PM", "Award Ceremony"],
    ];

    const formLink =
        "https://forms.gle/YUYraZ9A5aWPXNfz6";
</script>

<svelte:head>
    <title>SMT 2024</title>
</svelte:head>

<svelte:window bind:innerWidth={windowWidth} />

<br><br>
<Heading text="Stanford Math Tournament 2024" size={4} textColor="var(--heading-color)"/>
<Heading text="Overview" size={2.5} />
<div class="section-wrapper">
    <PanelBox>
        <div style="padding: 10px;">
            <p>
                <strong>DATE:</strong> April 13, 2024 <br />
                <strong>LOCATION:</strong> Stanford University <br />
                <strong>WHO:</strong> High School students residing within the United States <br />
                <strong>TEAM SIZE:</strong> 5-6 <br />
                <strong>COST:</strong> $20 per student (Financial aid available upon request!) <br /> <br />
                <i
                    ><strong>Note for International Students:</strong>
                    Please visit <Link
                        url="/competitions/smt-2024-online"
                        text="this page."
                    />
                </i>
            </p>
            <HeaderButton
                text="Apply for SMT 2024"
                href={formLink}
                newTab=true
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
            <p>For SMT 2024, we will be inviting <b>400 students</b> (~65-80 teams) from around the United States to compete in-person on Stanford’s campus. We are <b>now accepting applications</b> for in-person participation from schools and local organizations in the United States. We will not be accepting applications from individuals or teams with less than 5 participants. Teams that are unable to participate in our in-person tournament are invited to participate in our online tournaments.</p>
            <p>Students are highly encouraged to participate in SMT 2024 as part of their <b>school</b>. Students who do not have the opportunity to participate in SMT as part of their school may participate as part of a <b>local organization</b>. An organization is considered local if its students are within a roughly 50 mile radius of the organization’s headquarters. <i>Students may not participate as part of a mathematical organization if their school is sending a team to SMT 2024 in-person.</i></p>
            <p>A certain number of spots will be reserved for students from within the Bay Area (defined as within 150 miles of Stanford University) with the rest reserved for students from outside the Bay. For each of these categories, we will reserve spots for <b>top school teams</b> (non-orgs) from SMT 2023 and for teams that are <b>low-income</b> and/or <b>historically underrepresented</b> in mathematics. The rest of the spots will be assigned via a lottery, with preference given to school-based teams.</p>
            <p>These criteria only apply for SMT 2024 at Stanford, not for SMT 2024 Online. These selection criteria are not final and may change as we look for a set of criteria that make sense to promote both diversity and competition for this year and future ones. Decisions made by SMT are final and non-negotiable.</p>
            <p style="font-size: 0.8em;"><i>Updated on 11/22/2023</i></p>
        </div>
    </PanelBox>
</div>

<Heading text="Registration Timeline" size={2.5} />

<Timeline width="60%">
    <TimelineElement>
        <strong>November 19, 2023:</strong> In-person application form opens
        <a href={formLink} target="_blank">here</a>
        <!-- <br /> -->
        <!-- <Link
             url="https://docs.google.com/forms/d/e/1FAIpQLScyywaWqPFLnGATcamhA_XGwfREfsu6qMkB5fx2LLUk9GRKOA/viewform?usp=share_link"
             text="Link to registration form"
             /> -->
    </TimelineElement>
    <TimelineElement>
        <strong>March 1, 2024 at 11:59 PM PT:</strong> Application deadline
    </TimelineElement>
    <TimelineElement>
        <strong>March 6, 2024:</strong> Announcement of teams selected for
        in-person competition
    </TimelineElement>
    <TimelineElement>
        <strong>March 14, 2024:</strong> Deadline for selected teams to register
    </TimelineElement>
    <!--<TimelineElement>
        <strong>March 29, 2024:</strong> Deadline for proof of travel and housing.
    </TimelineElement>
    <TimelineElement>
        <strong>April 1, 2024:</strong> Deadline for student waiver submission.
    </TimelineElement>
-->
    <TimelineElement>
        <strong>April 13, 2024:</strong> SMT tournament day
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
                *Schedule subject to change. Note that there is built-in buffer
                time to explain instructions and assist with technical
                difficulties.*
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
            The <strong>Team Round</strong> is a 50-minute exam consisting of 15
            short answer questions.
        </p>
        <p>
            The <strong>Guts Round</strong> is an 80 minute team exam consisting
            of 9 series of 3 questions each, whereby teams must submit answers to
            a previous round in order to gain access to the next. Subsequent rounds
            are both harder and worth more points than previous rounds.
        </p>
        <p>
            For the individual portion, students may choose to take two subject
            tests in a specific topic or take a single, longer General Test.
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
            The <strong>Individual Round(s)</strong> are the rounds taken independent of your teams.
        </p>
    </PanelBox>
</div>
<!--
<Heading text="COVID-19 Policy" size={2.5} />
<div class="section-wrapper">
    <PanelBox>
        <div style="padding: 10px;">
            <p>Proof of Vaccination and Proof of Negative COVID test within 24 hours of the start of the program are required. Students looking to request exemption from this protocol would have to email <a href="mailto:protectminors@stanford.edu">protectminors@stanford.edu</a>.</p>
        </div>
    </PanelBox>
</div>
-->
<Heading text="FAQ" size={2.5} />
<section>
    <FlexBox wrap={true}>
        {#each Questions as QAitem}
            <QA
                question={QAitem.question}
                answer={QAitem.answer}
            />
        {/each}
    </FlexBox>
</section>
