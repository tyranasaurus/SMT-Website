<script>
  import Heading from '$lib/components/Heading.svelte'
  import Dropdown from '$lib/components/Dropdown.svelte'
  import Link from '$lib/components/Link.svelte'
  import Button from '$lib/components/Button.svelte'
  import PageHeader from '$lib/components/PageHeader.svelte'
  import Competition from '$lib/components/Competition.svelte'
  import FlexBox from '$lib/components/FlexBox.svelte'
  import Table from '$lib/components/Table.svelte'
  import PanelBox from '$lib/components/PanelBox.svelte'
  import Image from '$lib/components/Image.svelte'
  let windowWidth
  let scheduleData = [
    { 'Time (PT)': '9:00 AM - 9:30 AM', Event: 'Opening Ceremony' },
    { Time: '9:30 AM - 10:55 AM', Event: 'Round 1: Mounting Mayhem' },
    { Time: '10:55 AM - 12:05 PM', Event: 'Round 2: Bucking Bingo' },
    { Time: '12:05 PM - 1:00 PM', Event: 'Lunch Break' },
    { Time: '1:00 PM - 2:10 PM', Event: 'Round 3: Gallop' },
    { Time: '2:10 PM - 3:00 PM', Event: 'Round 4: Mystery Mare' },
    { Time: '3:00 PM - 4:00 PM', Event: 'Activities (Optional)' },
    { Time: '4:00 PM - 4:30 PM', Event: 'Awards Ceremony' },
  ]
  let topicsCovered = [
    {
      Algebra:
        '<ul><li>Systems of equations</li> <li>Quadratics</li> <li>Vieta’s</li> <li>Binomial Theorem</li> <li>Radicals/Exponents</li> <li>Simon’s Favorite Factoring Trick</li> <li>Ratios</li> <li>(Infinite) Geometric Series</li> <li>Arithmetic Series</li> <li>Sum/Difference of Powers</li> <li>Rate/Time</li> <li>Floor/Ceiling</li> <li>Absolute Value</li> <li>Substitution (Nested Roots/Repeated Fractions)</li> <li>Mean, Median, Mode, Range</li> <li>Telescoping</li></ul>',
      Combinatorics:
        '<ul><li>Sticks and Stones</li> <li>Permutation/Combination</li> <li>Properties of Inclusion Exclusion for three or less sets</li> <li>Basic Geometric Probability</li> <li>Conditional Probability</li> <li>Expected Values</li> <li>Complementary Counting</li> <li>Recursion</li> <li>Bijections</li> <li>Casework</li> <li>Pigeonhole Principle</li> <li>Double-counting</li> <li>Basic Invariants</li></ul>',
      Geometry:
        '<ul><li>Area Formulas</li> <li>Volume Formulas</li> <li>Shoelace Formula</li> <li>Pythagorean Theorem</li> <li>Distance Formula</li> <li>Similar Triangles</li> <li>Angle Chasing</li> <li>Power of a Point</li> <li>Basic Mass Points</li> <li>Heron’s Formula</li> <li>Pick’s Theorem</li> <li>Surface Area for Pyramids, Prisms, and Cones</li> <li>Arcs and Sectors</li> <li>Angle Bisector Theorem</li> <li>Internal/External Angles</li></ul>',
      'Number Theory':
        '<ul><li>Fermat’s Little Theorem</li> <li>Euclidean Algorithm</li> <li>Chinese Remainder Theorem</li> <li>Divisibility</li> <li>Chicken McNugget Theorem</li> <li>GCD and LCM</li> <li>Number of Factors</li> <li>Sum of Factors</li> <li>Basic Modular Arithmetic</li> <li>Fundamental Theorem of Arithmetic</li></ul>',
    },
  ]
  let topicsSmall1 = [
    {
      Algebra:
        '<ul><li>Systems of equations</li> <li>Quadratics</li> <li>Vieta’s</li> <li>Binomial Theorem</li> <li>Radicals/Exponents</li> <li>Simon’s Favorite Factoring Trick</li> <li>Ratios</li> <li>(Infinite) Geometric Series</li> <li>Arithmetic Series</li> <li>Sum/Difference of Powers</li> <li>Rate/Time</li> <li>Floor/Ceiling</li> <li>Absolute Value</li> <li>Substitution (Nested Roots/Repeated Fractions)</li> <li>Mean, Median, Mode, Range</li> <li>Telescoping</li></ul>',
      Combinatorics:
        '<ul><li>Sticks and Stones</li> <li>Permutation/Combination</li> <li>Properties of Inclusion Exclusion for three or less sets</li> <li>Basic Geometric Probability</li> <li>Conditional Probability</li> <li>Expected Values</li> <li>Complementary Counting</li> <li>Recursion</li> <li>Bijections</li> <li>Casework</li> <li>Pigeonhole Principle</li> <li>Double-counting</li> <li>Basic Invariants</li></ul>',
    },
  ]
  let topicsSmall2 = [
    {
      Geometry:
        '<ul><li>Area Formulas</li> <li>Volume Formulas</li> <li>Shoelace Formula</li> <li>Pythagorean Theorem</li> <li>Distance Formula</li> <li>Similar Triangles</li> <li>Angle Chasing</li> <li>Power of a Point</li> <li>Basic Mass Points</li> <li>Heron’s Formula</li> <li>Pick’s Theorem</li> <li>Surface Area for Pyramids, Prisms, and Cones</li> <li>Arcs and Sectors</li> <li>Angle Bisector Theorem</li> <li>Internal/External Angles</li></ul>',
      'Number Theory':
        '<ul><li>Fermat’s Little Theorem</li> <li>Euclidean Algorithm</li> <li>Chinese Remainder Theorem</li> <li>Divisibility</li> <li>Chicken McNugget Theorem</li> <li>GCD and LCM</li> <li>Number of Factors</li> <li>Sum of Factors</li> <li>Basic Modular Arithmetic</li> <li>Fundamental Theorem of Arithmetic</li></ul>',
    },
  ]
  let topicsAlgebra = [
    {
      Algebra:
        '<ul><li>Systems of equations</li> <li>Quadratics</li> <li>Vieta’s</li> <li>Binomial Theorem</li> <li>Radicals/Exponents</li> <li>Simon’s Favorite Factoring Trick</li> <li>Ratios</li> <li>(Infinite) Geometric Series</li> <li>Arithmetic Series</li> <li>Sum/Difference of Powers</li> <li>Rate/Time</li> <li>Floor/Ceiling</li> <li>Absolute Value</li> <li>Substitution (Nested Roots/Repeated Fractions)</li> <li>Mean, Median, Mode, Range</li> <li>Telescoping</li></ul>',
    },
  ]
  let topicsCombo = [
    {
      Combinatorics:
        '<ul><li>Sticks and Stones</li> <li>Permutation/Combination</li> <li>Properties of Inclusion Exclusion for three or less sets</li> <li>Basic Geometric Probability</li> <li>Conditional Probability</li> <li>Expected Values</li> <li>Complementary Counting</li> <li>Recursion</li> <li>Bijections</li> <li>Casework</li> <li>Pigeonhole Principle</li> <li>Double-counting</li> <li>Basic Invariants</li></ul>',
    },
  ]
  let topicsGeo = [
    {
      Geometry:
        '<ul><li>Area Formulas</li> <li>Volume Formulas</li> <li>Shoelace Formula</li> <li>Pythagorean Theorem</li> <li>Distance Formula</li> <li>Similar Triangles</li> <li>Angle Chasing</li> <li>Power of a Point</li> <li>Basic Mass Points</li> <li>Heron’s Formula</li> <li>Pick’s Theorem</li> <li>Surface Area for Pyramids, Prisms, and Cones</li> <li>Arcs and Sectors</li> <li>Angle Bisector Theorem</li> <li>Internal/External Angles</li></ul>',
    },
  ]
  let topicsNT = [
    {
      'Number Theory':
        '<ul><li>Fermat’s Little Theorem</li> <li>Euclidean Algorithm</li> <li>Chinese Remainder Theorem</li> <li>Divisibility</li> <li>Chicken McNugget Theorem</li> <li>GCD and LCM</li> <li>Number of Factors</li> <li>Sum of Factors</li> <li>Basic Modular Arithmetic</li> <li>Fundamental Theorem of Arithmetic</li></ul>',
    },
  ]
