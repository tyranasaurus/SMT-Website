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
    import Questions from "$lib/FAQ-smt-2023-online.json";

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

    let popupHidden = false;
    let modalBind;

    function modalTryClose(e, force) {
        if (force || e.target === modalBind) {
            popupHidden = true;
        }
    }

    const formLink =
        "https://docs.google.com/forms/d/e/1FAIpQLScyywaWqPFLnGATcamhA_XGwfREfsu6qMkB5fx2LLUk9GRKOA/viewform?usp=share_link";
</script>

<svelte:head>
    <title>SMT 2023</title>
</svelte:head>

<svelte:window bind:innerWidth={windowWidth} on:click={(e) => modalTryClose(e, false)} />

<div bind:this={modalBind} class="popup" style="display: {popupHidden ? 'none' : 'auto'}">
    <div class="popup-content">
        <span class="close" on:click={(e) => modalTryClose(e, true)}>&times;</span>
        <Heading text="Important Information" size={2.5} />
        <PanelBox>
            <p><b>If you are participating in SMT 2023 Online on 4/9, please read the guide and join the discord server!</b></p>
            <HeaderButton
                text="Guide to SMT 2023 Online"
                href={"https://tinyurl.com/SMT2023OnlineGuide"}
                isSmall
                newTab
            />
            <br />
            <HeaderButton
                text="Discord Link (JOIN!)"
                href={"https://discord.gg/r9p65c6spP"}
                isSmall
                newTab
            />
        </PanelBox>
    </div>
</div>

<br><br>
<Heading text="Stanford Math Tournament 2023 Online" size={4} textColor="var(--heading-color)"/>
<Heading text="Overview" size={2.5} />
<div class="section-wrapper">
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
<div class="section-wrapper">
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
            <div class="buttons-wrapper">
            <HeaderButton class = "RegButtons"
                text="Eventbrite Payment"
                href={"https://tinyurl.com/SMT2023OnlineEventbrite"}
                isSmall
            />
            <br/><br/>
            <HeaderButton class = "RegButtons"
                text="ContestDojo"
                href={"https://contestdojo.com"}
                isSmall
            />
            </div>
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
        <strong>April 6, 2023:</strong> Late ($25/student) registration deadline
    </TimelineElement>
    <TimelineElement>
        <strong>April 7, 2023:</strong> Deadline for student waiver submission.
    </TimelineElement>
    <TimelineElement>
        <strong>April 9, 2023:</strong> SMT Online!!!
    </TimelineElement>
    <TimelineElement>
        <strong>April 16, 2023:</strong> SMT Online Award Ceremony
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
<style>
    .RegButtons {
        display: inline-flex;
        padding: 5px;
        margin: 5px;
    }

    .popup {
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgb(0,0,0);
        background-color: rgba(0,0,0,0.4);
    }

    .popup-content {
        background-color: var(--background-white);
        margin: 15% auto;
        padding: 20px;
        border: 1px solid var(--black-border);
        width: 80%;
        border-radius: 5px;
    }

    .close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
    }

    .close:hover,
    .close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
    }
</style>
