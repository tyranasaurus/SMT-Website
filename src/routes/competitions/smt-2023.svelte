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
            Time: "8:00 AM-8:30 AM",
            Event: "Opening Ceremony",
        },
        ["9 AM-10:20 AM", "Power Round (80 min)"],
        ["10:30AM-11:30AM", "Team Round (50 min)"],
        ["11:30AM-1PM", "Lunch Break (1.5 hr)"],
        [
            "1:15PM-3:15PM",
            "Individual Round(s)<br>- 2 x 50 min (subject)<br>- 110 min (general)",
        ],
        ["3:30 PM-5:00 PM", "Guts Round (80 min)"],
        ["5:30 PM-6:30 PM", "Award Ceremony"],
    ];

    const formLink =
        "https://docs.google.com/forms/d/e/1FAIpQLScyywaWqPFLnGATcamhA_XGwfREfsu6qMkB5fx2LLUk9GRKOA/viewform?usp=share_link";
</script>

<svelte:head>
    <title>SMT 2023</title>
</svelte:head>

<svelte:window bind:innerWidth={windowWidth} />

<br />

<br id="registrationInfo" />
<Heading text="Stanford Math Tournament" size={6} textColor="black" />
<Heading text="Overview" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw;">
    <PanelBox>
        <div style="padding: 10px;">
            <p>
                <strong>TEAM SIZE:</strong> 5-6 <br />
                <strong>LOCATION:</strong> Stanford University
                <br />
                <strong>COST:</strong> $10 per student <br /> <br />
                <i
                    ><strong>Note for International Students:</strong> This page
                    is for the in-person SMT. If you would like to participate,
                    please visit <Link
                        url="/competitions/smt-2023-international"
                        text="this page."
                    />
                </i>
            </p>
        </div>
    </PanelBox>
</div>
<br />

<Heading text="Registration Information" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw;">
    <PanelBox>
        <div style="padding: 10px;">
            <p>
                This registration form is specifically for the in-person
                competition. If you are looking for SMT Online or International
                registration, those will be posted on their respective pages.
            </p>
            <HeaderButton
                text="Register for SMT 2023"
                hasArrow={false}
                href={formLink}
                isSmall
            />
        </div>
    </PanelBox>
</div>

<Heading text="Registration Timeline" size={2.5} />

<Timeline width="60%">
    <TimelineElement>
        <strong>Monday, February 13, 2023:</strong> Regular registration opens
        on Google Forms
        <br />
        <Link
            url="https://docs.google.com/forms/d/e/1FAIpQLScyywaWqPFLnGATcamhA_XGwfREfsu6qMkB5fx2LLUk9GRKOA/viewform?usp=share_link"
            text="Link to registration form"
        />
    </TimelineElement>
    <TimelineElement>
        <strong>Tuesday, March 7, 2023:</strong> Regular registration deadline on
        Google Forms
    </TimelineElement>
    <TimelineElement>
        <strong>Friday, March 10, 2023:</strong> Announcement of teams selected for
        in-person competition
    </TimelineElement>
    <TimelineElement>
        <strong>Friday, March 17, 2023:</strong> Deadline for selected teams to register
        on Eventbrite
    </TimelineElement>
    <TimelineElement>
        <strong>Tuesday, March 21, 2023:</strong> Deadline for payments on Eventbrite
        and proof of transportation
    </TimelineElement>
    <TimelineElement>
        <strong>Tuesday, March 28, 2023:</strong> Deadline for late payments on
        Eventbrite
        <br />
        <strong>Also:</strong> Deadline for student registration and waivers
    </TimelineElement>
    <TimelineElement>
        <strong>Saturday, April 8, 2023:</strong> SMT tournament day
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
                overallHeader="Tournament Schedule (8AM-6:30PM PT)"
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
        A: Teams consist of 6 students.<br />
        <br />
        Q: Can I participate in SMT remotely?<br />
        A: We will host two events: one in-person at Stanford and a separate online
        competition. Both competitions are open to all US students.<br />
        <br />
        Q: Do students on the same team have to be from the same school?<br />
        A: Yes, with one exception. Established math institutions such as A-Star
        and Euler Circle are invited to send teams with students that do not attend
        the same high schools.<br />
        <br />
        Q: What schools can participate in SMT?<br />
        A: SMT 2023 will be open to all US schools.<br />
        <br />
        Q: Can international teams participate in SMT? If so, how do they register?<br
        />
        A: No, unfortunately we will be limiting registration to US based students<br
        />
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
        Q: Which individual test should I take?<br />
        A: If you have little or no experience with contest math, we strongly recommend
        you take the General Test. Looking at past tests will help you get a sense
        of the difficulty of each test.<br />
        <br />
        <strong>Logistics</strong><br />
        Q: Do we need to have a teacher or coach attend SMT in person?<br />
        A: No, you are not required to have a teacher or coach at the tournament.<br
        />
        <br />
        Q: Can I use the problems from previous SMT tests listed below in my classroom/book/etc?<br
        />
        A: Yes! Feel free to use these problems provided you cite us.<br />
    </PanelBox>
</div>
