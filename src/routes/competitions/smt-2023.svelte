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
            Day: "4/22-4/29",
            "Start Time (PT)": "All Day",
            Event: "Problem of the Day",
        },
        ["4/29", "8:30 AM-9:00 AM", "Check-in"],
        ["4/29", "9:00 AM-9:30 AM", "Opening Ceremony & Contest Instructions"],
        ["4/29", "9:30 AM-10:55 AM", "Mounting Mayhem (75 minutes)"],
        ["4/29", "10:55 AM-12:05 PM", "Herding Hexes (60 minutes) "],
        ["4/29", "12:05 PM-1:00 PM", "Lunch Break (55 minutes)"],
        ["4/29", "1:00 PM-2:10 PM", "Mystery Mare (60 minutes)"],
        ["4/29", "2:10 PM-3:20 PM", "Gallop (60 minutes)"],
        ["4/29", "3:20 PM-4:30 PM", "Optional Activities"],
        ["4/29", "4:30 PM", "Awards Ceremony"],
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
    <title>MMT 2023</title>
</svelte:head>

<svelte:window bind:innerWidth={windowWidth} />

<PageHeader
    title="Mustang Math Tournament (MMT) California"
    description="April 29, 2023: 9:00 AM - 4:30 PM PT"
    button_url="https://contestdojo.com"
    button_text="Register for Competition!"
    button_id="registerOnContestDojo"
    target="_blank"
/>

<br />

<br id="registrationInfo" />
<Heading text="Overview" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw;">
    <PanelBox>
        <div style="padding: 10px;">
            <p>
                <strong>TEAM SIZE:</strong> 3-4* <br />
                <strong>LOCATION:</strong>Castro Valley, California**<br />
                <strong>EARLY HORSE COST:</strong> $10 per participant (Register
                before
                <strong>March 14th, 2023</strong>
                to receive the early horse price!)<br />
                <strong>NORMAL COST:</strong> $15 per participant (Register
                before
                <strong>April 22nd, 2023</strong>
                to participate)<br /> <br />
                <a
                    href="https://docs.google.com/document/d/1FRL4DLS2RVbbMRKe2r0t7K2Rhjabwr45TdgM0ISDKnQ/edit?usp=sharing"
                    target="_blank"
                    ><strong>CLICK HERE FOR REGISTRATION INSTRUCTIONS</strong
                    ></a
                >
                <br /><br />
                <i
                    ><strong>*:</strong> Incomplete teams of 1-2 may be merged with
                    other teams to make a full team of 3-4</i
                ><br />
                <i
                    ><strong>**:</strong> Location subject to change within 20 miles</i
                ><br /><br />
                <i
                    ><strong>Note for International Students:</strong> Students
                    not in Canada or the United States should participate in the
                    international version of our tournament being run by SIMCC.
                    Email us at
                    <a href="mailto:tournament@mustangmath.com"
                        >tournament@mustangmath.com</a
                    > if you're interested.</i
                ><br /><br />
                <i
                    ><strong>Note for Students in California:</strong> Students
                    living within 50 miles of our in-person sites
                    <strong>must</strong>
                    participate in person. If you have an extenuating circumstance
                    that would prevent this please send an email to
                    <a href="mailto:tournament@mustangmath.com"
                        >tournament@mustangmath.com</a
                    >, and we'll grant you permission to participate online.</i
                >
            </p>
        </div>
    </PanelBox>
</div>
<br />

<Heading text="Timeline" size={2.5} />
<div class="schedule-wrapper">
    <Timeline width="60%">
        <TimelineElement>
            <p>hi</p>
        </TimelineElement>
        <TimelineElement>
            <h1>Another timeline element</h1>
        </TimelineElement>
    </Timeline>

    <FlexBox>
        <PanelBox>
            <Table
                data={scheduleData}
                width="auto"
                cellPadding={5}
                cellPaddingRight={20}
                tableStyle="margin-left: auto; margin-right: auto"
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

<Heading text="Awards" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw;">
    <PanelBox>
        <p style="font-size: 1.5em; text-align: center;">
            Medals will be given to (at minimum) the members of the top 3 teams
            of each division, along with certificates of participation to all
            students and certificates of achievement to high-scoring teams. A
            wide variety of other prizes are available for top scoring teams,
            winners of activities, and a raffle including prizes from Wolfram,
            AoPS, and more!
        </p>
    </PanelBox>
</div>
<br />

