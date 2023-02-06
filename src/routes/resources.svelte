<script>
  import Heading from "$lib/components/Heading.svelte";
  import DropdownArchive from "$lib/components/DropdownArchive.svelte";
  import Text from "$lib/components/Text.svelte";
  import Link from "$lib/components/Link.svelte";
  import Button from "$lib/components/Button.svelte";
  import PanelBox from "$lib/components/PanelBox.svelte";
  import PageHeader from "$lib/components/PageHeader.svelte";
  import { onMount } from "svelte";

  let windowWidth;

  let handoutData = [
    [["Quadratics", "archive/handouts/Algebra/Quadratics.pdf"]],
    [],
    [],
    [
      ["Factors", "archive/handouts/Number Theory/Factors.pdf"],
      ["LCM & GCD", "archive/handouts/Number Theory/LCM&GCD.pdf"],
    ],
  ];

  let problems = "Problems";
  let answers = "Answers";
  let solutions = "Solutions";

  onMount(() => {
    if (windowWidth < 700) {
      problems = "Probl.";
      answers = "Ans.";
      solutions = "Soln.";
    }
  });
</script>

<svelte:head>
  <title>Study Resources</title>
</svelte:head>
<svelte:window bind:innerWidth={windowWidth} />

<PageHeader
  title="Resources"
  description="Study for upcoming tournaments or classes with these resources!"
  button_url="/classes"
  button_text="Learn more with our classes!"
  button_id="trainingPortal"
/>

