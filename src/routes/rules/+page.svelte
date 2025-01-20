<script>
    import Heading from "$lib/components/Heading.svelte";
    import Dropdown from "$lib/components/Dropdown.svelte";
    import Link from "$lib/components/Link.svelte";
    import Button from "$lib/components/Button.svelte";
    import PageHeader from "$lib/components/PageHeader.svelte";
    import HeaderButton from "$lib/components/HeaderButton.svelte";
    import Testimonial from "$lib/components/Testimonial.svelte";
    import Competition from "$lib/components/Competition.svelte";
    import FlexBox from "$lib/components/FlexBox.svelte";
    import Table from "$lib/components/Table.svelte";
    import PanelBox from "$lib/components/PanelBox.svelte";
    import Image from "$lib/components/Image.svelte";
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
                "<ul><li>Systems of equations</li> <li>Quadratics</li> <li>Vieta's</li> <li>Binomial Theorem</li> <li>Radicals/Exponents</li> <li>Simon's Favorite Factoring Trick</li> <li>Ratios</li> <li>(Infinite) Geometric Series</li> <li>Arithmetic Series</li> <li>Sum/Difference of Powers</li> <li>Rate/Time</li> <li>Floor/Ceiling</li> <li>Absolute Value</li> <li>Substitution (Nested Roots/Repeated Fractions)</li> <li>Mean, Median, Mode, Range</li> <li>Telescoping</li></ul>",
            Combinatorics:
                "<ul><li>Sticks and Stones</li> <li>Permutation/Combination</li> <li>Properties of Inclusion Exclusion for three or less sets</li> <li>Basic Geometric Probability</li> <li>Conditional Probability</li> <li>Expected Values</li> <li>Complementary Counting</li> <li>Recursion</li> <li>Bijections</li> <li>Casework</li> <li>Pigeonhole Principle</li> <li>Double-counting</li> <li>Basic Invariants</li></ul>",
            Geometry:
                "<ul><li>Area Formulas</li> <li>Volume Formulas</li> <li>Shoelace Formula</li> <li>Pythagorean Theorem</li> <li>Distance Formula</li> <li>Similar Triangles</li> <li>Angle Chasing</li> <li>Power of a Point</li> <li>Basic Mass Points</li> <li>Heron's Formula</li> <li>Pick's Theorem</li> <li>Surface Area for Pyramids, Prisms, and Cones</li> <li>Arcs and Sectors</li> <li>Angle Bisector Theorem</li> <li>Internal/External Angles</li></ul>",
            "Number Theory":
                "<ul><li>Fermat's Little Theorem</li> <li>Euclidean Algorithm</li> <li>Chinese Remainder Theorem</li> <li>Divisibility</li> <li>Chicken McNugget Theorem</li> <li>GCD and LCM</li> <li>Number of Factors</li> <li>Sum of Factors</li> <li>Basic Modular Arithmetic</li> <li>Fundamental Theorem of Arithmetic</li></ul>",
        },
    ];
    const topicsSmall1 = [
        {
            Algebra:
                "<ul><li>Systems of equations</li> <li>Quadratics</li> <li>Vieta's</li> <li>Binomial Theorem</li> <li>Radicals/Exponents</li> <li>Simon's Favorite Factoring Trick</li> <li>Ratios</li> <li>(Infinite) Geometric Series</li> <li>Arithmetic Series</li> <li>Sum/Difference of Powers</li> <li>Rate/Time</li> <li>Floor/Ceiling</li> <li>Absolute Value</li> <li>Substitution (Nested Roots/Repeated Fractions)</li> <li>Mean, Median, Mode, Range</li> <li>Telescoping</li></ul>",
            Combinatorics:
                "<ul><li>Sticks and Stones</li> <li>Permutation/Combination</li> <li>Properties of Inclusion Exclusion for three or less sets</li> <li>Basic Geometric Probability</li> <li>Conditional Probability</li> <li>Expected Values</li> <li>Complementary Counting</li> <li>Recursion</li> <li>Bijections</li> <li>Casework</li> <li>Pigeonhole Principle</li> <li>Double-counting</li> <li>Basic Invariants</li></ul>",
        },
    ];
    const topicsSmall2 = [
        {
            Geometry:
                "<ul><li>Area Formulas</li> <li>Volume Formulas</li> <li>Shoelace Formula</li> <li>Pythagorean Theorem</li> <li>Distance Formula</li> <li>Similar Triangles</li> <li>Angle Chasing</li> <li>Power of a Point</li> <li>Basic Mass Points</li> <li>Heron's Formula</li> <li>Pick's Theorem</li> <li>Surface Area for Pyramids, Prisms, and Cones</li> <li>Arcs and Sectors</li> <li>Angle Bisector Theorem</li> <li>Internal/External Angles</li></ul>",
            "Number Theory":
                "<ul><li>Fermat's Little Theorem</li> <li>Euclidean Algorithm</li> <li>Chinese Remainder Theorem</li> <li>Divisibility</li> <li>Chicken McNugget Theorem</li> <li>GCD and LCM</li> <li>Number of Factors</li> <li>Sum of Factors</li> <li>Basic Modular Arithmetic</li> <li>Fundamental Theorem of Arithmetic</li></ul>",
        },
    ];
    const topicsAlgebra = [
        {
            Algebra:
                "<ul><li>Systems of equations</li> <li>Quadratics</li> <li>Vieta's</li> <li>Binomial Theorem</li> <li>Radicals/Exponents</li> <li>Simon's Favorite Factoring Trick</li> <li>Ratios</li> <li>(Infinite) Geometric Series</li> <li>Arithmetic Series</li> <li>Sum/Difference of Powers</li> <li>Rate/Time</li> <li>Floor/Ceiling</li> <li>Absolute Value</li> <li>Substitution (Nested Roots/Repeated Fractions)</li> <li>Mean, Median, Mode, Range</li> <li>Telescoping</li></ul>",
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
                "<ul><li>Area Formulas</li> <li>Volume Formulas</li> <li>Shoelace Formula</li> <li>Pythagorean Theorem</li> <li>Distance Formula</li> <li>Similar Triangles</li> <li>Angle Chasing</li> <li>Power of a Point</li> <li>Basic Mass Points</li> <li>Heron's Formula</li> <li>Pick's Theorem</li> <li>Surface Area for Pyramids, Prisms, and Cones</li> <li>Arcs and Sectors</li> <li>Angle Bisector Theorem</li> <li>Internal/External Angles</li></ul>",
        },
    ];
    const topicsNT = [
        {
            "Number Theory":
                "<ul><li>Fermat's Little Theorem</li> <li>Euclidean Algorithm</li> <li>Chinese Remainder Theorem</li> <li>Divisibility</li> <li>Chicken McNugget Theorem</li> <li>GCD and LCM</li> <li>Number of Factors</li> <li>Sum of Factors</li> <li>Basic Modular Arithmetic</li> <li>Fundamental Theorem of Arithmetic</li></ul>",
        },
    ];