<Heading text="Rules" size={2.5} />
<Dropdown mainText="General Rules" id="showDropdown">
    <ol>
        <li>
            No cheating - This contest has a zero-tolerance cheating policy. Any
            evidence of cheating may lead to immediate disqualification, or any
            other punishment deemed appropriate by competition staff.
        </li>
        <li>
            No calculators, rulers, compasses, protractors, or other aids are
            permitted.
        </li>
        <li>
            You may not use the Internet as a resource at any point during a
            test.
        </li>
        <ol type="a">
            <li>
                In order to help enforce this, we may require individuals to
                provide a solution for a problem during the competition - so
                keep track of your work!
            </li>
        </ol>
        <li>
            All communication will take place through the Discord platform.
            <ol type="a">
                Scores, important information, documents, etc. will only be
                communicated through this platform on the day of the contest.
            </ol>
            <ol type="a">
                All teams should be communicating with each other on this
                platform ONLY.
            </ol>
            <ol type="a">
                <strong
                    >Students under 13 years of age should use a parent-created
                    and monitored Discord account.</strong
                >
            </ol>
        </li>
        <li>
            The team divisions are determined by the highest grade level amongst
            the team members. Teams with 1 or more 8th graders will be in the <strong
                >Stallion</strong
            >
            division, teams with 7th graders and below will be in the
            <strong>Colt</strong>
            division, and teams with 6th graders and below will be in the
            <strong>Foal</strong>
            division. Teams may <em>choose</em> to compete in a higher division,
            if they&rsquo;d like.
        </li>
    </ol>
</Dropdown>
<Dropdown mainText="Answer Formatting Rules" id="showDropdown">
    <ol>
        <li>
            Carry out any reasonable calculations. For instance, you should
            evaluate any expressions which will take negligible time to evaluate
            (such as 1/2+1/3). You don't have to carry out unreasonable
            calculations, including large powers (e.g. 7<sup>8</sup>), large
            factorials, large products, and trigonometric functions which cannot
            be expressed in terms of radicals.
        </li>
        <li>
            Write rational numbers in lowest terms. Decimals are also
            acceptable, provided they are exact.
        </li>
        <li>
            Move all square factors outside radicals. For example, write 3√7
            instead of √63.
        </li>
        <li>
            Denominators need to be rationalized. For example, write 1/√2 as
            √2/2 instead.
        </li>
        <li>Do not express an answer using a repeated sum or product.</li>
        <li>
            Here are some examples of simplified answers, and examples of
            unsimplified answers with simplified equivalents:
            <div style="margin-top: 5px">
                <Image
                    url="../mmt-2022/acceptable-answers.png"
                    alt="Acceptable answer examples"
                />
            </div>
            <div style="margin-top: 5px">
                <Image
                    url="../mmt-2022/unacceptable-answers.png"
                    alt="Unacceptable answer examples"
                />
            </div>
        </li>
    </ol>
