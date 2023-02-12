<script>
    import Heading from "$lib/components/Heading.svelte";
    import Newsletter from "$lib/components/Newsletter.svelte";
    import { fly } from "svelte/transition";
    import { onMount } from "svelte";
    import Header from "$lib/header/Header.svelte";

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
            <Heading
                className="glow"
                text="Stanford Math Tournament"
                align="left"
                textColor="black"
                size={windowWidth > 700 ? 7 : 3}
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
    </div>
</div>
<div
    bind:this={infoElem}
    style="padding-bottom: 150px; padding-top:150px; padding-left: 40px"
>
    <div class="mobile-flex">
        <div style="margin-right: 50px;" class="infodiv">
            <Heading
                className="glow"
                text="Math Tournament?"
                align="left"
                textColor="black"
                size="3"
                marginLeft="0"
                padding="0"
                style="display: inline;"
            />
            <p class="other-text">
                Stanford Math Tournament is run entirely by Stanford students.
                We are one of the largest math competitions in the country with
                1200 participants in 2022. We are proudly supported by the
                Stanford Undergraduate Mathematics Organization (SUMO) and the
                Stanford Department of Mathematics.
            </p>
            <Heading
                className="glow"
                text="SMT?"
                align="left"
                textColor="black"
                size="3"
                marginLeft="0"
                padding="0"
                style="display: inline;"
            />
            <p class="other-text">SMT 2023 will be held April 8th, 2023.</p>
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
        <div style="margin-right: 30px; flex-direction: column">
            <img
                src="/sample-problem.png"
                alt="sample problem"
                width="100%"
                style="border: 1px solid var(--black-border); border-radius: 4px"
            />
            <div style="margin-top: 10px;">
                <a
                    sveltekit:prefetch
                    href="/archive/problems"
                    class="headerButton"
                >
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
            </div>
        </div>
    </div>
</div>
<div style="padding-bottom: 150px; margin-left: 40px">
    <Heading
        className="glow"
        text="Tournaments"
        align="left"
        textColor="black"
        size="3"
        marginLeft="0"
        padding="0"
        style="display: inline;"
    />
    <div class="mobile-flex" style="width: 100%">
        <div class="flex-item border-right tournament">
            <h2>SMT</h2>
            <p>Stuff about SMT goes here</p>
            <div style="margin-top: 10px;">
                <a
                    sveltekit:prefetch
                    href="/competitions/smt-2023"
                    class="smallerButton"
                >
                    <div
                        class="smallerButton"
                        on:mouseenter={toggleBackground}
                        on:mouseleave={toggleBackground}
                    >
                        <p class="smallerButton" id="signupforssmt">
                            Go to SMT 2023
                        </p>
                        <i class="fa fa-caret-right" aria-hidden="true" />
                    </div>
                </a>
            </div>
        </div>
        <div class="flex-item border-right tournament">
            <h2>SMT International</h2>
            <div style="margin-top: 10px;">
                <a
                    sveltekit:prefetch
                    href="/competitions/smt-2023-international"
                    class="smallerButton"
                >
                    <div
                        class="smallerButton"
                        on:mouseenter={toggleBackground}
                        on:mouseleave={toggleBackground}
                    >
                        <p class="smallerButton" id="signupforssmt">
                            Go to SMT 2023 International
                        </p>
                        <i class="fa fa-caret-right" aria-hidden="true" />
                    </div>
                </a>
            </div>
        </div>
        <div class="flex-item tournament">
            <h2>SMT Online</h2>
            <div style="margin-top: 10px;">
                <a
                    sveltekit:prefetch
                    href="/competitions/smt-2023-online"
                    class="smallerButton"
                >
                    <div
                        class="smallerButton"
                        on:mouseenter={toggleBackground}
                        on:mouseleave={toggleBackground}
                    >
                        <p class="smallerButton" id="signupforssmt">
                            Go to SMT 2023 Online
                        </p>
                        <i class="fa fa-caret-right" aria-hidden="true" />
                    </div>
                </a>
            </div>
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

    .other-text {
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

    div.smallerButton {
        display: flex;
        background-color: #981c1d;
        border-radius: 5px;
        padding: 5px;
        color: white;
        justify-content: center;
        align-items: center;
        width: 300px;
        flex-grow: 0;
    }

    .mobile-flex {
        display: flex;
        flex-direction: row;
    }

    .infodiv {
        max-width: 50%;
    }

    .flex-item {
        width: 100%;
    }

    .border-right {
        border-right: 1px solid var(--black-border);
    }

    .tournament {
        padding-left: 10px;
        padding-right: 10px;
        height: 100%;
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

        .mobile-flex {
            display: flex;
            flex-direction: column;
        }

        .infodiv {
            max-width: unset;
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

    p.headerButton,
    p.smallerButton {
        color: white;
        align-self: center;
        font-size: 1em;
        margin: 5px;
        margin-right: 20px;
    }

    a.headerButton,
    a.smallerButton {
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
