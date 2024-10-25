<script>
	export let data = [[]];
    export let colStyles = [];
    export let headerRow = true;

    import { onMount } from 'svelte';

    const getColumnStyles = (column) => {
        let styles = '';

        // Iterate through column properties and add them to the style string
        for (const key in column) {
            styles += `${key}: ${column[key]}; `;
        }

        return styles;
    };

	let tableData = [];
    let loading = true;

	console.log(data);
    async function merge(rowIdx, colIdx) {
		let curRowIdx = rowIdx;
		let curColIdx = colIdx;
		const value = data[rowIdx][colIdx];
        if (value === null) {
            return
        }
        //console.log("Val",value)
		let colCount = 1;
		let rowCount = 1;
		while (curColIdx + 1 < data[curRowIdx].length && data[curRowIdx][curColIdx + 1] === value) {
			curColIdx++;
			colCount++;
		}
		while (true) {
			curRowIdx++;
			curColIdx = colIdx;
			while (curRowIdx < data.length && data[curRowIdx][curColIdx] === value) {
				curColIdx++;
			}
			if (curColIdx - colIdx == colCount) {
				rowCount++;
			} else {
				break;
			}
		}
		//console.log('index', rowIdx, colIdx);
		//console.log('count', rowCount, colCount);
		for (let i = 0; i < rowCount; i++) {
            data[rowIdx + i].fill(null, colIdx, colIdx+colCount)
			//console.log('D', data);
		}
		tableData[rowIdx].push([value, rowCount, colCount, colStyles[colIdx] ? colStyles[colIdx] : ""]);
	}

	async function processData(data) {
		for (let i = 0; i < data.length; i++) {
            tableData.push([]);
			for (let j = 0; j < data[i].length; j++) {
				//console.log(i, j);
				await merge(i, j);
				//console.log(data);
				//console.log(tableData);
			}
		}
        //console.log(tableData)
	}

    onMount(async () => {
        await processData(data);
        console.log(tableData);
        loading = false;
    });

	
</script>

<!-- Table rendering -->
{#if !loading}
    <table>
        {#each tableData as row, rowIndex (row)}
            <tr>
                {#if headerRow && rowIndex == 0}
                    {#each row as cell, colIndex (cell)}
                        <th 
                            rowspan={cell[1]} 
                            colspan={cell[2]}
                        >
                            {@html cell[0]}
                        </th>
                    {/each}
                {:else}
                    {#each row as cell, colIndex (cell)}
                        <td 
                            style={cell[3]}
                            rowspan={cell[1]} 
                            colspan={cell[2]}
                        >
                            {@html cell[0]}
                        </td>
                    {/each}
                {/if}
            </tr>
        {/each}
    </table>
{:else}
    <p>Loading...</p>
{/if}

<style>
	/* Add your styling here */
	table {
		border-collapse: collapse;
		width: 100%;
        table-layout: auto;
	}

	td,
	th {
		border: 1px solid var(--accent-color);
		padding: 8px;
		text-align: center;
        height: 1px;
	}

    th {
        color: var(--bold-color);
        font-size: 110%
    }

    @media only screen and (max-width: 600px) {
        table {
            font-size: 0.4rem; /* Adjust the font size for smaller screens */
        }
    }

</style>
