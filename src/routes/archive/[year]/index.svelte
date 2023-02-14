<script>
    import { page } from "$app/stores";
    import Heading from "$lib/components/Heading.svelte";
    import Link from "$lib/components/Link.svelte";
    import PanelBox from "$lib/components/PanelBox.svelte";
    import Table from "$lib/components/Table.svelte";

    const supportedYears = [2011, 2022];

    let year = $page.params.year;

    // check valid year
    let isYearSupported =
        year >= supportedYears[0] && year <= supportedYears[1];

    function getTableForYear(year, tb) {
        function getRow(round) {
            return [
                round,
                `/pdfs/smt${year}/${round.toLowerCase()}-problems.pdf`,
                `/pdfs/smt${year}/${round.toLowerCase()}-solutions.pdf`,
            ];
        }

        function getTBRow(round) {
            return [
                round,
                `/pdfs/smt${year}/${round.toLowerCase()}-tiebreaker-problems.pdf`,
                `/pdfs/smt${year}/${round.toLowerCase()}-tiebreaker-solutions.pdf`,
            ];
        }

        let rounds = {
            tests2022: [
                "Team",
                "Algebra",
                "Calculus",
                "Discrete",
                "Geometry",
                "General",
                "Guts",
                "Power",
            ],
            tb2022: ["Algebra", "Calculus", "Discrete", "Geometry", "General"],
            tests2021: [
                "Team",
                "Algebra",
                "Combo",
                "NT",
                "Geometry",
                "General",
                "Guts",
                "Power",
            ],
            tb2021: ["Algebra", "Combo", "NT", "Geometry", "General"],
            tests2020: [
                "Team",
                "Algebra",
                "Calculus",
                "Discrete",
                "Geometry",
                "General",
                "Guts",
                "Power",
            ],
            tb2020: ["Algebra", "Calculus", "Discrete", "Geometry", "General"],
            tests2019: [
                "Team",
                "Algebra",
                "Calculus",
                "Discrete",
                "Geometry",
                "General",
                "Power",
            ],
            tb2019: ["Algebra", "Calculus", "Discrete", "Geometry", "General"],
            tests2018: [
                "Team",
                "Algebra",
                "Calculus",
                "Discrete",
                "Geometry",
                "General",
                "Power",
            ],
            tb2018: ["Algebra", "Calculus", "Discrete", "Geometry", "General"],
            tests2014: [
                "Team",
                "Algebra",
                "Calculus",
                "Advanced",
                "Geometry",
                "General",
                "Power",
            ],
            tb2014: ["Algebra", "Calculus", "Advanced", "Geometry", "General"],
            tests2013: [
                "Team",
                "Algebra",
                "Calculus",
                "Advanced",
                "Geometry",
                "General",
                "Power",
            ],
            tb2013: ["Algebra", "Calculus", "Advanced", "Geometry", "General"],
            tests2012: [
                "Team",
                "Algebra",
                "Calculus",
                "Advanced",
                "Geometry",
                "General",
                "Power",
            ],
            tb2012: ["Algebra", "Calculus", "Advanced", "Geometry", "General"],
            tests2011: [
                "Team",
                "Algebra",
                "Calculus",
                "Advanced",
                "Geometry",
                "General",
                "Power",
            ],
            // arpit: continue filling it out in this format
        };

        if (tb) {
            return rounds["tb" + year]?.map((x) => getTBRow(x)) ?? [];
        } else {
            return rounds["tests" + year]?.map((x) => getRow(x)) ?? [];
        }
    }

    function getResults(year) {
        let resultLinks = {
            results2022: [
                {
                    text: "Results",
                    url: `/pdfs/smt2022/results.pdf`,
                },
                {
                    text: "International Results",
                    url: `/pdfs/smt2022/results-intl.pdf`,
                },
            ],
        };

        return resultLinks["results" + year] ?? [];
    }
</script>

{#if !isYearSupported}
    <h2 style="height: 100vh; margin-left: 10px;">
        This year is not yet supported. <Link url="/" text="Go back" />
    </h2>
{:else}
    <div style="min-height: 100vh;">
        <Heading size={5} text={year + " Archive"} textColor="black" />

        <div style="margin-left: 10vw; margin-right: 10vw;">
            <PanelBox>
                <div class="flex">
                    <!-- custom table -->
                    <div
                        style="margin-right: 30px; margin-bottom: 10px; min-height: 100%;"
                    >
                        <h3>Tests</h3>
                        <table>
                            {#each getTableForYear(year, false) as yearRow}
                                <tr>
                                    <td>{yearRow[0]}</td>
                                    <td
                                        ><Link
                                            url={yearRow[1]}
                                            text="Problems"
                                        /></td
                                    >
                                    <td
                                        ><Link
                                            url={yearRow[2]}
                                            text="Solutions"
                                        /></td
                                    >
                                </tr>
                            {/each}
                        </table>
                    </div>

                    {#if year !== 2011}
                        <div style="min-height: 100%; height: 100%;">
                            <h3>Tiebreakers</h3>
                            <table>
                                {#each getTableForYear(year, true) as yearRow}
                                    <tr>
                                        <td>{yearRow[0]}</td>
                                        <td
                                            ><Link
                                                url={yearRow[1]}
                                                text="Problems"
                                            /></td
                                        >
                                        <td
                                            ><Link
                                                url={yearRow[2]}
                                                text="Solutions"
                                            /></td
                                        >
                                    </tr>
                                {/each}
                            </table>
                        </div>
                    {/if}
                </div>

                <div class="flex" style="margin-top: 5px;">
                    <div style="margin-right: 30px">
                        <strong>Results:</strong>
                    </div>
                    {#each getResults(year) as resultLink}
                        <div style="margin-right: 20px">
                            <Link url={resultLink.url} text={resultLink.text} />
                        </div>
                    {/each}
                </div>
            </PanelBox>
        </div>
    </div>
{/if}

<style>
    table {
        border-collapse: collapse;
    }

    table,
    td,
    tr {
        border: 1px solid var(--black-border);
    }

    td {
        padding: 5px;
        min-width: 100px;
    }

    .flex {
        display: flex;
        flex-direction: row;
        align-items: stretch;
    }
</style>