const testInfo = "https://docs.google.com/document/d/1CZOsMz27ZdP3Ftj3DoCS9h8yFcukC5eu3nzf7GMdfWs/edit?usp=sharing";
const rulesScoring = "https://docs.google.com/document/d/1gHIbirfCyn_2qybVmC0AhN3l2z2UVybVmsdFw8-T8W4/edit?usp=sharing";
const cheating = "https://docs.google.com/document/d/1wYJbRgsZYBsGPNTlu6QEsgIG0GbEviulDaI-3oFamZU/edit?usp=sharing";
const answerformat = "https://docs.google.com/document/d/1TWJQIqpJzT7engSTAJ9dIphMcG07vevcqWbsKhVOMqg/edit?usp=sharing";
const notation = "https://drive.google.com/file/d/1jhHz2K4yUsKICDj4HvRhcICmHrINb1hL/view?usp=sharing";
</script>

<svelte:head>
    <title>SMT Rules</title>
</svelte:head>

<svelte:window bind:innerWidth={windowWidth} />

<br><br>
<Heading text="SMT Rules" size={4} textColor="var(--heading-color)"/>
<div class="section-wrapper col-sm" style="margin-top: 1vh">
    <PanelBox>
        <div class="section-item">
            <p>
            The mathematical expectations for each test (both individual and team) can be found in the document below. It outlines the content that each test might include, and can serve as a useful guide for those debating which test to take. 
            </p>
            <HeaderButton
                text="Test Information"
                href={testInfo}
                isSmall
                centered
                newTab
            />
        </div>
        <div class="section-item">
            <p>
                The specific test rules, parameters (i.e. duration), and scoring can be found in the document below. It further outlines total scoring for the tournament, as well as awards and protests. 
            </p>
            <HeaderButton
                text="Scoring"
                href={rulesScoring}
                isSmall
                centered
                newTab
            />
        </div>
        <div class="section-item">
            <p>
                By participating in the tournament, one agrees to maintain and uphold academic honesty, and abide by the Code of Conduct and The Stanford Honor Code. These can be reviewed below.
            </p>
            <HeaderButton
                text="Honor Code"
                href={cheating}
                isSmall
                centered
                newTab
            />
        </div>
    <div class="section-item">
        <p>
            Only answers in the specified format will be labelled as correct, most notably on tests that are not proof-based. Please take time to review the answer formatting rules, as well as common mathematical notation used in the tests in the documents below. 
        </p>
        <div class="buttons-wrapper">
            <HeaderButton
                text="Answer Format"
                href={answerformat}
                isSmall
                newTab
            />
            <HeaderButton
                text="Notation"
                href={notation}
                isSmall
                newTab
            />
        </div>
    </div>
    </PanelBox>
