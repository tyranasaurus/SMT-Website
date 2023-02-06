<script>
    import PanelBox from "../PanelBox.svelte";

    export let timeText = "";
</script>

<div class="container">
    <div class="timeline-element">
        <PanelBox>
            <slot />
        </PanelBox>
    </div>
    <div id="timeline-dot">
        <div class="time-text">
            {timeText}
        </div>
    </div>
</div>

<style>
    .container {
        position: relative;
    }

    /* circle */
    #timeline-dot {
        content: "";
        position: absolute;
        width: 20px;
        height: 20px;
        right: -52px;
        background-color: var(--button-color);
        border: 5px solid white;
        top: 24px;
        border-radius: 50%;
        z-index: 1;
    }

    /* line */
    .timeline-element::after {
        content: "";
        width: 70px;
        height: 6px;
        background-color: white;
        right: -12px;
        top: 35px;
        position: absolute;
    }

    .timeline-element {
        width: auto;
        padding-right: 60px;
    }

    .time-text {
        position: absolute;
        left: 35px;
        top: -2px;
        vertical-align: middle;
        text-align: left;
        font-size: 1.3em;
        min-width: 100px;
    }
</style>
