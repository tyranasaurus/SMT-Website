<!-- Component for that shadow box with glow on hover thing -->
<script>
    export let width = "unset";
    export let height = "unset";
    export let margin = "10px";
    export let padding = "10px";
    export let borderRadius = "5px";
    export let style = "";
    export let boxSizing = "border-box";
</script>

<div
    class="panel-box"
    style="width: {width}; height: {height}; margin: {margin}; padding: {padding}; border-radius: {borderRadius}; box-sizing: {boxSizing}; {style}"
>
    <slot />
</div>

<style>
    .panel-box {
        background-color: white;
        /*box-shadow: 5px 10px 10px rgb(0, 0, 0, 0.1);*/
        opacity: 0.8;
        transition: 0.5s;
    }

    .panel-box:hover {
        background-color: var(--hover-color);
        opacity: 1;
    }
</style>
