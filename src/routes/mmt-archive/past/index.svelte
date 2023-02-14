<script>
    import Heading from '$lib/components/Heading.svelte';
    import Dropdown from '$lib/components/Dropdown.svelte';
    import PanelBox from '$lib/components/PanelBox.svelte';
    import Link from '$lib/components/Link.svelte';
    import Button from '$lib/components/Button.svelte';
    import PageHeader from '$lib/components/PageHeader.svelte';

    const competitions = [
        {
            title: "Mustang Math Tournament 2022 (MMT)",
            location: "mmt-2022"
        },
        {
            title: "Mustang Mini Math Tournament 2022 (3MT)",
            location: "3mt-2022"
        }
    ];
    // A value of false represents that the ith button is unfilled
    let buttonStates = Array(competitions.length).fill(false);

    function toggleArrow(i) {
        buttonStates[i] = !buttonStates[i];
    }
</script>

<svelte:head>
	<title>Competitions</title>
</svelte:head>

<PageHeader title="Past Competitions" description="Check Out Our Upcoming Competitions" button_url="https://contestdojo.com/" button_text="Register on ContestDojo!" button_id="registerOnContestDojo"/>
<section style="padding: 30px;">
    {#each competitions as competition, i}
    <PanelBox>
        <div on:mouseenter={() => toggleArrow(i)} on:mouseleave={() => toggleArrow(i)}>
            <a class="headerButton" href="/competitions/past/{competition.location}">
                <p class="headerButton" id={competition.location}>{competition.title}</p>
                <img height="40px" class="headerButton" src={buttonStates[i] ? "/right-arrow-shaded.png" : "/right-arrow.png"} alt="Right-facing arrow icon" />
            </a>
        </div>
    </PanelBox>
    {/each}
</section>

<style>
    .headerButton {
        display: flex;
        padding: 10px;
        margin: auto;
        justify-content: center;
        align-items: center;
    }

    p.headerButton {
        align-self: center;
        margin: 5px;
        margin-right: 20px;
        font-weight: 700;
    }

    .headerButton:hover {
        text-decoration: none;
    }
</style>
