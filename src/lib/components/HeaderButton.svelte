<script>
    export let text;
    export let hasArrow = true;
    export let arrowDirection = "right";
    export let isSmall = false;
    export let isLink = true; // can be link or button
    export let href = "javascript:;";
    export let onClick = () => {};

    let className = isSmall ? "smallerButton" : "headerButton";
</script>

{#if isLink}
    <div>
        <a sveltekit:prefetch {href} class={className}>
            <div class={className} on:click={onClick}>
                <p class={className}>
                    {text}
                </p>
                {#if hasArrow}
                    <i
                        class="fa fa-caret-{arrowDirection}"
                        aria-hidden="true"
                    />
                {/if}
            </div>
        </a>
    </div>
{:else}
    <div class={className} on:click={onClick}>
        <p class={className}>
            {text}
        </p>
        {#if hasArrow}
            <i class="fa fa-caret-{arrowDirection}" aria-hidden="true" />
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
