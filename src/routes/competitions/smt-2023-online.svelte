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

    let windowWidth;
    const scheduleData = [
        {
            Time: "8:30 AM-9:00 AM",
            Event: "Event Checkin",
        },
        ["9:00 AM-9:30 AM", "Opening Ceremony"],
        ["9:30 AM-11:00 AM", "Power Round (80 min)"],
        ["11:00 AM-12:00 PM", "Team Round (50 min)"],
        ["12:00 PM-1:00 PM", "Lunch Break (60 min)"],
        [
            "1:00 PM-3:00 PM",
            "Individual Round(s)",
        ],
        ["3:00 PM-4:30 PM", "Guts Round (80 min)"],
    ];

    const formLink =
        "https://docs.google.com/forms/d/e/1FAIpQLScyywaWqPFLnGATcamhA_XGwfREfsu6qMkB5fx2LLUk9GRKOA/viewform?usp=share_link";
</script>

<svelte:head>
    <title>SMT 2023</title>
</svelte:head>

<svelte:window bind:innerWidth={windowWidth} />

<br><br>
<Heading text="Stanford Math Tournament 2023 Online" size={4} textColor="var(--heading-color)"/>
<Heading text="Overview" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw;">
    <PanelBox>
        <div style="padding: 10px;">
            <p>
                <strong>DATE:</strong> April 9, 2023 <br />
                <strong>LOCATION:</strong> Online, PST Timezone<br />
                <strong>WHO:</strong> High School and Middle School students<br />
                <strong>TEAM SIZE:</strong> 6-8 (smaller teams may be combined with others to make full teams) <br />
                <strong>COST:</strong> $10 early bird registration per student, $15 regular registration, $25 last-minute registration (Financial Aid available on request!) <br /> <br />
            </p>
        </div>
    </PanelBox>
</div>
<br />

<Heading text="Registration Information" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw;">
    <PanelBox>
        <div style="padding: 10px;">
            <p>In order to properly register for SMT Online, all of the following steps must be completed by the coach and students:</p>
            <ol>
                <li>Coaches must make payment for participating students on <a href = "https://tinyurl.com/SMT2023OnlineEventbrite">Eventbrite</a>. Seats purchased on Eventbrite will be reflected in ContestDojo within two business days.</li>
                <li>Coaches must create a coaches account  <a href = "https://contestdojo.com">ContestDojo</a> and register thir organization for SMT 2023 Online.</li>
                <li>Coaches must invite students on ContestDojo by email or organization join code.</li>
                <li>Students must join the organization and fill out the registration form.</li>
                <li>Coaches organize their students into teams.</li>
            </ol>
            <HeaderButton class = "RegButtons"
                text="Eventbrite Payment"
                href={"https://tinyurl.com/SMT2023OnlineEventbrite"}
                isSmall
            />
            <br>
            <HeaderButton class = "RegButtons"
                text="ContestDojo"
                href={"https://contestdojo.com"}
                isSmall
            />
        </div>
    </PanelBox>
</div>

<Heading text="Registration Timeline" size={2.5} />

<Timeline width="60%">
    <TimelineElement>
        <strong>Feburary 27, 2023:</strong> SMT Online Registration opens
    </TimelineElement>
    <TimelineElement>
        <strong>March 15, 2023 at 11:59 PM PT:</strong> Early Bird ($10/student) registration deadline
    </TimelineElement>
    <TimelineElement>
        <strong>March 29, 2023:</strong> Regular ($15/student) registration deadline
    </TimelineElement>
    <TimelineElement>
        <strong>April 1, 2023:</strong> Deadline for student waiver submission.
    </TimelineElement>
    <TimelineElement>
        <strong>April 6, 2023:</strong> Late ($25/student) registration deadline
    </TimelineElement>
    <TimelineElement>
        <strong>April 9, 2023:</strong> SMT Online!!!
    </TimelineElement>
    <TimelineElement>
        <strong>April 16, 2023:</strong> SMT Online Award Ceremony
    </TimelineElement>
</Timeline>

<Heading text="Contest Schedule" size={2.5} />
<div class="schedule-wrapper">
    <FlexBox>
        <PanelBox>
            <Table
                data={scheduleData}
                width="auto"
                cellPadding={5}
                cellPaddingRight={20}
                tableStyle="margin-left: auto; margin-right: auto"
                overallHeader="Tournament Schedule (8:30 AM-4:30 PM PT)"
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

<div style="margin-left: 10vw; margin-right: 10vw;">
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

<Heading text="FAQ" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw;">
    <PanelBox>
        Make sure to check the rules page for detailed information regarding
        SMT. If your question is not answered below, feel free to contact the
        SMT coordinators at <a href="mailto:stanford.math.tournament@gmail.com"
            >stanford.math.tournament@gmail.com</a
        >. <br />
        <br />
        <strong>Registration</strong><br />
        Q: How many students may be on a team?<br />
        A: Teams consist of 6-8 members. Individuals and incomplete teams may be combined by organizers to form complete teams.<br />
        <br />
        Q: Do students on the same team have to be from the same school or established mathematical organization?<br />
        A: Yes, students must be from the same school or mathematical organization<br />
        <br />
        
        Q: What schools or organizations can participate in SMT Online?<br />
        A: SMT 2023 Online will be open to all students.<br />
        <br />
        Q: Can international teams participate in SMT? If so, how do they register?<br
        />
        A: Yes, as long as they are able to take the test in PST time.<br
        />
        <br />
        Q: PST time does not work for me. What do I do?
        A: You can participate in <Link url="/competitions/smt-2023-async" text="SMT Asyncronous!" />
        <br />
        <strong>Testing</strong><br />
        Q: Are calculators allowed?<br />
        A: No. Calculators are not allowed on any portion of the tests. Check the
        SMT rules for information on permitted items.<br />
        <br />
        Q: What topics may appear on the tests? How hard are the tests?<br />
        A: See the mathematical expectations document for guidelines on what topics
        may appear on each test. It is also advisable to look at the test from previous
        years in order to get a sense of the typical style and difficulty of SMT
        tests.<br />
        <br />
        <!--
        Q: Which individual test should I take?<br />
        A: If you have little or no experience with contest math, we strongly recommend
        you take the General Test. Looking at past tests will help you get a sense
        of the difficulty of each test.<br />
        <br />
        -->
        <strong>Logistics</strong><br />
        Q: Can I use the problems from previous SMT tests listed below in my classroom/book/etc?<br
        />
        A: Yes! Feel free to use these problems provided you cite us in the format (Stanford Math Tournament [Year] [Round] [Problem #])<br />
    </PanelBox>
</div>

<style>
    .RegButtons {
        display: inline-flex;
        padding: 5px;
        margin: 5px;
    }
</style>