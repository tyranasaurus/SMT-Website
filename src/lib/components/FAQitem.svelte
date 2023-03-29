<script>
    export let question;
    export let answer;

    import Text from '$lib/components/Text.svelte';
    import Heading from '$lib/components/Heading.svelte';
    import PanelBox from '$lib/components/PanelBox.svelte';
</script>

<PanelBox width="40em" align-items="left">
    <div class="faq-item-flex">
        <p class="faq-text"><span class="faq-label">Q: </span>{question}</p>
        <p class="faq-text"><span class="faq-label">A: </span>{answer}</p>
    </div>
</PanelBox>


<style>
    .faq-text{
    color: black;
    font-size: 1em;
    font-weight: 400;
    }
    .faq-item-flex{
        display: block;
        width: 100%;
        height: fit-content;
        flex-basis: 0;
        flex-grow: 1;
        align-items: left;
        justify-content: center;
        padding-left: 5px;
        text-align: left;
    }
    .faq-label{
        color: "var(--heading-color)";
        font-weight: 600;
    }
</style>
