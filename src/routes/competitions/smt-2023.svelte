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
        "https://docs.google.com/forms/d/e/1FAIpQLScyywaWqPFLnGATcamhA_XGwfREfsu6qMkB5fx2LLUk9GRKOA/viewform?usp=share_link";
</script>

<svelte:head>
    <title>SMT 2023</title>
</svelte:head>

<svelte:window bind:innerWidth={windowWidth} />

<br />

<br id="registrationInfo" />
<Heading text="Stanford Math Tournament 2023" size={4} textColor="var(--heading-color)"/>
<Heading text="Overview" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw;">
    <PanelBox>
        <div style="padding: 10px;">
            <p>
                <strong>DATE:</strong> 4/8/2023 <br />
                <strong>LOCATION:</strong> Stanford University <br />
                <strong>WHO:</strong> High School students residing within the United States <br />
                <strong>TEAM SIZE:</strong> 5-6 <br />
                <strong>COST:</strong> $10 per student (Financial aid available upon request!) <br /> <br />
                <i
                    ><strong>Note for International Students:</strong> This page
                    is for the in-person SMT, which you are not eligible for. If you would like to participate,
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

<Heading text="Application Information" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw;">
    <PanelBox>
        <div style="padding: 10px;">
            <p>For SMT 2023, Stanford University policy limits us to 42 teams of 5-6 students from the United States in-person at Stanford’s campus. As such, we are now accepting applications for in-person participation from United States based schools and established mathematical organizations. We will not be accepting individual applications or applications for teams of size less than 5. All teams who don’t want to travel or are international should participate in our online tournaments. </p>
            <p>We will be accepting 25 teams from within the Bay Area (defined as within 150 mi of Stanford University), and 17 are from other domestic locations. Of these, 10 Bay Area teams and 7 Domestic teams will be merit-based - selected on performance in previous year’s tournaments, and the rest will be selected based on a lottery system. The remaining teams will not be allowed to come in person and should participate in the online tournament happening on April 9, 2023.</p>
            <HeaderButton
                text="Apply for SMT 2023"
                hasArrow={false}
                href={formLink}
                isSmall
            />
        </div>
    </PanelBox>
</div>

<Heading text="COVID-19 Policy" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw;">
    <PanelBox>
        <div style="padding: 10px;">
            <p>Proof of Vaccination and Proof of Negative COVID test within 24 hours of the start of the program are required. Students looking to request exemption from this protocol would have to email <a href="mailto:protectminors@stanford.edu">mailto:protectminors@stanford.edu</a>.</p>
        </div>
    </PanelBox>
</div>

<Heading text="Registration Timeline" size={2.5} />

<Timeline width="60%">
    <TimelineElement>
        <strong>Monday, February 13, 2023:</strong> In-person Application Form opens
        <br />
        <Link
            url="https://docs.google.com/forms/d/e/1FAIpQLScyywaWqPFLnGATcamhA_XGwfREfsu6qMkB5fx2LLUk9GRKOA/viewform?usp=share_link"
            text="Link to registration form"
        />
    </TimelineElement>
    <TimelineElement>
        <strong>Wednesday, March 8, 2023 at 11:59 PM PT:</strong> Application Deadline
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
        <strong>Friday, March 24, 2023:</strong> Deadline for proof of travel and housing.
    </TimelineElement>
    <TimelineElement>
        <strong>April 1, 2023:</strong> Deadline for student waiver submission.
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
        A: Teams must consist of 5-6 members. Teams with less or more students will not be accepted.<br />
        <br />
        Q: Can I participate in SMT remotely?<br />
        A: Yes, see the SMT Online and SMT International Pages<br />
        <br />
        Q: Do students on the same team have to be from the same school or established mathematical organization?<br />
        A: Yes, students must be from the same school or mathematical organization<br />
        <br />
        Q: What schools or organizations can participate in SMT?<br />
        A: SMT 2023 will be open to all domestic students from US-based schools or organizations.<br />
        <br />
        Q: Can international teams participate in SMT? If so, how do they register?<br
        />
        A: Yes, but they must participate in SMT International - see that page for more details.<br
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
        <!--
        Q: Which individual test should I take?<br />
        A: If you have little or no experience with contest math, we strongly recommend
        you take the General Test. Looking at past tests will help you get a sense
        of the difficulty of each test.<br />
        <br />
        -->
        <strong>Logistics</strong><br />
        Q: Do we need to have a teacher or coach attend SMT in person?<br />
        A: Yes, you must have at least one authorized adult chaperone present per team.<br/>
        <br />
        Q: Can I use the problems from previous SMT tests listed below in my classroom/book/etc?<br
        />
        A: Yes! Feel free to use these problems provided you cite us in the format (Stanford Math Tournament [Year] [Round] [Problem #])<br />
    </PanelBox>
</div>
