<script>
    import Heading from "$lib/components/Heading.svelte";
    import Newsletter from "$lib/components/Newsletter.svelte";
    import { fly } from "svelte/transition";
    import { onMount } from "svelte";

    // need to do this to make the animation play on page load
    let visible = false;
    let windowWidth;
    let background = "right-arrow.png";
    let scrollOpacity = 1;

    let show = false;

    onMount(() => {
        visible = true;
    });

    function toggleBackground() {
        if (background == "right-arrow.png") {
            background = "right-arrow-shaded.png";
        } else {
            background = "right-arrow.png";
        }
    }

    let y;

    let windowHeight;
    let learnMoreIsVisible = true;
    $: scrollOpacity = Math.max((windowHeight - 2 * y) / windowHeight, 0);
    $: learnMoreIsVisible = scrollOpacity > 0;

    let infoElem;
    function scrollToInfo() {
        infoElem.scrollIntoView({
            behavior: "smooth",
        });
    }
</script>

<svelte:window
    bind:scrollY={y}
    bind:innerWidth={windowWidth}
    bind:innerHeight={windowHeight}
/>

<svelte:head>
    <title>Stanford Math Tournament</title>
</svelte:head>

<div class="outside" style="height: 100vh;">
    <div class="header flex">
        <div class="minidiv">
            {#if windowWidth > 700}
                <Heading
                    className="glow"
                    text="Stanford Math Tournament"
                    align="left"
                    textColor="black"
                    size="6"
                    marginLeft="0"
                    padding="0"
                />
            {:else}
                <Heading
                    className="glow"
                    text="SMT"
                    textColor="black"
                    size="5"
                />
            {/if}
            <p class="descript">
                The Stanford Math Tournament (SMT) is a high school math
                tournament run by students at Stanford University. We are
                passionate about providing a high quality and challenging event
                to students interested in mathematics globally.
            </p>
            <a
                sveltekit:prefetch
                href="/competitions/smt-2023"
                class="headerButton"
            >
                <div
                    class="headerButton"
                    on:mouseenter={toggleBackground}
                    on:mouseleave={toggleBackground}
                >
                    <p class="headerButton" id="signupforsmt">
                        Register for SMT 2023!
                    </p>
                    <i class="fa fa-caret-right" aria-hidden="true" />
                </div>
            </a>
            <br />
            <!--<button class="sign-up" on:click={() => {show = !show;}}><i class="fa-regular fa-newspaper"></i> Sign Up for our Newsletter</button>-->
        </div>
    </div>
</div>
<div
    bind:this={infoElem}
    class="outside"
    style="height: 90vh; padding-left: 10vh"
>
    <div class="header flex">
        <div class="minidiv" style="width: 400vh">
            <Heading
                className="glow"
                text="Math Tournament?"
                align="left"
                textColor="black"
                size="3"
                marginLeft="0"
                padding="0"
            />
            <p class="descript">
                The Stanford Math Tournament (SMT) is a high school math
                tournament run by students at Stanford University. We are
                passionate about providing a high quality and challenging event
                to students interested in mathematics globally.
            </p>
            <Heading
                className="glow"
                text="SMT?"
                align="left"
                textColor="black"
                size="3"
                marginLeft="0"
                padding="0"
            />
            <p class="descript">
                The Stanford Math Tournament (SMT) is a high school math
                tournament run by students at Stanford University. We are
                passionate about providing a high quality and challenging event
                to students interested in mathematics globally.
            </p>
            <a
                sveltekit:prefetch
                href="/competitions/smt-2023"
                class="headerButton"
            >
                <div
                    class="headerButton"
                    on:mouseenter={toggleBackground}
                    on:mouseleave={toggleBackground}
                >
                    <p class="headerButton" id="signupforsmt">
                        Register for SMT 2023!
                    </p>
                    <i class="fa fa-caret-right" aria-hidden="true" />
                </div>
            </a>
            <br />
            <!--<button class="sign-up" on:click={() => {show = !show;}}><i class="fa-regular fa-newspaper"></i> Sign Up for our Newsletter</button>-->
        </div>
        <div class="minidiv" style="margin-left: -30vh">
            <img src="/sampleproblem.png" alt="sample problem" />
            <a sveltekit:prefetch href="/resources" class="headerButton">
                <div
                    class="headerButton"
                    on:mouseenter={toggleBackground}
                    on:mouseleave={toggleBackground}
                >
                    <p class="headerButton" id="signupforssmt">
                        See More Past Problems
                    </p>
                    <i class="fa fa-caret-right" aria-hidden="true" />
                </div>
            </a>
            <br />
        </div>
    </div>
</div>
<div
    class="scroll-notification"
    style="opacity: {scrollOpacity}; display: {learnMoreIsVisible
        ? ''
        : 'none'} "
    on:click={scrollToInfo}
>
    Learn more &nbsp;
    <i class="fa fa-caret-down" style="margin-left: 2px;" />
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

    div.headerButton,
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

        div.headerButton {
            margin: auto;
            width: 80%;
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

    p.headerButton {
        color: white;
        align-self: center;
        font-size: 1em;
        margin: 5px;
        margin-right: 20px;
    }

    a.headerButton {
        align-items: flex-start;
    }

    a.headerButton:hover {
        text-decoration: none;
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
</style>
