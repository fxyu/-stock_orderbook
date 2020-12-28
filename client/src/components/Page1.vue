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
    
    <div class="container m-0 p-0">
      <button v-on:click="start">Start</button>
      <button v-on:click="stop">Stop</button>
      <button v-on:click="test">Test</button>
      <button v-on:click="newItemTest">New Item Test</button>
      <button v-on:click="get_history">Get History</button>
      <button v-on:click="renew_1mData">Update_new_1m</button>
      <button v-on:click="get_ob_history">OB history</button>
    </div>

    <DraggableDiv ref="pDiv" class="col-12 m-0 p-0">
      <template slot="header">
        Chart
      </template>
      <template slot="main" >
        <Charts />
      </template>
    </DraggableDiv>  
  </div>  
</template>

<script>
import OrderBookCharts from './OrderBookCharts.vue'
import DraggableDiv from './DraggableDiv.vue'
import Charts from './Charts.vue'
import TickTable from './TickTable.vue'
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
    Charts,
    DraggableDiv
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
          // console.log(history)
          store.commit('add_tick_data',history)
        })

      this.$socket.client.emit('client_get_1m_kdata',null,function(rtn){
        console.log(rtn)
      })
    },
    renew_1mData : function(event){
      store.commit('renew_1mData',{})
    },
    get_ob_history: function(event){
      this.$socket.client.emit('client_get_ob_history',null,function(rtn){
        console.log(rtn)
      })
    }
  }
}
</script>

<style scoped>
  .my-font-family{
        font-family: 微軟正黑體修正,微軟正黑體修正2,微軟正黑體,'Microsoft JhengHei',Arial;
  }
</style>