</div>

<style>
    .outside {
        background-color: var(--background-white);
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        overflow: hidden;
    }

    .descript {
        width: 70%;
        font-weight: 300;
        font-size: 22px;
        color: black;
    }

    .other-text {
        font-weight: 300;
        font-size: 22px;
        color: black;
    }

    .scroll-notification {
        display: flex;
        background-color: #981c1d;
        border-radius: 10px;
        padding: 10px;
        color: white;
        justify-content: center;
        align-items: center;
        width: 300px;
        flex-grow: 0;
    }

    .mobile-flex {
        display: flex;
        flex-direction: row;
    }

    .infodiv {
        max-width: 50%;
    }

    .flex-item {
        width: 100%;
    }

    .border-right {
        border-right: 1px solid var(--black-border);
    }

    .tournament {
        padding-left: 20px;
        padding-right: 20px;
        padding-bottom: 5px;
        min-height: 100%;
    }

    @media (max-width: 700px) {
        .outside {
            background-color: var(--background-white);
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }

        .descript {
            width: auto;
            font-size: 16px;
            text-align: center;
        }

        .mobile-flex {
            display: flex;
            flex-direction: column;
        }

        .infodiv {
            max-width: unset;
        }
    }

    .header {
        text-align: center;
        position: relative;
        height: calc(100% - 70px);
    }

    .svg {
        position: absolute;
        margin-left: auto;
        margin-right: auto;
        left: 0;
        right: 0;
        text-align: center;
    }

    .minidiv {
        z-index: 9;
        margin: 20px;
        max-width: 90%;
        text-align: left;
    }

    .scroll-notification {
        position: fixed;
        bottom: 5px;
        z-index: 10;
        align-self: center;
        width: 150px;
        height: 25px;
        border-radius: 25px;
        cursor: pointer;
        margin-bottom: 30px;
    }

    .buttons-wrapper {
        display: flex;
        gap: 1rem;
    }
</style>
