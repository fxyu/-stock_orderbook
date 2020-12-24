<template>
    <!-- TradingVueJs 101 (example from 'Getting Started' ) -->
    <trading-vue :data="chart" :width="this.width" :height="this.height"
        :overlays="overlays"
        :color-back="colors.colorBack"
        :color-grid="colors.colorGrid"
        :color-text="colors.colorText">
    </trading-vue>
</template>

<script>
import TradingVue from 'trading-vue-js'
import Data from '../data/data.json'
import PerfectTrades from './overlay/PerfectTrades.js'
import Grin from './overlay/Grin.js'

export default {
    name: 'Chart',
    components: { TradingVue },
    props : ['divWidth'],
    methods: {
        onResize(event) {
            this.width = window.innerWidth
            this.height = window.innerHeight
        }
    },
    mounted() {
        // console.log(this.$ref.pDiv.width)
        // this.width = this.$ref.pDiv.width
        // this.height = this.$ref.pDiv.height
        window.addEventListener('resize', this.onResize)
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.onResize)
    },
    data() {
        return {
            chart: Data,
            width: window.innerWidth,
            height: window.innerHeight,
            colors: {
                colorBack: '#fff',
                colorGrid: '#eee',
                colorText: '#333',
            },
            overlays: [PerfectTrades]
        }
    },
    
}
</script>

<style>

</style>