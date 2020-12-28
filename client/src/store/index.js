import Vue from 'vue'
import Vuex from 'vuex'
import Data from '../data/data.json'
import moment from 'moment'

Vue.use(Vuex)

const manageNewTickData = function(newData){
  let data = newData[0].split(' ')
  let tickItem = {
    'Time': data[0], 
    'Price': data[1], 
    'Volume': data[2]
  }
  return tickItem
}

const vuex_store = {
  state: {
    tickData : [],
    tickData_large : [],
    ob : [],
    chart : Data,
    code : 'HK.HSIMain',
    last_update : 'Updating',
  },
  mutations: {
    SOCKET_SERVER_NEWORDERBOOKDATA(state, newData) {
      // console.log('new Data from "server_newOrderBookData" event')
      // console.log(newData)
      state.ob = newData.data
    },
    SOCKET_SERVER_TEST(state){
      console.log('Test from server')
    },
    SOCKET_SERVER_NEWTICKDATA(state, newData){
      state.tickData = [manageNewTickData(newData), ...state.tickData]
    },
    SOCKET_SERVER_NEWKLINE(state, newData){
      // format: [timestamp, open, high, low, close, volume]
      console.log(newData)
      let e = JSON.parse(newData)[0]
      let timestamp = +moment(e.time_key)

      // exit if no data
      if (state.chart.chart.data.length == 0) return;
      var last1M = state.chart.chart.data.pop()

      // console.log("new k line Data!")
      console.log(+moment(timestamp))
      console.log(moment(timestamp).format('llll'))
      console.log(moment(last1M[0]).format('llll'))
      
      // if the time (in minutes) of the incoming data is same as last item

      if (moment(timestamp).minutes() == moment(last1M[0]).minutes()){
        state.chart.chart.data.push([
          timestamp, e.open, e.high, e.low, e.close, e.volume])
      }
      else{
        console.log('new 1M !')
        state.chart.chart.data.push(last1M)
        state.chart.chart.data.push([
          timestamp, e.open, e.high, e.low, e.close, e.volume])
      }
    },
    // Candle Stick Information
    SOCKET_SERVER_HISTORY1MDATA(state, newData){
      // console.log(newData)
      let processed = JSON.parse(newData).map(e => {
        // format: [timestamp, open, high, low, close, volume],
        return [
          +moment(e.time_key),
          e.open,
          e.high,
          e.low,
          e.close,
          e.volume
        ]
      });
      processed.pop()
      // console.log(processed[0])
      // console.log([...processed])

      state.chart.chart.data = [...processed]
    },






    add_tick_data(state, newData){
      let processed = newData.map((item, idx) => {
        return manageNewTickData(item)
      }).reverse();
      state.tickData = [...processed, ...state.tickData]
    },
    new_ob_json(state, newob){
      state.ob = newob
    },
    renew_1mData(state, data){
      let last_element = state.chart.chart.data.pop()
      last_element[5] += 10
      state.chart.chart.data.push(last_element)
      console.log(moment(last_element[0]).format('llll'))
      // state.chart.chart.data
    }
  },
  actions: { },
  modules: { }
}

export default new Vuex.Store(vuex_store)