<section>
  <Heading text="Topic-Based Handouts" size={2.5} />
  <div style="margin-left: 10vw; margin-right: 10vw;">
    <PanelBox>
      <table>
        <tr>
          <th>Algebra</th>
          {#each handoutData[0] as handout}
            <td
              ><a target="_blank" sveltekit:prefetch href={handout[1]}
                >{handout[0]}</a
              ></td
            >
          {/each}
        </tr>
        <tr>
          <th>{windowWidth < 700 ? "Combo" : "Combinatorics"}</th>
          {#each handoutData[1] as handout}
            <td
              ><a target="_blank" sveltekit:prefetch href={handout[1]}
                >{handout[0]}</a
              ></td
            >
          {/each}
        </tr>
        <tr>
          <th>{windowWidth < 700 ? "Geo" : "Geometry"}</th>
          {#each handoutData[2] as handout}
            <td
              ><a target="_blank" sveltekit:prefetch href={handout[1]}
                >{handout[0]}</a
              ></td
            >
          {/each}
        </tr>
        <tr>
          <th>{windowWidth < 700 ? "NT" : "Number Theory"}</th>
          {#each handoutData[3] as handout}
            <td
              ><a target="_blank" sveltekit:prefetch href={handout[1]}
                >{handout[0]}</a
              ></td
            >
          {/each}
        </tr>
      </table>
    </PanelBox>
  </div>
</section>

<section>
  <Heading text="Youtube Videos" size={2.5} />
  <div style="margin-left: 10vw; margin-right: 10vw;">
    <PanelBox>
      <p style="font-size: 1.5em; text-align: center;">
        Check out our first solution video!<br />
      </p>
      <p align="center">
        <iframe
          align="center"
          title="MMT 2022 Solutions Video"
          width="100%"
          height="450"
          style="text-align: center"
          src="https://www.youtube.com/embed/pl17fwL8dE0?start=1"
        />
      </p>
    </PanelBox>
  </div>
</section>

<section>
  <Heading text="Past Exams" size={2.5} />
  <DropdownArchive
    id="showDropdown"
    year="2022"
    tests={[
      [
        ["Mounting Mayhem"],
        ["Rules", "archive/2022/MountingMayhemRules.pdf"],
        ["Puzzles", "https://tinyurl.com/MMT2022MountingMayhemPuzzles"],
        [solutions, "https://tinyurl.com/MM2022MountingMayhemAnswers"],
      ],
      [
        ["Bucking Bingo"],
        [problems, "archive/2022/BuckingBingoProblems.pdf"],
        [answers, "archive/2022/BuckingBingoAnswers.pdf"],
        [solutions, "archive/2022/BuckingBingoSolutions.pdf"],
      ],
      [
        ["Gallop"],
        [problems, "archive/2022/GallopProblems.pdf"],
        [answers, "archive/2022/GallopAnswers.pdf"],
        [solutions, "archive/2022/GallopSolutions.pdf"],
      ],
      [
        ["Pressure Round 1 (Mystery Mare)"],
        [problems, "archive/2022/Pressure1Problems.pdf"],
        [answers, "archive/2022/Pressure1Answers.pdf"],
        [solutions, "archive/2022/Pressure1Solutions.pdf"],
      ],
      [
        ["Pressure Round 2 (Mystery Mare)"],
        [problems, "archive/2022/Pressure2Problems.pdf"],
        [answers, "archive/2022/Pressure2Answers.pdf"],
        [solutions, "archive/2022/Pressure2Solutions.pdf"],
      ],
    ]}
  />
  <DropdownArchive
    id="showDropdown"
    year="2021"
    tests={[
      [["Mounting Mayhem"], [problems, "archive/2021/MountingMayhem.pdf"]],
      [["Bucking Bingo"], [problems, "archive/2021/BuckingBingo.pdf"]],
      [
        ["Relay Rodeo (Mystery Mare)"],
        [problems, "archive/2021/Relay Rodeo.pdf"],
      ],
      [["Gallop Round 1"], [problems, "archive/2021/Gallop Set 1.pdf"]],
      [["Gallop Round 2"], [problems, "archive/2021/Gallop Set 2.pdf"]],
      [["Gallop Round 3"], [problems, "archive/2021/Gallop Set 3.pdf"]],
      [["Gallop Round 4"], [problems, "archive/2021/Gallop Set 4.pdf"]],
      [["Gallop Round 5"], [problems, "archive/2021/Gallop Set 5.pdf"]],
      [["Gallop Round 6"], [problems, "archive/2021/Gallop Set 6.pdf"]],
      [["Gallop Round 7"], [problems, "archive/2021/Gallop Set 7.pdf"]],
      [["Gallop Round 8"], [problems, "archive/2021/Gallop Set 8.pdf"]],
      [
        [answers, "archive/2021/Answers.pdf"],
        ["Results", "archive/2021/Results.pdf"],
      ],
    ]}
  />
  <DropdownArchive
    id="showDropdown"
    year="2020"
    tests={[
      [["Mounting Mayhem"], [problems, "archive/2020/MountingMayhem.pdf"]],
      [
        ["Unbridled Approximation"],
        [problems, "archive/2020/UnbridledApproximation.pdf"],
      ],
      [["Gallop Round 1"], [problems, "archive/2020/Gallop Set 1.pdf"]],
      [["Gallop Round 2"], [problems, "archive/2020/Gallop Set 2.pdf"]],
      [["Gallop Round 3"], [problems, "archive/2020/Gallop Set 3.pdf"]],
      [["Gallop Round 4"], [problems, "archive/2020/Gallop Set 4.pdf"]],
      [["Gallop Round 5"], [problems, "archive/2020/Gallop Set 5.pdf"]],
      [["Gallop Round 6"], [problems, "archive/2020/Gallop Set 6.pdf"]],
      [["Gallop Round 7"], [problems, "archive/2020/Gallop Set 7.pdf"]],
      [["Gallop Round 8"], [problems, "archive/2020/Gallop Set 8.pdf"]],
      [
        [answers, "archive/2020/Answers.pdf"],
        ["Results", "archive/2020/Results.pdf"],
      ],
    ]}
  />
</section>

<style>
  section {
    padding: 10px;
  }
  iframe {
    display: block;
    max-width: 800px;
  }
  table {
    text-align: left;
    border-spacing: 1em;
  }
</style>