</script>

<svelte:head>
  <title>MMT 2022</title>
</svelte:head>

<svelte:window bind:innerWidth={windowWidth} />

<PageHeader
  title="MMT 2022"
  description="MAY 28, 2022: 9 AM - 5 PM PT"
  button_url="https://contestdojo.com/"
  button_text="Register on ContestDojo!"
  button_id="registerOnContestDojo"
/>
<br /> <br />
<Dropdown
  mainText="Registration Instructions and Information"
  showContent={true}
  id="showDropdown"
>
  <ol start="0">
    <li>
      If you have a partial team (1-3 members) and are interested in getting to
      a full one, consider using our <a
        target="_blank"
        sveltekit:prefetch
        href="https://tinyurl.com/MMT2022TeammateFinder"
        >Teammate Finder Spreadsheet</a
      >. You can input your contact information and also contact other
      parents/coaches to try to find teammates for your students!
    </li>
    <li>
      Our registration is managed by <a
        target="_blank"
        sveltekit:prefetch
        href="https://contestdojo.com">ContestDojo</a
      > - if you are a coach for a math team, or just a parent registering your child's
      team, you should create a Coaches account on ContestDojo. Note - it may ask
      you to affirm that you are an 'official representative' for your organization
      - you can just click that checkbox to move on, we don't require you to be an
      official representative at MMT.
    </li>
    <li>
      Once you create your coaches account, you can click the little 'register'
      button for MMT 2022. Once you do that, you can add your students to your
      portal, buy the 'seats' for your students through Stripe, and create and
      organize your organization's teams! Registration cost is $10 per
      participant. If you have need for a partial or full fee waiver, please
      email us at <a target="_blank" href="mailto:contact@mustangmath.com"
        >contact@mustangmath.com</a
      > detailing your request.
    </li>
    <li>
      Once added to the coaches portal, students should receive an email from
      ContestDojo detailing how to login to their account. Students should look
      for this email and login so that they may try taking the 'ContestDojo
      Practice Round' in their portals with their team! This is helpful in
      making sure that they understand how our test portal works and are all set
      for competition day!
    </li>
    <li>
      You should be all set to go for the tournament! As always, email us at <a
        target="_blank"
        href="mailto:contact@mustangmath.com">contact@mustangmath.com</a
      > if you have any confusion or issues!
    </li>
  </ol>
  <strong class="registration-other">Registration closes May 27.</strong>
  <br />
  <p class="registration-other">
    International Students in a non-ideal timezone should participate in the
    international version of our tournament being run by SIMCC on August 27,
    2022. If you're interested in participating, you should email <a
      href="mailto:rupendrad@simcc.org"
      target="_blank">rupendrad@simcc.org</a
    >
  </p>
