<template class="my-default">
	<div class="container-fluid vh-100 my-font-family">
    <b-sidebar id="sidebar-1" title="Sidebar" right shadow>
			<b-list-group class="m-2">
				<b-list-group-item button v-on:click="start">Start</b-list-group-item>
				<b-list-group-item button v-on:click="stop">Stop</b-list-group-item>
				<b-list-group-item button v-on:click="test">Test</b-list-group-item>
			</b-list-group>
		</b-sidebar>

    <b-button v-b-toggle.sidebar-1>Toggle Sidebar</b-button>

		<div class="row col-10" style="height: 500px">
			<div ref="chartdiv" class="h-z100 col-12 p-0 m-0">
				<Charts :dc="dc"/>
			</div>
		</div>

	</div>  
</template>

<script>
import Charts from '../components/Charts.vue'
import { mapState } from 'vuex'
import { DataCube } from 'trading-vue-js'
import moment from 'moment'
import Data from '../data/data.json'

// import axios from 'axios'
// import store from '../store'

export default {
  sockets: {
    connect() {
      console.log('socket connected')
    },

    server_1mk_history_ymF(data) {
      // self.dc = new DataCube(Data)
      let dd = JSON.parse(data)
      // console.log(dd)
      console.log(dd[0].Datetime)
      console.log(dd[1].Datetime)
      console.log(dd[2].Datetime)

      let processed = JSON.parse(data).map(e => {
        // format: [timestamp, open, high, low, close, volume],
        return [
          +moment(e.Datetime), e.Open, e.High, e.Low, e.Close, e.Volume]
      });
      
      this.dc.merge('chart.data', processed)
      console.log(processed[0])
    }
  },
  name: 'About',
  components: {
    Charts,
  },
  computed: {
    ...mapState([
      'code',
      'last_update',
      'tickData',
      'tickData_large'
    ])
  },
  methods : {
    start: function(event){
      this.$socket.client.emit('client_get_1mk_history',null,(msg)=>console.log(msg))
    },
    stop: function(event){

    },
    test : function(event){

    },
  },
  data(){ 
    return {
      volume_text: ["Volume","交易訂單"],
      volume_large_text: ["Large Volume","大單"],
      dc: new DataCube(Data)
    }
  }
}
</script>

<style>
  .my-font-family{
    font-family: 微軟正黑體修正,微軟正黑體修正2,微軟正黑體,'Microsoft JhengHei',Arial;
  }

  .my-default{
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    /* text-align: center; */
    color: #2c3e50;
    margin-top: 0px;
  }

  /* html, body {
    height: 100%;
  } */

  @import '../assets/c3.min.css';
</style>