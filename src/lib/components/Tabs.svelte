<script>
    export let items = [];
    export let style;
    export let activeTabValue = 1;
    import {LightenDarkenColor} from "$lib/utils/Colors.svelte";
  
    const handleClick = (tabValue) => () => (activeTabValue = tabValue);
    
  </script>
  <!-- 
      This is NOT very universal right now - component could be made more versatile!
      Ever item needs to have a hex, a value, 
  -->
  <div class="tabs" {style}>
      <ul>
          <div class="rolebar">
              {#each items as item}
              <li
                  class={activeTabValue === item.value ? "active" : "inactive"}
              >
                  <span style="background-color: {item.hex}" on:click={handleClick(item.value)}>{item.label}</span>
              </li>
              {/each}
          </div>
      </ul>
      <div class="content">
          {#each items as item}
              {#if activeTabValue == item.value}
                  <div class="box" style="background-color: {item.hex} border-radius: 30px">
                      <slot {item} />
                  </div>
              {/if}
          {/each}
      </div>
  </div>
  
  <style>
    .box {
      margin-bottom: 10px;
      border: 1px solid #dee2e6;
      border-radius: 20em;
      border-top: 0;
      margin-top: 0px;
    }
    ul {
      flex-wrap: wrap;
      margin-bottom: 0;
      list-style: none;
    }
    .tabs {
      justify-content: center;
    }
    .rolebar {
      justify-content: center;
      width: 100%;
      display: flex;
      flex-wrap: wrap;
    }
    li {
      bottom: 0;
      text-align: center;
      border-radius: 17px 17px 0 0;
      margin-right: 3px;
    }
  
    span {
      border: 1px solid transparent;
      border-radius: 17px 17px 0 0;
      display: block;
      padding: 0.5rem 1rem;
    }
  
    li.inactive > span:hover {
      filter: brightness(105%);
      cursor: pointer;
    }
  
    li.active > span {
      color: #000000;
      font-weight: bold;
    }
  </style>
  