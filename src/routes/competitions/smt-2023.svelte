<script>
    import Heading from "$lib/components/Heading.svelte";
    import Dropdown from "$lib/components/Dropdown.svelte";
    import Link from "$lib/components/Link.svelte";
    import Button from "$lib/components/Button.svelte";
    import PageHeader from "$lib/components/PageHeader.svelte";
    import Testimonial from "$lib/components/Testimonial.svelte";
    import Competition from "$lib/components/Competition.svelte";
    import FlexBox from "$lib/components/FlexBox.svelte";
    import Table from "$lib/components/Table.svelte";
    import PanelBox from "$lib/components/PanelBox.svelte";
    import Image from "$lib/components/Image.svelte";
    import Timeline from "$lib/components/timeline/Timeline.svelte";
    import TimelineElement from "$lib/components/timeline/TimelineElement.svelte";
    let windowWidth;
    const scheduleData = [
        {
            Time: "8:00 AM-8:30 AM",
            Event: "Opening Ceremony",
            Location: "LOCATION TBA",
        },
        ["9 AM-10:20 AM", "Power Round (80 min)", "LOCATION TBA"],
        ["10:30AM-11:30AM", "Team Round (50 min)", "LOCATION TBA"],
        ["11:30AM-1PM", "Lunch Break (1.5 hr)", "LOCATION TBA"],
        [
            "1:15PM-3:15PM",
            "Individual Round(s)<br>- 2 x 50 min (subject)<br>- 110 min (general)",
            "LOCATION TBA",
        ],
        ["3:30 PM-5:00 PM", "Guts Round (80 min)", "LOCATION TBA"],
        ["5:30 PM-6:30 PM", "Award Ceremony", "LOCATION TBA"],
    ];

    const topicsCovered = [
        {
            Algebra:
                "<ul><li>Systems of equations</li> <li>Quadratics</li> <li>Vieta’s</li> <li>Binomial Theorem</li> <li>Radicals/Exponents</li> <li>Simon’s Favorite Factoring Trick</li> <li>Ratios</li> <li>(Infinite) Geometric Series</li> <li>Arithmetic Series</li> <li>Sum/Difference of Powers</li> <li>Rate/Time</li> <li>Floor/Ceiling</li> <li>Absolute Value</li> <li>Substitution (Nested Roots/Repeated Fractions)</li> <li>Mean, Median, Mode, Range</li> <li>Telescoping</li></ul>",
            Combinatorics:
                "<ul><li>Sticks and Stones</li> <li>Permutation/Combination</li> <li>Properties of Inclusion Exclusion for three or less sets</li> <li>Basic Geometric Probability</li> <li>Conditional Probability</li> <li>Expected Values</li> <li>Complementary Counting</li> <li>Recursion</li> <li>Bijections</li> <li>Casework</li> <li>Pigeonhole Principle</li> <li>Double-counting</li> <li>Basic Invariants</li></ul>",
            Geometry:
                "<ul><li>Area Formulas</li> <li>Volume Formulas</li> <li>Shoelace Formula</li> <li>Pythagorean Theorem</li> <li>Distance Formula</li> <li>Similar Triangles</li> <li>Angle Chasing</li> <li>Power of a Point</li> <li>Basic Mass Points</li> <li>Heron’s Formula</li> <li>Pick’s Theorem</li> <li>Surface Area for Pyramids, Prisms, and Cones</li> <li>Arcs and Sectors</li> <li>Angle Bisector Theorem</li> <li>Internal/External Angles</li></ul>",
            "Number Theory":
                "<ul><li>Fermat’s Little Theorem</li> <li>Euclidean Algorithm</li> <li>Chinese Remainder Theorem</li> <li>Divisibility</li> <li>Chicken McNugget Theorem</li> <li>GCD and LCM</li> <li>Number of Factors</li> <li>Sum of Factors</li> <li>Basic Modular Arithmetic</li> <li>Fundamental Theorem of Arithmetic</li></ul>",
        },
    ];
    const topicsSmall1 = [
        {
            Algebra:
                "<ul><li>Systems of equations</li> <li>Quadratics</li> <li>Vieta’s</li> <li>Binomial Theorem</li> <li>Radicals/Exponents</li> <li>Simon’s Favorite Factoring Trick</li> <li>Ratios</li> <li>(Infinite) Geometric Series</li> <li>Arithmetic Series</li> <li>Sum/Difference of Powers</li> <li>Rate/Time</li> <li>Floor/Ceiling</li> <li>Absolute Value</li> <li>Substitution (Nested Roots/Repeated Fractions)</li> <li>Mean, Median, Mode, Range</li> <li>Telescoping</li></ul>",
            Combinatorics:
                "<ul><li>Sticks and Stones</li> <li>Permutation/Combination</li> <li>Properties of Inclusion Exclusion for three or less sets</li> <li>Basic Geometric Probability</li> <li>Conditional Probability</li> <li>Expected Values</li> <li>Complementary Counting</li> <li>Recursion</li> <li>Bijections</li> <li>Casework</li> <li>Pigeonhole Principle</li> <li>Double-counting</li> <li>Basic Invariants</li></ul>",
        },
    ];
    const topicsSmall2 = [
        {
            Geometry:
                "<ul><li>Area Formulas</li> <li>Volume Formulas</li> <li>Shoelace Formula</li> <li>Pythagorean Theorem</li> <li>Distance Formula</li> <li>Similar Triangles</li> <li>Angle Chasing</li> <li>Power of a Point</li> <li>Basic Mass Points</li> <li>Heron’s Formula</li> <li>Pick’s Theorem</li> <li>Surface Area for Pyramids, Prisms, and Cones</li> <li>Arcs and Sectors</li> <li>Angle Bisector Theorem</li> <li>Internal/External Angles</li></ul>",
            "Number Theory":
                "<ul><li>Fermat’s Little Theorem</li> <li>Euclidean Algorithm</li> <li>Chinese Remainder Theorem</li> <li>Divisibility</li> <li>Chicken McNugget Theorem</li> <li>GCD and LCM</li> <li>Number of Factors</li> <li>Sum of Factors</li> <li>Basic Modular Arithmetic</li> <li>Fundamental Theorem of Arithmetic</li></ul>",
        },
    ];
    const topicsAlgebra = [
        {
            Algebra:
                "<ul><li>Systems of equations</li> <li>Quadratics</li> <li>Vieta’s</li> <li>Binomial Theorem</li> <li>Radicals/Exponents</li> <li>Simon’s Favorite Factoring Trick</li> <li>Ratios</li> <li>(Infinite) Geometric Series</li> <li>Arithmetic Series</li> <li>Sum/Difference of Powers</li> <li>Rate/Time</li> <li>Floor/Ceiling</li> <li>Absolute Value</li> <li>Substitution (Nested Roots/Repeated Fractions)</li> <li>Mean, Median, Mode, Range</li> <li>Telescoping</li></ul>",
        },
    ];
    const topicsCombo = [
        {
            Combinatorics:
                "<ul><li>Sticks and Stones</li> <li>Permutation/Combination</li> <li>Properties of Inclusion Exclusion for three or less sets</li> <li>Basic Geometric Probability</li> <li>Conditional Probability</li> <li>Expected Values</li> <li>Complementary Counting</li> <li>Recursion</li> <li>Bijections</li> <li>Casework</li> <li>Pigeonhole Principle</li> <li>Double-counting</li> <li>Basic Invariants</li></ul>",
        },
    ];
    const topicsGeo = [
        {
            Geometry:
                "<ul><li>Area Formulas</li> <li>Volume Formulas</li> <li>Shoelace Formula</li> <li>Pythagorean Theorem</li> <li>Distance Formula</li> <li>Similar Triangles</li> <li>Angle Chasing</li> <li>Power of a Point</li> <li>Basic Mass Points</li> <li>Heron’s Formula</li> <li>Pick’s Theorem</li> <li>Surface Area for Pyramids, Prisms, and Cones</li> <li>Arcs and Sectors</li> <li>Angle Bisector Theorem</li> <li>Internal/External Angles</li></ul>",
        },
    ];
    const topicsNT = [
        {
            "Number Theory":
                "<ul><li>Fermat’s Little Theorem</li> <li>Euclidean Algorithm</li> <li>Chinese Remainder Theorem</li> <li>Divisibility</li> <li>Chicken McNugget Theorem</li> <li>GCD and LCM</li> <li>Number of Factors</li> <li>Sum of Factors</li> <li>Basic Modular Arithmetic</li> <li>Fundamental Theorem of Arithmetic</li></ul>",
        },
    ];
