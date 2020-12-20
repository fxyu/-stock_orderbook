<template>
  <div class="my-font-family">
    <h3>{{code}}</h3>
    <p>{{last_update}}</p>

    <OrderBookCharts />

    <div class="container-sm mt-3 m-0 p-0">
      <div class="row">
        <TickTable v-bind:tickItems="tickData" class="col-6 m-0 p-0" style="border:1px solid; overflow-y: scroll; height: 200px"/>
        <TickTable v-bind:tickItems="tickData_large" class="col-6 m-0 p-0" style="border:1px solid; overflow-y: scroll; height: 200px"/>
      </div>
    </div>
    
    <button v-on:click="start">Start</button>
    <button v-on:click="stop">Stop</button>
    <button v-on:click="test">Test</button>
    <button v-on:click="newItemTest">New Item Test</button>
    <button v-on:click="get_history">Get History</button>
  </div>  
</template>

<script>
import OrderBookCharts from './OrderBookCharts'
import TickTable from './TickTable'
import { mapState } from 'vuex'
import axios from 'axios'
import store from '../store'

export default {
  sockets: {
    connect() {
      console.log('socket connected')
    },
  },
  name: 'App',
  components: {
    OrderBookCharts,
    TickTable,
  },
  computed: mapState([
    'code',
    'last_update',
    'tickData',
    'tickData_large'
  ]),
  methods : {
    start: function(event){
      axios.get('http://0.0.0.0:5005/start')
        .then((res) => console.log(res))
        .catch((err) => console.log(err))
    },
    stop: function(event){
      axios.get('http://0.0.0.0:5005/stop')
        .then((res) => console.log(res))
        .catch((err) => console.log(err))
    },
    test : function(event){
      // axios.get('http://0.0.0.0:5005/test')
      //   .then((res) => console.log(res))
      //   .catch((err) => console.log(err))

      store.commit('new_ob_json', [
                {price: 100, bid: 10, ask: 0},
                {price: 101, bid: 0, ask: 10},
                {price: 102, bid: 0, ask: 10},
                ])
    },
    newItemTest : function(event){
      store.commit('add_tick_data',[['14:01:13 30000 1', 1]])
    },
    get_history : function(event){
      this.$socket.client.emit('client_history',null,function(history){
          console.log(history)
          store.commit('add_tick_data',history)
        })
    },
  }
}
</script>

<style scoped>
  .my-font-family{
        font-family: 微軟正黑體修正,微軟正黑體修正2,微軟正黑體,'Microsoft JhengHei',Arial;
  }
</style>