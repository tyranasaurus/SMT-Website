<script context="module">
    export const prerender = true;
</script>

<script>
    import FlexBox from "$lib/components/FlexBox.svelte";
    import Person from "$lib/components/Person.svelte";
    import PageHeader from "$lib/components/PageHeader.svelte";
    import Alumni from "$lib/components/Alumni.svelte";
    import Members from "$lib/Members.json";
    import Heading from "$lib/components/Heading.svelte"
    let windowWidth;
</script>

<svelte:head>
    <title>Our Team</title>
</svelte:head>

<svelte:window bind:innerWidth={windowWidth} />
<br>
<br>
<Heading text="Our Team" size={4} textColor="var(--heading-color)"/>
<section>
    <FlexBox wrap={true}>
        {#each Members as Member}
            <Person
                width="21em"
                pic={Member.primary}
                name={Member.fullName}
                grade={Member.grade}
            />
        {/each}
    </FlexBox>
</section>

<style>
</style>