</script>

<svelte:head>
    <title>SMT 2023</title>
</svelte:head>

<svelte:window bind:innerWidth={windowWidth} />

<PageHeader
    title="Stanford Math Tournament"
    description="April 8, 2023: 8:00 AM - 6:30 PM PT"
    button_url="https://docs.google.com/forms/d/e/1FAIpQLScyywaWqPFLnGATcamhA_XGwfREfsu6qMkB5fx2LLUk9GRKOA/viewform?usp=share_link"
    button_text="Register for Competition!"
    button_id="registerGoogleForm"
    target="_blank"
/>

<br />

<br id="registrationInfo" />
<Heading text="Overview" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw;">
    <PanelBox>
        <div style="padding: 10px;">
            <p>
                <strong>TEAM SIZE:</strong> 5-6 <br />
                <strong>LOCATION:</strong> Stanford University, exact location
                TBA <br />
                <strong>COST:</strong> $10 per student <br /> <br />
                <i
                    ><strong>Note for International Students:</strong> we are unfortunately
                    unable to invite international students for the 2023 competition.
                    This may change in future years.
                </i>
            </p>
        </div>
    </PanelBox>
</div>
<br />

<Heading text="Registration Timeline" size={2.5} />

<!--
Monday February 13, 2023 - Regular registration opens on Google Forms
https://docs.google.com/forms/d/1Ly8MopxSsMgsT1ZYyZ9s5c-iCiOyEUq5H1DmSB90iUc/edit
Tuesday March 7, 2023 - Regular Registration deadline on Google Forms
Friday March 10, 2023 - Announcement of teams selected for in-person competition
Friday March 17th, 2023 - Deadline for selected teams to register on Eventbrite
Tuesday, March 21st, 2023 - Deadline for payments on Eventbrite and proof of transportation
Tuesday, March 28th, 2023 - Deadline for late payments on Eventbrite
Tuesday, March 28th, 2023 - Deadline for student registration and waivers 
Saturday April 8, 2023 - SMT tournament day
-->

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

<br />

<br /><br />

<style>
    li {
        list-style-type: disc;
        margin-left: 20px;
    }
</style>
