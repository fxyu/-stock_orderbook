import Vue from 'vue'
import Vuex from 'vuex'

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
    code : 'HK.HSIMain',
    last_update : 'Updating',
  },
  mutations: {
    SOCKET_SERVER_NEWORDERBOOKDATA(state, newData) {
      console.log('new Data from "server_newOrderBookData" event')
    },
    SOCKET_SERVER_TEST(state){
      console.log('Test from server')
    },
    SOCKET_SERVER_NEWTICKDATA(state, newData){
      state.tickData = [manageNewTickData(newData), ...state.tickData]
    },
    add_tick_data(state, newData){
      let processed = newData.map((item, idx) => {
        return manageNewTickData(item)
      }).reverse();
      state.tickData = [...processed, ...state.tickData]
    },
    new_ob_json(state, newob){
      state.ob = newob
    }
  },
  actions: { },
  modules: { }
}

export default new Vuex.Store(vuex_store)
