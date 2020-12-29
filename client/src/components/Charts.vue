<template>
    <div class='p-0 m-0'>
        <!-- <button :v-bind="reset">R</button>
        <span class="night-mode">
            <input type="checkbox" v-model="night">
            <label>NM</label>
        </span> -->
        <trading-vue :data="dc" :width="this.width" :height="this.height"
            title-txt="HK.HSIMain"
            ref="tvjs"
            :extensions="ext"
            :overlays="overlays"
            :timezone="parseInt(8)"
            :toolbar="true"
            :color-back="colors.colorBack"
            :color-grid="colors.colorGrid"
            :color-text="colors.colorText">
        </trading-vue>
    </div>
</template>

<script>
import TradingVue from 'trading-vue-js'
import XP from 'tvjs-xp'
import Overlays from 'tvjs-overlays'
import PerfectTrades from './overlay/PerfectTrades.js'
// import Grin from './overlay/Grin.js'

export default {
    name: 'Chart',
    components: { TradingVue },
    props : ['divWidth'],
    computed: {
        dc () {
            return this.$store.state.chart
        }
    },
    methods: {
        onResize(event) {
            // console.log(this.$parent)
            // let parent = this.$parent
            this.width = this.$parent.$refs.chartdiv.clientWidth
            this.height = this.$parent.$refs.chartdiv.clientHeight
        },
        reset(event){
            this.$refs.tvjs.resetChart()
        }
    },
    mounted() {
        // console.log(this.$ref.pDiv.width)
        this.width = this.$parent.$refs.chartdiv.clientWidth
        this.height = this.$parent.$refs.chartdiv.clientHeight
        window.addEventListener('resize', this.onResize)
        // console.log(Object.values(Overlays))
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.onResize)
    },
    data() {
        return {
            // chart: Data,
            width: null,
            height: null,
            colors: {
                colorBack: '#fff',
                colorGrid: '#eee',
                colorText: '#333',
            },
            ext: Object.values(XP),
            overlays: Object.values(Overlays),
            night: true,
        }
    },
    
}
</script>

<style>
.night-mode {
    position: absolute;
    top: 30px;
    right: 30px;
}
</style>