</Dropdown> <br />

<Heading text="MMT 2022 Unregistered Guide" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw;">
  <PanelBox>
    <p style="font-size: 1.5em; text-align: center;">
      A lot of the information on this page is reiterated in our <a
        href="https://docs.google.com/document/d/1mJQouqkewOWl8ZJuB3v_C9s-iJ3KBsK3QzrJkQliW_A/edit?usp=sharing"
        >MMT 2022 Unregistered Guide</a
      >. On completion of registration, you will receive a link by email to a
      complete version of the guide with relevant links and additional
      information!
    </p>
  </PanelBox>
</div>
<br />

<Heading text="Rounds" size={2.5} />
<div class="competition-wrapper">
  <FlexBox align="start">
    <Competition
      imgSource="mmt-2022/puzzlepiece.png"
      competition="Mounting Mayhem"
      description="A team puzzle round where participants are faced with a variety of logical and mathematical puzzles"
    />
    <Competition
      imgSource="mmt-2022/bingoboard.png"
      competition="Bucking Bingo"
      description="A 24-question strategy-based round where teams work to knock out as many bingos as possible!"
    />
    <Competition
      imgSource="mmt-2022/runninghorse.png"
      competition="Gallop"
      description="An intense, fast paced round where teams race to be at the top of the live-scored leaderboard"
    />
    <Competition
      imgSource="mmt-2022/magnifyingglass.png"
      competition="Mystery Mare"
      description="MMT's signature mystery round, where students will be introduced to the format of the round on competition day!"
    />
  </FlexBox>
</div>
<br />