</Dropdown>
<Dropdown mainText="Potential Topics Covered" id="showDropdown">
    <p id="disclaimer">
        Disclaimer: While most problems should fall within the scope of these
        topics, there may be a few that are not.
    </p>
    {#if windowWidth > 1000}
        <Table
            data={topicsCovered}
            width="100%"
            headerColor="#1B9AAA"
            rowColors={["var(--table-color-1)"]}
            cellPadding={5}
            cellPaddingRight={20}
            textSize={1}
            cellStyle="vertical-align: top; font-size: {windowWidth / 1200}em;"
            tableStyle="table-layout: fixed; padding: 10px;"
            headerStyle="font-size: {windowWidth / 1500}em;"
        />
    {:else if windowWidth > 800}
        <Table
            data={topicsSmall1}
            width="100%"
            headerColor="#1B9AAA"
            rowColors={["var(--table-color-1)"]}
            cellPadding={5}
            cellPaddingRight={20}
            textSize={1}
            cellStyle="vertical-align: top; font-size: {windowWidth / 800}em;"
            tableStyle="table-layout: fixed; padding: 10px;"
            headerStyle="font-size: {windowWidth / 800}em;"
        />
        <Table
            data={topicsSmall2}
            width="100%"
            headerColor="#1B9AAA"
            rowColors={["var(--table-color-1)"]}
            cellPadding={5}
            cellPaddingRight={20}
            textSize={1}
            cellStyle="vertical-align: top; font-size: {windowWidth / 800}em;"
            tableStyle="table-layout: fixed; padding: 10px;"
            headerStyle="font-size: {windowWidth / 800}em;"
        />
    {:else}
        <Table
            data={topicsAlgebra}
            width="100%"
            rowColors={["var(--table-color-1)"]}
            cellPadding={5}
            cellPaddingRight={20}
            textSize={1}
            cellStyle="vertical-align: top; font-size: {windowWidth / 500}em;"
            tableStyle="table-layout: fixed; padding: 10px;"
            headerStyle="font-size: {windowWidth / 500}em;"
        />
        <Table
            data={topicsCombo}
            width="100%"
            headerColor="#1B9AAA"
            rowColors={["var(--table-color-1)"]}
            cellPadding={5}
            cellPaddingRight={20}
            textSize={1}
            cellStyle="vertical-align: top; font-size: {windowWidth / 500}em;"
            tableStyle="table-layout: fixed; padding: 10px;"
            headerStyle="font-size: {windowWidth / 500}em;"
        />
        <Table
            data={topicsGeo}
            width="100%"
            headerColor="#1B9AAA"
            rowColors={["var(--table-color-1)"]}
            cellPadding={5}
            cellPaddingRight={20}
            textSize={1}
            cellStyle="vertical-align: top; font-size: {windowWidth / 500}em;"
            tableStyle="table-layout: fixed; padding: 10px;"
            headerStyle="font-size: {windowWidth / 500}em;"
        />
        <Table
            data={topicsNT}
            width="100%"
            headerColor="#1B9AAA"
            rowColors={["var(--table-color-1)"]}
            cellPadding={5}
            cellPaddingRight={20}
            textSize={1}
            cellStyle="vertical-align: top; font-size: {windowWidth / 500}em;"
            tableStyle="table-layout: fixed; padding: 10px;"
            headerStyle="font-size: {windowWidth / 500}em;"
        />
    {/if}
</Dropdown>
<Dropdown mainText="ROUND 1: Mounting Mayhem (Puzzle)" id="showDropdown">
    <ol>
        <li>
            The Mounting Mayhem Round will consist of a series of progressively
            harder logic puzzles. Students will have 15 minutes to learn the
            rules and basic strategy of the puzzles, then 60 minutes to solve as
            many of them as possible.
        </li>
        <li>
            Puzzles often require out-of-the-box thinking although all topics
            can readily be understood and grasped by middle schoolers.
        </li>
        <li>
            Harder puzzles will be worth more points, but these puzzles will be
            longer and/or require more creativity — you must decide what
            problems to focus your time on to optimize your team score.
        </li>
    </ol>
</Dropdown>
<Dropdown mainText="ROUND 2: Herding Hexes" id="showDropdown">
    <ol>
        <li>
            The “Herding Hexes” Round will consist of 25-30 questions to be
            solved in 60 minutes.
        </li>
        <li>
            The questions will be laid out on a grid of connected hexagons, with
            more difficult problems being located furthest from the center.
        </li>
        <li>
            Your score in the round will be determined by the problems you get
            correct, with bonus points available for having more correct answers
            connected within the grid!
        </li>
        <li>
            You are not necessarily expected to solve all the questions in this
            round within the allotted time. Instead, we encourage you to
            strategize how you might use your time to maximize your points!
        </li>
    </ol>
</Dropdown>
<Dropdown mainText="ROUND 3: Mystery Mare" id="showDropdown">
    <ol>
        <li>
            The Mystery Mare round is exactly that — a mystery! The rules of the
            round will be revealed on competition day.
        </li>
        <li>
            Hints about the nature of the round may be revealed as the
            competition date nears.
        </li>
    </ol>
</Dropdown>
<Dropdown mainText="ROUND 4: Gallop" id="showDropdown">
    <ol>
        <li>
            The Gallop Round will consist of 24 questions to be solved in 60
            minutes.
        </li>
        <li>
            The questions will be divided into 8 sets of 3 questions each, and
            you <strong>must submit the answers to one set</strong> before accessing
            the problems for the next. This means you must strategize when to submit
            each set (incomplete or not) to ensure you get access to as many questions
            as possible.
        </li>
        <li>
            The problems will get progressively more difficult, and later
            problems will be worth more points.
        </li>
        <li>
            Submissions will be scored immediately and a live score of all
            participating teams will be available during the competition.
            Prepare for the adrenaline rush!
        </li>
    </ol>
</Dropdown>
<!--
<Dropdown mainText="FAQ" id="showDropdown">
    <p>
        <strong>Q:</strong> I'm a parent or a student, not a coach - how can I register? <br />
        <strong>A:</strong> MMT doesn't require you to be a coach! A parent can act as a coach (and register as a coach on ContestDojo) to create an organization and team(s) for their participating students. <strong>Students should not create coach accounts.</strong>
    </p>
    <p>
        <strong>Q:</strong> I have students that are interested in participating, but they are not a full team of 4 and would like to be paired up with other incomplete teams! How can we do this?<br />
        <strong>A:</strong> Use our <a target="_blank" href="https://tinyurl.com/MMT2023TeamFinder">Teammate Finder Spreadsheet</a>! There, you can input your parent/coach contact information and find others to join your team! <strong>Students should not create coach accounts.</strong>
    </p>
    <p>
        <strong>Q:</strong> Do we have to participate separately from our own homes? Or can our entire team meet up and take the test together? <br />
        <strong>A:</strong> Absolutely, your team can meet up and take the test together! We still require that your team is present on Discord with the video on and all members visible so that you can receive information in a timely manner!
    </p>
    <p>
        <strong>Q:</strong> Where can I find practice material for the tests? How can we prepare? <br />
        <strong>A:</strong> You can take a look at our <a target="_blank" sveltekit:prefetch href="/resources">past tests</a>, and we also highly recommend looking at <a target="_blank" sveltekit:prefetch href="https://www.mathcounts.org/resources/past-competitions">past MathCounts</a>, <a target="_blank" sveltekit:prefetch href="https://artofproblemsolving.com/wiki/index.php/AMC_Problems_and_Solutions">AMC 8/10</a>, and <a target="_blank" sveltekit:prefetch href="https://www.ocf.berkeley.edu/~bmt/archive/">BmMT</a> tests as these are similar in level to the problems at MMT.
    </p>
</Dropdown>
-->
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
