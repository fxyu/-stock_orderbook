<template>
    <div id="chart"></div>
</template>

<script>
import * as c3 from 'c3'

export default {
    name: 'Charts',
    props: {},
    data() {
        return {
            chart : null
        }
    },
    created(){
        this.chart = c3.generate({
                bindto: '#chart',
                data: {
                    columns: [
                        ['data1', -30, 200, 200, 400, -150, 250],
                        ['data2', 130, 100, -100, 200, -150, 50],
                        ['data3', -230, 200, 200, -300, 250, 250]
                    ],
                    type: 'bar',
                    groups: [
                        ['data1', 'data2']
                    ]
                },
                grid: {
                    y: {
                        lines: [{value:0}]
                    }
                }
            });
            this.$forceUpdate();
        
    }
}
</script>

<style>
    
</style>