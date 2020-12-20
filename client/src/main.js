import Vue from 'vue'
import App from './App.vue'
import store from './store'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import VueSocketIOExt from 'vue-socket.io-extended';
import io from 'socket.io-client';

// const socket = io('http://socketserver.com:1923');
const socket = io('http://0.0.0.0:5005/');

Vue.use(VueSocketIOExt, socket, {store});

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

Vue.config.productionTip = false

new Vue({
  store,
  render: h => h(App)
}).$mount('#app')

