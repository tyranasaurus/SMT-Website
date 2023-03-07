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
    <br><br>
    <!-- hide footer because we don't have socials? TODO: add socials -->
    {#if $page.url.pathname !== "/"}
        <footer>
            <div class="socials">
                <SocialsLink url="mailto:stanford.math.tournament@gmail.com" type="solid" icon="envelope" />
                <SocialsLink url="https://www.facebook.com/StanfordMathTournament" type="brands" icon="facebook" />
			    <SocialsLink url="https://www.instagram.com/StanfordMathTournament/" type="brands" icon="instagram" />
            </div>
        </footer>
    {/if}
</div>

<style>
    .socials {
        color: white
    }
    .divider {
		width: 2px;
		background-color: white;
		height: 50px;
		margin-left: 10px;
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
        min-height: 52px;
        background-color: var(--background-dark);
    }

    .socials {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        font-size: 1em;
        padding-top: 10px;
        padding-bottom: 8px;
        color: lightgray;
    }
</style>