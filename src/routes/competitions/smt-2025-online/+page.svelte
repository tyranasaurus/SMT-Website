
<svelte:head>
    <title>More Information Coming Soon</title>
</svelte:head>

<div class="info-container">
    <h1 class="info-title">SMT 2025 Online Coming Soon</h1>
    <p class="info-description">Check back later for information with dates, format, and registration!</p>
</div>

<style>
    body {
        overflow: hidden;
    }
    .info-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 85vh;
        background-color: var(--primary-color);
        color: var(--text-color);
        text-align: center;
    }

    .info-title {
        font-size: 2.5em;
        font-weight: 600;
        margin-bottom: 20px;
    }

    .info-description {
        font-size: 1.5em;
        font-weight: 400;
        color: var(--paragraph-color);
    }
</style>
