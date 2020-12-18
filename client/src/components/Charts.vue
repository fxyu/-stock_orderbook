<template>
    <div style="width: 800px; border:1px solid">
        <div id="mychart"></div>
    </div>
</template>

<script>
import c3 from 'c3'

export default {
    name: 'Charts',
    props: {},
    data() {
        return {
            chart : 1
        }
    },
    mounted(){
        console.log('Mounted()');
            // console.log(this.$c3)
        c3.generate({
            bindto: '#mychart',
            data: {
                json: [
                    {price: 100, bid: 10, ask: 0},
                    {price: 101, bid: 0, ask: 10},
                    {price: 102, bid: 0, ask: 10},
                    {price: 103, bid: 0, ask: 10},
                    {price: 104, bid: 0, ask: 10},
                    {price: 105, bid: 0, ask: 10},
                    {price: 106, bid: 0, ask: 10},
                    {price: 107, bid: 0, ask: 10},
                    ],
                keys: {
                    x: 'price', // it's possible to specify 'x' when category axis
                    value: ['bid','ask']
                },
                // columns : [

                // ],
                type: 'bar',
                labels: {
                    format: function (v, id, i, j) { if (v>0) return v; }
                },
                groups: [
                    ['bid','ask']
                ]
            },
            grid: {
                y: {
                    lines: [{value:0}]
                }
            },
            axis: {
                x: {
                    type: 'category',
                    tick: {
                        rotate: 90,
                        multiline: false,
                    }
                },
                y: {
                    min : 0,
                    max : 30,
                    padding: {top:0, bottom:0}
                }

            },
            bar: {
                width: {
                    ratio: 0.95
                }
            },
            transition: {
                duration: 30
            }
        });
        
        // this.$forceUpdate();
        
    }
}
</script>

<style>
    
</style>