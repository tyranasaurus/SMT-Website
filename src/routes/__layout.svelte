<script>
    import Header from "$lib/header/Header.svelte";
    import SocialsLink from "$lib/components/SocialsLink.svelte";
    import "../app.css";
    import { page } from "$app/stores";
    import Newsletter from "$lib/components/Newsletter.svelte";

    let show = false;
</script>

<div class="all-container">
    <Header />

    <main>
        <slot />
        <Newsletter {show} />
    </main>

    <!-- hide footer because we don't have socials? TODO: add socials -->
    {#if $page.url.pathname !== "/"}
        <footer>
            <div class="socials">
                <button
                    class="sign-up"
                    on:click={() => {
                        show = !show;
                    }}><i class="fa-regular fa-newspaper" /> Signup</button
                >
                <div class="divider" />
                <SocialsLink
                    url="mailto:contact@mustangmath.com"
                    type="solid"
                    icon="envelope"
                />
                <SocialsLink
                    url="https://discord.gg/bYDDWxan5d"
                    type="brands"
                    icon="discord"
                />
                <SocialsLink
                    url="https://www.facebook.com/MustangMath"
                    type="brands"
                    icon="facebook"
                />
                <SocialsLink
                    url="https://www.instagram.com/mustangmath/"
                    type="brands"
                    icon="instagram"
                />
                <SocialsLink
                    url="https://www.linkedin.com/company/mustangmathtournament/"
                    type="brands"
                    icon="linkedin"
                />
                <SocialsLink
                    url="https://www.youtube.com/channel/UCCCk-s3dHatOKfwiC5yJBAA"
                    type="brands"
                    icon="youtube"
                />
                <SocialsLink
                    url="https://artofproblemsolving.com/wiki/index.php/Mustang_Math_Tournament"
                    type="text"
                    icon="AoPS"
                    text
                />
            </div>
        </footer>
    {/if}
</div>

<style>
    .divider {
        width: 2px;
        background-color: white;
        height: 50px;
        margin-left: 10px;
    }

    @media screen and (max-width: 900px) {
        .divider {
            margin-right: 5px;
        }
    }

    main {
        flex: 1;
        display: flex;
        flex-direction: column;
        width: 100%;
        margin: 0 auto;
        box-sizing: border-box;
    }

    .all-container {
        position: relative;
        min-height: 100vh;
        box-sizing: border-box;
    }

    footer {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        bottom: 0;
        width: 100%;
        text-align: center;
        position: sticky;
        z-index: 2;
        min-height: 50px;
        background-color: var(--background-dark);
    }

    .socials {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        padding-top: 10px;
        padding-bottom: 8px;
    }
</style>
