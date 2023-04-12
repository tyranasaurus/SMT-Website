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
    import Questions from "$lib/FAQ-smt-2023-async.json";

    let windowWidth;
    const scheduleData = [
        {
            Time: "5:00 AM-5:30 AM",
            Event: "Opening Ceremony",
        },
        ["5:30 AM-7:30 AM", "Individual Round(s)"],
        ["7:30 AM-8:30 AM", "Lunch Break (60 min)"],
        ["8:30 AM-9:30 AM", "Team Round (50 min)"],
        ["9:30 AM-11:00 AM", "Guts Round (80 min)"],
    ];

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

<svelte:window bind:innerWidth={windowWidth} />

<div bind:this={modalBind} class="popup" style="display: {popupHidden ? 'none' : 'auto'}">
    <div class="popup-content">
        <span class="close" on:click={(e) => modalTryClose(e, true)}>&times;</span>
        <Heading text="Registration Open!" size={2.5} />
        <PanelBox>
            <p><b>Regsistration for SMT Async is open on ContestDojo!</b></p>
            <HeaderButton
                text="Register Now!"
                href={"https://contestdojo.com"}
                isSmall
                newTab
            />
        </PanelBox>
    </div>
</div>

<br><br>
<Heading text="Stanford Math Tournament 2023 Asynchronous" size={4} textColor="var(--heading-color)"/>
<Heading text="Overview" size={2.5} />
<div class="section-wrapper">
    <PanelBox>
        <div style="padding: 10px;">
            <p>
                <strong>DATE:</strong> April 12 until April 16 <br />
                <strong>LOCATION:</strong> Online <br />
                <strong>WHO:</strong> Any student anywhere.<br />
                <strong>TEAM SIZE:</strong> Up to 8 <br />
                <strong>COST:</strong> $5 per participant<br /> <br />
            </p>
            <strong>Note for International Students:</strong> We are no longer offering SMT International this year. International students may participate in SMT Online, or if the timing is bad for them, SMT Asynchronous.
            <p><b>Regsistration for SMT Async is open on ContestDojo!</b></p>
            <HeaderButton
                text="Register Now!"
                href={"https://contestdojo.com"}
                isSmall
                newTab
            />
        </div>
    </PanelBox>
</div>
<br />

<Heading text="Contest Information" size={2.5} />
<div class="section-wrapper">
    <PanelBox>
        <div style="padding: 10px;">
            <p>There are no awards or official rankings for SMT Asynchronous, but you will receive a certificate of participation, as well as score reports the give you general statistics and let you know how you compare to all participants in SMT 2023 (in-person, online, asynchronous).</p>
            <p>SMT Asynchronous may take placeanywhere or anytime during the testing window - you can make it an entire-day affair, or you can split the tests up across multiple days.</p>
            <p>For the team rounds (team and guts) you can form teams of up to 8, during which you all can work together on the test, and your answers will sync in ContestDojo. <b>One student starting the test will start it for the entire team!</b></p>
        </div>
    </PanelBox>
</div>
<!--
<Heading text="Registration Timeline" size={2.5} />

<Timeline width="60%">
    <TimelineElement>
        <strong>Monday, February 20, 2023:</strong> SMT Asyncronous Registration opens
    </TimelineElement>
    <TimelineElement>
        <strong>Wednesday, March 15, 2023 at 11:59 PM PT:</strong> Early Bird ($10/student) registration deadline
    </TimelineElement>
    <TimelineElement>
        <strong>Wednesday, April 5, 2023:</strong> Regular ($15/student) registration deadline
    </TimelineElement>
    <TimelineElement>
        <strong>Saturday, April 8, 2023:</strong> Deadline for student waiver submission.
    </TimelineElement>
    <TimelineElement>
        <strong>Thursday, April 13, 2023:</strong> Late ($25/student) registration deadline
    </TimelineElement>
    <TimelineElement>
        <strong>Sunday, April 10-16, 2023:</strong> SMT Asyncronous
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
                overallHeader="Tournament Schedule (5:00 AM-11:00 AM UTC)"
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
-->
<Heading text="Test Information" size={2.5} />

<div class="section-wrapper">
    <PanelBox>
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
