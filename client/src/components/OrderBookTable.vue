<template>
    <div style="width:600px" class="m-2 obTable">
        <b-row>
            <b-col cols=2 >Price</b-col>
            <b-col cols=2 >Volume</b-col>
            <b-col cols=6> </b-col>
        </b-row>
        <b-row v-for="(item, index) in ob" :key="index">
            <b-col cols=2 >{{item[0]}}</b-col>
            <b-col cols=2 >{{item[1]}}</b-col>
            <b-col cols=6>
                <b-progress height="100%" :max="max" show-value>
                    <b-progress-bar :value="item[1]" :variant="item[2] ? 'success' : 'warning'" style="transition: none;"></b-progress-bar>
                </b-progress>
            </b-col>
        </b-row>

        <b-button class="mt-3" @click="randomValue">Click me</b-button>
    </div>
</template>

<script>


export default {
    name: 'OrderBookTable',
    props: {},
    data() {
        return {
            fakeOb: [
                [1000, 23, 1],
                [1001, 10, 1],
                [1002, 15, 1],
                [1003, 0, 0],
                [1004, 26, 0],
                [1005, 32, 0],
                [1006, 45, 0],
            ],
            value: 30,
            max: 200
        }
    },
    computed: {
        ob () {
            return this.$store.state.ob
        }
    },
    mounted(){

    },
    watch: {
    },
    methods: {
        randomValue() {
            this.value = Math.random() * this.max
        },
        process_map(item){
            return item ? "success" : "warning"
        }
    },
    beforeDestroy() {
    }
}
</script>

<style scoped>
    .obTable .row > div {
        /* background: lightgrey; */
        font-size: 12px;
        border: 1px solid grey;
    }
</style>