<Heading text="Schedule" size={2.5} />
<div class="schedule-wrapper">
  <FlexBox>
    <PanelBox>
      <Table
        data={scheduleData}
        width="auto"
        headerColor="#1B9AAA"
        rowColors={['var(--table-color-1)', '#ADCDD6']}
        cellPadding={5}
        cellPaddingRight={20}
      />
    </PanelBox>
  </FlexBox>
</div>
<br />

<Heading text="Awards" size={2.5} />
<div style="margin-left: 10vw; margin-right: 10vw;">
  <PanelBox>
    <p style="font-size: 1.5em; text-align: center;">
      Medals will be given to (at minimum) the members of the top 5 teams of
      each division, along with certificates of participation to all students
      and certificates of achievement to high-scoring teams. A wide variety of
      other prizes are available for top scoring teams, winners of activities,
      and a raffle, including but not limited to <a
        target="_blank"
        href="https://education.ti.com/en/products/calculators/scientific-calculators/ti-30xs-mv"
        ><b>TI-30XS MultiView™ Scientific Calculators</b></a
      >,
      <a target="_blank" href="https://www.wolfram.com/notebooks/"
        >Wolfram Notebooks</a
      >, AoPS Gift Certificates,
      <a target="_blank" href="https://live.poshenloh.com/summer"
        >Daily Challenge Summer Class Vouchers</a
      >, and
      <a target="_blank" href="https://www.bbmc-math.com/"
        >BBMC Math Summer Class Vouchers</a
      >.
    </p>
  </PanelBox>
</div>
<br />

<Heading text="Rules" size={2.5} />
<Dropdown mainText="General Rules" id="showDropdown">
  <ol>
    <li>
      No cheating - This contest has a zero-tolerance cheating policy. Any
      evidence of cheating may lead to immediate disqualification, or any other
      punishment deemed appropriate by competition staff.
    </li>
    <li>
      No calculators, rulers, compasses, protractors, or other aids are
      permitted.
    </li>
    <li>
      You may not use the Internet as a resource at any point during a test.
    </li>
    <ol type="a">
      <li>
        In order to help enforce this, we may require teams to provide a
        solution for a problem during the competition - so keep track of your
        work!
      </li>
    </ol>
    <li>All communication will take place through the Discord platform.</li>
    <ol type="a">
      <li>
        Scores, important information, documents, etc. will only be communicated
        through this platform on the day of the contest.
      </li>
      <li>
        All teams should be communicating with each other on this platform ONLY.
      </li>
      <li>
        <strong
          >Students under 13 years of age should use a parent-created and
          monitored Discord account.</strong
        >
      </li>
    </ol>
    <li>
      Teams may not collaborate with people other than the 1-4 members of their
      own registered team. This includes members from other teams, parents,
      coaches, siblings, and friends.
    </li>
    <li>
      Teams will be split into three divisions based on the sum of their grade
      levels. Empty spots and students 5th grade and below count for 5 “points”.
      The exact sum splits will be determined to even out the divisions as much
      as possible.
    </li>
  </ol>
</Dropdown>
<Dropdown mainText="Answer Formatting Rules" id="showDropdown">
  <ol>
    <li>
      Carry out any reasonable calculations. For instance, you should evaluate
      any expressions which will take negligible time to evaluate (such as
      1/2+1/3). Unreasonable calculations include large powers (e.g. 7<sup
        >8</sup
      >), large factorials, large products, and trigonometric functions which
      cannot be expressed in terms of radicals.
    </li>
    <li>
      Write rational numbers in lowest terms. Decimals are also acceptable,
      provided they are exact.
    </li>
    <li>
      Move all square factors outside radicals. For example, write 3√7 instead
      of √63.
    </li>
    <li>
      Denominators need to be rationalized. For example, write 1/√2 as √2/2
      instead.
    </li>
    <li>Do not express an answer using a repeated sum or product.</li>
    <li>
      Here are some examples of simplified answers, and examples of unsimplified
      answers with simplified equivalents:
      <div style="margin-top: 5px">
        <Image
          url="mmt-2022/acceptable-answers.png"
          alt="Acceptable answer examples"
        />
      </div>
      <div style="margin-top: 5px">
        <Image
          url="mmt-2022/unacceptable-answers.png"
          alt="Unacceptable answer examples"
        />
      </div>
    </li>
  </ol>
