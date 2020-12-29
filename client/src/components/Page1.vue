<template>
  <div class="container-fluid vh-100 my-font-family">
    <div class="w-100 row d-inline-block p-0 m-0" 
         style="height: 10%; background-color: rgba(0,0,255,.1)">
      <div class="col-11">
        <h3>{{code}}</h3>
        <p>{{last_update}}</p>
      </div>
    </div>
    
    <div class="row p-0 m-0" 
          style="height: 90%; background-color: rgba(0,255,255,.1)">

      <div class="col-2">

        <b-list-group class="m-2">
          <b-list-group-item button v-on:click="start">Start</b-list-group-item>
          <b-list-group-item button v-on:click="stop">Stop</b-list-group-item>
          <b-list-group-item button v-on:click="test">Test</b-list-group-item>
          <b-list-group-item button v-on:click="newItemTest">New Item Test</b-list-group-item>
          <b-list-group-item button v-on:click="get_history">Get History</b-list-group-item>
          <b-list-group-item button v-on:click="renew_1mData">Update new 1m</b-list-group-item>
          <b-list-group-item button v-on:click="get_ob_history">OB history</b-list-group-item>
        </b-list-group>

      </div>


      <div class="col-9 p-0 m-0">

        <div class="h-50 row col-12 p-2 m-0">
          <OrderBookCharts />
        </div>

        <div class="h-50 row p-2 m-0">
          <div class="h-100 col-6 p-0 m-0"
               style="background-color: rgba(0,255,155,.1)">
            <div class="row p-0 m-0">
              <TickTableV2 
                v-bind:tickItems="tickData" 
                v-bind:title="volume_text"
                class="col-6"/>
              <TickTableV2 
                v-bind:tickItems="tickData_large" 
                v-bind:title="volume_large_text"
                class="col-6"/>
            </div>
          </div>
          
          <div ref="chartdiv" class="h-100 col-6 p-0 m-0">
            <Charts/>
          </div>
        </div>
      </div>

    </div>

    <DraggableDiv ref="pDiv" class="col-12 m-0 p-0" style="display: None">
      <template slot="header">
        Chart
      </template>
      <template slot="main" >
        
      </template>
    </DraggableDiv>  
  </div>  
</template>

<script>
import OrderBookCharts from './OrderBookCharts.vue'
import DraggableDiv from './DraggableDiv.vue'
import Charts from './Charts.vue'
import TickTable from './TickTable.vue'
import TickTableV2 from './TickTableGrid.vue'
import { mapState } from 'vuex'
import axios from 'axios'
import store from '../store'

export default {
  sockets: {
    connect() {
      console.log('socket connected')

      this.$socket.client.emit('client_history',null,function(history){
          // console.log(history)
          store.commit('add_tick_data',history)
        })

      this.$socket.client.emit('client_get_1m_kdata',null,function(rtn){
        console.log(rtn)
      })
    },
  },
  name: 'App',
  components: {
    OrderBookCharts,
    // TickTable,
    Charts,
    DraggableDiv,
    TickTableV2
  },
  computed: mapState([
    'code',
    'last_update',
    'tickData',
    'tickData_large'
  ]),
  methods : {
    start: function(event){
      axios.get('http://localhost:5005/start')
        .then((res) => console.log(res))
        .catch((err) => console.log(err))
    },
    stop: function(event){
      axios.get('http://localhost:5005/stop')
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
  },
  data(){ 
    return {
      volume_text: ["Volume","交易訂單"],
      volume_large_text: ["Large Volume","大單"]
    }
  }
}
</script>

<style>
  .my-font-family{
    font-family: 微軟正黑體修正,微軟正黑體修正2,微軟正黑體,'Microsoft JhengHei',Arial;
  }

  /* html, body {
    height: 100%;
  } */
</style>