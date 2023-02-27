<script>
    import Heading from "$lib/components/Heading.svelte";
    import Newsletter from "$lib/components/Newsletter.svelte";
    import { fly } from "svelte/transition";
    import { onMount } from "svelte";
    import Header from "$lib/header/Header.svelte";
    import HeaderButton from "$lib/components/HeaderButton.svelte";
    import PageHeader from "$lib/components/PageHeader.svelte";

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
    let tournElem;

    function scrollToElem(e) {
        e.scrollIntoView({
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

<div class="outside" style="height: calc(max(600px, 100vh));">
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
            <HeaderButton
                text="Register for SMT 2023!"
                arrowDirection="down"
                onClick={() => scrollToElem(tournElem)}
                isLink={false}
            />
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
                text="What is SMT?"
                align="left"
                textColor="black"
                size="3"
                marginLeft="0"
                padding="0"
                style="display: inline;"
            />
            <p class="other-text">
                Stanford Math Tournament is run entirely by Stanford students.
                We are one of the largest math competitions in the country with over
                1200 participants globally in 2022. We are proudly supported by the
                Stanford Undergraduate Mathematics Organization (SUMO) and the
                Stanford Department of Mathematics.
            </p>
            <!--
            <p class="other-text">SMT 2023 will be held April 8th, 2023.</p>
            <HeaderButton
                text="Register for SMT 2023!"
                arrowDirection="down"
                onClick={() => scrollToElem(tournElem)}
                isLink={false}
            />
            <br />
            -->
            <!--<button class="sign-up" on:click={() => {show = !show;}}><i class="fa-regular fa-newspaper"></i> Sign Up for our Newsletter</button>-->
        </div>
        <div style="margin-right: 30px; flex-direction: column">
            <img
                src="/sample-problem.png"
                alt="sample problem"
                width="100%"
                style="border: 1px solid var(--black-border); border-radius: 4px"
            />
            <div style="margin-top: 10px; margin-left: 10px;">
                <HeaderButton
                    href="/archive/problems"
                    text="See More Past Problems"
                />
            </div>
        </div>
    </div>
</div>
<div
    bind:this={tournElem}
    style="padding-bottom: 150px; margin-left: 40px; padding-top: 20px;"
>
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
            <p>The Stanford Math Tournament (SMT) is a contest organized by Stanford students, held on Stanford’s campus. In 2023, SMT will be held on <b>April 8, 2023</b>, and will be open via application to 250 high school contestants from within the United States. </p>
            <div style="margin-top: 10px;">
                <HeaderButton
                    href="/competitions/smt-2023"
                    text="Go to SMT 2023"
                    isSmall={true}
                />
            </div>
        </div>
        <div class="flex-item border-right tournament">
            <h2>SMT Online</h2>
            <p>In support of our mission to spread mathematics education and improve the accessibility of math tournaments, we are hosting a concurrent online tournament, identical to SMT. It will occur on <b>April 9, 2023</b> and is open to all middle and high school students from <b>anywhere in the world</b>.</p>
            <div style="margin-top: 10px;">
                <HeaderButton
                    href="/competitions/smt-2023-online"
                    text="Go to SMT 2023 Online"
                    isSmall={true}
                />
            </div>
        </div>
        <div class="flex-item tournament">
            <h2>SMT Asynchronous</h2>
            <p>For students unable to participate in SMT in-person or Online, we are offering SMT Asynchronous - a week long period where you can experience the SMT tests on your own or in a team at your own leisure.</p>
            <div style="margin-top: 10px;">
                <HeaderButton
                    href="/competitions/smt-2023-async"
                    text="Go to SMT 2023 Asynchronous"
                    isSmall={true}
                />
            </div>
        </div>
        
    </div>
</div>
<div
    class="scroll-notification"
    style="opacity: {scrollOpacity}; display: {learnMoreIsVisible
        ? ''
        : 'none'} "
    on:click={() => scrollToElem(infoElem)}
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
        padding-left: 20px;
        padding-right: 20px;
        padding-bottom: 5px;
        min-height: 100%;
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