</Dropdown>
<Dropdown mainText="Potential Topics Covered" id="showDropdown">
  <p id="disclaimer">
    Disclaimer: While most problems should fall within the scope of these
    topics, there may be a few that are not.
  </p>
  {#if windowWidth > 1000}
    <Table
      data={topicsCovered}
      width="100%"
      headerColor="#1B9AAA"
      rowColors={['var(--table-color-1)']}
      cellPadding={5}
      cellPaddingRight={20}
      textSize={1}
      cellStyle="vertical-align: top; font-size: {windowWidth / 1200}em;"
      tableStyle="table-layout: fixed; padding: 10px;"
      headerStyle="font-size: {windowWidth / 1500}em;"
    />
  {:else if windowWidth > 800}
    <Table
      data={topicsSmall1}
      width="100%"
      headerColor="#1B9AAA"
      rowColors={['var(--table-color-1)']}
      cellPadding={5}
      cellPaddingRight={20}
      textSize={1}
      cellStyle="vertical-align: top; font-size: {windowWidth / 800}em;"
      tableStyle="table-layout: fixed; padding: 10px;"
      headerStyle="font-size: {windowWidth / 800}em;"
    />
    <Table
      data={topicsSmall2}
      width="100%"
      headerColor="#1B9AAA"
      rowColors={['var(--table-color-1)']}
      cellPadding={5}
      cellPaddingRight={20}
      textSize={1}
      cellStyle="vertical-align: top; font-size: {windowWidth / 800}em;"
      tableStyle="table-layout: fixed; padding: 10px;"
      headerStyle="font-size: {windowWidth / 800}em;"
    />
  {:else}
    <Table
      data={topicsAlgebra}
      width="100%"
      headerColor="#1B9AAA"
      rowColors={['var(--table-color-1)']}
      cellPadding={5}
      cellPaddingRight={20}
      textSize={1}
      cellStyle="vertical-align: top; font-size: {windowWidth / 500}em;"
      tableStyle="table-layout: fixed; padding: 10px;"
      headerStyle="font-size: {windowWidth / 500}em;"
    />
    <Table
      data={topicsCombo}
      width="100%"
      headerColor="#1B9AAA"
      rowColors={['var(--table-color-1)']}
      cellPadding={5}
      cellPaddingRight={20}
      textSize={1}
      cellStyle="vertical-align: top; font-size: {windowWidth / 500}em;"
      tableStyle="table-layout: fixed; padding: 10px;"
      headerStyle="font-size: {windowWidth / 500}em;"
    />
    <Table
      data={topicsGeo}
      width="100%"
      headerColor="#1B9AAA"
      rowColors={['var(--table-color-1)']}
      cellPadding={5}
      cellPaddingRight={20}
      textSize={1}
      cellStyle="vertical-align: top; font-size: {windowWidth / 500}em;"
      tableStyle="table-layout: fixed; padding: 10px;"
      headerStyle="font-size: {windowWidth / 500}em;"
    />
    <Table
      data={topicsNT}
      width="100%"
      headerColor="#1B9AAA"
      rowColors={['var(--table-color-1)']}
      cellPadding={5}
      cellPaddingRight={20}
      textSize={1}
      cellStyle="vertical-align: top; font-size: {windowWidth / 500}em;"
      tableStyle="table-layout: fixed; padding: 10px;"
      headerStyle="font-size: {windowWidth / 500}em;"
    />
  {/if}
</Dropdown>
<Dropdown mainText="ROUND 1: Mounting Mayhem (Puzzle)" id="showDropdown">
  <ol>
    <li>
      The Mounting Mayhem Round will consist of a series of logic puzzles
      centered around a certain theme.
    </li>
    <li>
      Students will have 15 minutes to read the instructions and then 60 minutes
      to work together with their teams and solve as many of the puzzles as
      possible.
    </li>
    <li>
      Harder puzzles will be worth more points, but these puzzles will be longer
      and/or require more creativity — you must decide what problems to focus
      your time on to optimize your team score.
    </li>
  </ol>
</Dropdown>
<Dropdown mainText="ROUND 2: Bucking Bingo" id="showDropdown">
  <ol>
    <li>
      The “Bingo” Round will consist of 24 questions to be solved in 60 minutes.
    </li>
    <li>
      The questions will vary in difficulty, but not necessarily in increasing
      order — rather the difficult problems will be randomly distributed.
    </li>
    <li>The image below shows the format of the Bingo board:</li>
    <img src="bingo-board.png" alt="Bingo Board" height="300em" />
    <li>
      In this round, each correctly solved question is worth points, but each
      completed and correct Bingo (each of the problems in a given row, column,
      or long diagonal are solved and correct) is worth bonus points!
    </li>
    <li>
      You are not expected to solve all the questions in this round within the
      allotted time. Instead, we encourage you to strategize how you might use
      your time to maximize your points!
    </li>
  </ol>
</Dropdown>
<Dropdown mainText="ROUND 3: Gallop (Guts)" id="showDropdown">
  <ol>
    <li>
      The Gallop Round will consist of 27 questions to be solved in 60 minutes.
    </li>
    <li>
      The questions will be divided into 9 sets of 3 questions each, and you <strong
        >must submit the answers to one set</strong
      > before accessing the problems for the next. This means you must strategize
      when to submit each set (incomplete or not) to ensure you get access to as
      many questions as possible.
    </li>
    <li>
      The problems will get progressively more difficult, and later problems
      will be worth more points.
    </li>
    <li>
      Submissions will be scored immediately and a live score of all
      participating teams will be available during the competition. Prepare for
      the adrenaline rush!
    </li>
  </ol>
</Dropdown>
<Dropdown mainText="ROUND 4: Mystery Mare" id="showDropdown">
  <ol>
    <li>The Mystery Mare round is exactly that — a mystery!</li>
    <li>
      The exact format of the round will be revealed on competition day, but we
      might drop some hints in communication to students!
    </li>
    <li>We promise it will be as fun and engaging as the other rounds.</li>
  </ol>
</Dropdown>
<Dropdown mainText="FAQ" id="showDropdown">
  <p>
    <strong>Q:</strong> I'm a parent or a student, not a coach - how can I
    register? <br />
    <strong>A:</strong> MMT doesn't require you to be a coach! A parent can act
    as a coach (and register as a coach on ContestDojo) to create an
    organization and team(s) for their participating students.
    <strong>Students should not create coach accounts.</strong>
  </p>
  <p>
    <strong>Q:</strong> I have students that are interested in participating,
    but they are not a full team of 4 and would like to be paired up with other
    incomplete teams! How can we do this? <br />
    <strong>A:</strong> Use our
    <a href="https://tinyurl.com/MMT2022TeammateFinder" target="_blank"
      >Teammate Finder Spreadsheet</a
    >! There, you can input your parent/coach contact information and find
    others to join your team!
  </p>
  <p>
    <strong>Q:</strong> Do we have to participate separately from our own homes?
    Or can our entire team meet up and take the test together? <br />
    <strong>A:</strong> Absolutely, your team can meet up and take the test together!
    We still require that your team is present on Discord with the video on and all
    members visible so that you can receive information in a timely manner!
  </p>
  <p>
    <strong>Q:</strong> Where can I find practice material for the tests? How
    can we prepare? <br />
    <strong>A:</strong> You can take a look at our
    <a target="_blank" sveltekit:prefetch href="/past-exams">past tests</a>, and
    we also highly recommend looking at
    <a
      target="_blank"
      sveltekit:prefetch
      href="https://www.mathcounts.org/resources/past-competitions"
      >past MathCounts</a
    >,
    <a
      target="_blank"
      sveltekit:prefetch
      href="https://artofproblemsolving.com/wiki/index.php/AMC_Problems_and_Solutions"
      >AMC 8/10</a
    >, and
    <a
      target="_blank"
      sveltekit:prefetch
      href="https://www.ocf.berkeley.edu/~bmt/archive/">BmMT</a
    > tests as these are similar in level to the problems at MMT.
  </p>
</Dropdown>
<br />

<style>
  li {
    margin-bottom: 0.5em;
  }
  .competition-wrapper {
    margin-right: 5vw;
    margin-left: 0vw;
    width: 100%;
  }
  #disclaimer {
    margin-left: 1em;
  }
  .registration-other {
    margin-left: 1.5em;
  }
</style>
