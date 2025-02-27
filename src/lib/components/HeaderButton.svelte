<script>
    import { faCaretLeft, faCaretRight } from "@fortawesome/free-solid-svg-icons"
    import Fa from 'svelte-fa'

    export let text;
    export let icon = false;
    export let hasArrow = true;
    export let arrowDirection = "right";
    export let isSmall = false;
    export let isLink = true; // can be link or button
    export let href = "javascript:;";
    export let onClick = () => {};
    export let style = "";
    export let centered = false;
    export let newTab=false;

    let className = isSmall ? "smallerButton" : "headerButton";
    style = centered ? "margin-left: auto; margin-right: auto; {style}" : style;
    let target = newTab ? "_blank" : "_self";
</script>

{#if isLink}
    <div style={style}>
        <a sveltekit:prefetch {href} class={className} target={target}>
            <div class={className} on:click={onClick}>
                <p class={className}>
                    {#if icon} 
                        <i class={icon}></i>
                    {/if}
                    {text}
                </p>
                {#if hasArrow}
                    <Fa icon={arrowDirection == "right" ? faCaretRight : faCaretLeft} aria-hidden="true"/>
                {/if}
            </div>
        </a>
    </div>
{:else}
    <div class={className} on:click={onClick} style={style}>
        <p class={className}>
            {text}
        </p>
        {#if hasArrow}
            <Fa icon={arrowDirection == "right" ? faCaretRight : faCaretLeft} aria-hidden="true"/>
        {/if}
    </div>
{/if}

<style>
    div {
        display: flex;
        background-color: #981c1d;
        color: white;
        justify-content: center;
        align-items: center;
        width: 300px;
        flex-grow: 0;
        cursor: pointer;
    }

    div.headerButton {
        border-radius: 10px;
        padding: 10px;
    }

    div.smallerButton {
        border-radius: 5px;
        padding: 5px;
    }

    @media (max-width: 700px) {
        div.headerButton {
            margin: auto;
            width: 80%;
        }
    }

    p {
        color: white;
        align-self: center;
        font-size: 1em;
        margin: 5px;
        margin-right: 20px;
    }

    a {
        align-items: flex-start;
    }

    a:hover {
        text-decoration: none;
    }
</style>
