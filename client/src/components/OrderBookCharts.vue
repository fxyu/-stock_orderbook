<template>
    <div style="width: 100%; height:100%; border:1px solid" ref="mychart">
        <div id="mychart"></div>
    </div>
</template>

<script>
import c3 from 'c3'

export default {
    name: 'OrderBookCharts',
    props: {},
    data() {
        return {
            chart : null
        }
    },
    computed: {
        ob () {
            return this.$store.state.ob
        }
    },
    mounted(){
        // console.log('Mounted()');
            // console.log(this.$c3)
        this.chart = c3.generate({
            bindto: '#mychart',
            data: {
                json: [{price: 100, bid: 10, ask: 0}],
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
                    max : 100,
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
            },
            // onresized: function (){ 
            //     this.selectChart.style('max-height', 'none')
            // },
            size: {
                height: 400
            }
        });
        
        // this.chart.resize({height: this.$refs.mychart.clientHeight}) 
        window.addEventListener('resize', this.onResize)  
    },
    watch: {
        'ob': function () {
            // ob = newData.data

            // if ($('#check_auto').is(":checked")){
            //     low_price = Math.round(ob[0].price / 5 ) * 5 - 10
            //     high_price = low_price + 40  
            // }
            // else{
            //     low_price = $('#range_low').val()
            //     high_price = $('#range_high').val()

            //     if (high_price-low_price > 300){
            //         low_price = Math.round(ob[0].price / 5 ) * 5 - 10
            //         high_price = low_price + 40  
            //     }
            // }
            
            // var tmp1 = []
            // for(var n=low_price; n<ob[0].price; n++ ){
            //     tmp1.push({
            //         price : n,
            //         ask : 0,
            //         bid : 0
            //     })
            // }

            // var tmp2 = []
            // for(var n=ob[ob.length-1].price + 1; n<=high_price; n++ ){
            //     tmp2.push({
            //         price : n,
            //         ask : 0,
            //         bid : 0
            //     })
            // }

            // ob = tmp1.concat(ob).concat(tmp2)
            // console.log(this.ob)
            this.chart.load({
                json: this.ob,
                keys: {
                    x: 'price',
                    value: ['ask', 'bid']
                }
            });
        }
    },
    methods: {
        onResize(event) {
            // console.log(this.$refs.mychart.clientHeight)
            this.chart.resize({height: this.$refs.mychart.clientHeight-10})
        }
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.onResize)
    }
}
</script>

<style>
    
</style>