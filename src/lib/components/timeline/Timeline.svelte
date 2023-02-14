<script>
    import { onMount } from "svelte";

    export let width = "75%";
    let timelineElem;
    let updatedHeight = 0;

    onMount(() => {
        updatedHeight = getLastElementHeight();
    });

    // corrected for the timeline position
    function getLastElementHeight() {
        // get last element
        const height =
            timelineElem?.lastChild?.previousElementSibling?.offsetHeight;
        if (!height) return 0;
        return height - 27;
    }
</script>

<div class="timeline-outer" style="width: {width}">
    <div class="timeline-container">
        <div
            class="timeline"
            bind:this={timelineElem}
            style="--child-height: {updatedHeight}px"
        >
            <slot />
        </div>
    </div>
</div>

<style>
    /* warning: lots of hardcoded values */

    .timeline-outer {
        align-items: center;
        margin: auto;
    }

    .timeline-container {
        position: relative;
    }

    .timeline::before {
        content: "";
        position: absolute;
        top: 28px;
        bottom: var(--child-height);
        right: -40px;
        width: 6px;
        background-color: white;
        display: inline-block;
    }
</style>
