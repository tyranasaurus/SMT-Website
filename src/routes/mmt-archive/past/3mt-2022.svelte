<script>
    import Heading from "$lib/components/Heading.svelte";
    import Dropdown from "$lib/components/Dropdown.svelte";
    import Link from "$lib/components/Link.svelte";
    import Button from "$lib/components/Button.svelte";
    import PageHeader from "$lib/components/PageHeader.svelte";
    import Competition from "$lib/components/Competition.svelte";
    import FlexBox from "$lib/components/FlexBox.svelte";
    import Table from "$lib/components/Table.svelte";
    import PanelBox from "$lib/components/PanelBox.svelte";
    import Image from "$lib/components/Image.svelte";
    let windowWidth;
    const scheduleData = [
        {
            Day: "11/12-11/18",
            "Start Time (PT)": "All Day",
            Event: "Problem of the Day",
        },
        ["11/19", "9:00 AM-9:30 AM", "Opening Ceremony"],
        ["11/19", "9:30 AM-10:40 AM", "3MT Round (1 hour)"],
        ["11/19", "10:40 AM-11:30 AM", "Activities"],
        ["11/19", "11:30 AM-12:00 PM", "Awards Ceremony"],
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
    <title>3MT</title>
</svelte:head>

<svelte:window bind:innerWidth={windowWidth} />

<PageHeader
    title="Mustang Mini Math Tournament (3MT)"
    description="November 19, 2022: 9:00 AM - 11:30 AM PT"
    button_url="https://contestdojo.com/"
    button_text="Registration on ContestDojo!"
    button_id="registerOnContestDojo"
/>

<br /><br />

<Dropdown
    mainText="Registration Instructions and Information"
    showContent={true}
    id="showDropdown"
>
    <div style="padding: 10px;">
        <strong>COST:</strong> $5 per participant <br /> <br />
        <strong>REGISTRATION DEADLINE:</strong> November 17, 2022 <br /> <br />
        <strong>LOCATION:</strong> Discord and ContestDojo<br /> <br />
        <a
            href="https://docs.google.com/document/d/1gdpWZWvTugWZQNTl2L20TkcyfRXfii_Bu62LwlqEQ7E/edit?usp=sharing"
            target="_blank"
            ><strong>CLICK HERE FOR REGISTRATION INSTRUCTIONS</strong></a
        >
    </div>
</Dropdown> <br />

<Heading text="Schedule" size={2.5} />
<div class="schedule-wrapper">
    <FlexBox>
        <PanelBox>
            <Table
                data={scheduleData}
                width="auto"
                headerColor="#1B9AAA"
                rowColors={["var(--table-color-1)", "#ADCDD6"]}
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
            <b>$50</b>, <b>$25</b>, and <b>$25</b> gift cards will be given to the
            1st, 2nd, and 3rd place finishers within each division (not HS). 1st
            and 2nd place finishers will additionally receive a math book from AwesomeMath.
            All students will receive certificates of participation and high-scoring
            students will receive certificates of achievement.
        </p>
        <p style="font-size: 1.5em; text-align: center;">
            A wide variety of other prizes are available for top scoring
            individuals, winners of activities, and a raffle, including AoPS
            Gift Certificates, Brilliant Premium subscriptions, vouchers for <a
                target="_blank"
                href="https://mustangmath.com/classes">Mustang Math Classes</a
            >,
            <a target="_blank" href="https://www.wolfram.com/notebooks/"
                >Wolfram Notebooks</a
            >, AwesomeMath books and more!
        </p>
    </PanelBox>
</div>
<br />

<Heading text="Participant Elgibility" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw; font-size: 1.5em;">
    <PanelBox>
        <p>
            3MT is a tournament meant for <b>middle school students and below</b
            >
            from the <b>the United States and Canada</b>. Students not from the
            US or Canada should participate in the international version of the
            contest happening next January-February.
        </p>
        <p>The divisions in 3MT are as follows:</p>
        <ul style="opacity: 0.8;">
            <li><strong>Grades 6 and below: Foal Division</strong></li>
            <li><strong>Grades 7: Colt Division</strong></li>
            <li><strong>Grades 8: Stallion Division</strong></li>
        </ul>
        <p>
            Students may choose to compete in a higher division than they were
            originally assigned. Student <u><strong>may not</strong></u> compete
            in a lower division than they were originally assigned.
        </p>
        <p>
            High school students are welcome to participate, but they will
            participate in a separate High School division and will not receive
            rankings or awards.
        </p>
    </PanelBox>
</div>
<br />

<Heading text="Activities" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw; font-size: 1.5em;">
    <PanelBox>
        <p>
            <strong>Desmos Art:</strong> Get your creative (math) juices flowing
            with a Desmos art session! Draw something ingenious on the
            desmos.com graphing calculator, and see where your imagination takes
            you.<br />
        </p>
        <p>
            <strong>Very Legit Round:</strong> This is a completely normal, typical,
            100% standard, math tournament round. There is nothing suspicious about
            the problems at all...
        </p>
    </PanelBox>
</div>
<br />

<Heading text="Problem of the Day" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw; font-size: 1.5em;">
    <PanelBox>
        <p>
            POTD is a small mini-contest that will be held in the week leading
            up to 3MT. We will post a problem every day, starting on 11/12, and
            participants will have the chance to answer these problems through
            ContestDojo. Points are earned for each correct answer, and the
            person with the most points at the end will be the winner!
        </p>
    </PanelBox>
</div>
<br />

<Heading text="Rules" size={2.5} />
<Dropdown mainText="General Rules" id="showDropdown">
    <ol>
        <li>
            All contestants will be required to have their cameras and mics ON
            during the test.
        </li>
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
            Individuals may not collaborate with anyone. This includes other
            participants, parents, coaches, siblings, and friends.
        </li>
        <li>
            Individuals will be split into three divisions based on their grade
            level. As mentioned above, students may upcompete.
        </li>
    </ol>
</Dropdown>
<Dropdown mainText="Scoring & Tiebreakers" id="showDropdown">
    <p>
        Your score on the 3MT Round is simply the number of questions you get
        right - each question is worth 1 point.
    </p>
    <p>
        If two or more students get the same number of questions right, ties
        will be broken as follows:
    </p>
    <ol>
        <li>
            1. Difficulty of problems solved. This will be determined by
            whichever student has the lowest <b>tiebreaker index</b>. <br />
            The <b>tiebreaker index</b> for a student is calculated by multiplying
            the total number of correct solves per problem for each problem the student
            got correct.
        </li>
        <br />
        <li>
            2. Completion time. Should two students have the same tiebreaker
            index, ties will be broken by completion time. In particular,
            whichever student enters their final correct answer earliest will
            win this tiebreaker.
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
<Dropdown mainText="Problem of the Day" id="showDropdown">
    <ol>
        <li>
            The Daily POTD will be made available on ContestDojo at around 3 PM
            PT daily from 11/12 to 11/18 (7 total). POTDs may be solved and
            answers updated in ContestDojo for up to 24 hours from the release
            of the daily problem.
        </li>
        <li>
            Solutions to the previous day's POTD will be posted the day after in
            #potd [link to channel]
        </li>
        <li>
            Anyone who has registered for 3MT is eligible to participate in this
            contest. You must be fully set up on ContestDojo and Discord to
            properly participate.
        </li>
        <li>
            Answers to the POTD will be submitted via ContestDojo. Log into your
            student portal in order to do so (See detailed info below)
        </li>
        <li>
            Do NOT discuss the current POTD with anyone, including but not
            limited to the Mustang Math Tournament server, with your teammates,
            and any other forms of social media or in-person communication. POTD
            is an individual event. Violators of this rule will be disqualified
            from the POTD competition.
        </li>
        <li>
            No tools besides a writing utensil and pencil are permitted for
            POTD's unless otherwise specified! This includes, but is not limited
            to, calculators, rulers, compasses, protractors, and the internet.
        </li>
        <li>
            Each problem will be worth 10 points. Some problems will split these
            points across multiple parts that build upon each other.
        </li>
        <li>
            The winner of POTD will win an AwesomeMath Book. Additionally, all
            students that submit at least one POTD correctly will be entered
            into a raffle for a Wolfram|Alpha Notebook Edition.
        </li>
        <li>Any ties will be broken by total time taken for the problems</li>
    </ol>
</Dropdown>
<Dropdown mainText="FAQ" id="showDropdown">
    <p>
        <strong>Q:</strong> I'm a parent or a student, not a coach - how can I
        register? <br />
        <strong>A:</strong> MMT doesn't require you to be a coach! A parent can
        act as a coach (and register as a coach on ContestDojo) to create an
        organization and team(s) for their participating students.
        <strong>Students should not create coach accounts.</strong>
    </p>
    <p>
        <strong>Q:</strong> Why aren't there awards for high schoolers? <br />
        <strong>A:</strong> Our mission and tests are geared towards middle school
        mathematics, and thus our awards are as well. We welcome high school students
        to participate for the experience only.
    </p>
    <p>
        <strong>Q:</strong> You have three divisions, what are the differences?
        <br />
        <strong>A:</strong> Our Foal Division is for students in 6th grade and below
        and will have easier problems as compared to our Colt Division (7th grade)
        and Stallion Division (8th grade). Students may compete in divisions higher
        than their grade level but are not allowed to compete in lower divisions.
    </p>
    <p>
        <strong>Q:</strong> Where can I find practice material for the tests?
        How can we prepare? <br />
        <strong>A:</strong> You can take a look at our
        <a target="_blank" sveltekit:prefetch href="/past-exams">past tests</a>,
        and we also highly recommend looking at
        <a
            target="_blank"
            sveltekit:prefetch
            href="https://www.mathcounts.org/resources/past-competitions"
            >past MathCounts</a
        >,
        <a
            target="_blank"
            sveltekit:prefetch
            href="https://artofproblemsolving.com/wiki/index.php/AMC_Problems_and_Solutions"
            >AMC 8/10</a
        >, and
        <a
            target="_blank"
            sveltekit:prefetch
            href="https://www.ocf.berkeley.edu/~bmt/archive/">BmMT</a
        > tests as these are similar in level to the problems at MMT.
    </p>
</Dropdown>

<style>
    li {
        list-style-type: disc;
        margin-left: 20px;
    }
</style>
