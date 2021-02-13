import Vue from 'vue'
import App from './App.vue'
import store from './store'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import VueSocketIOExt from 'vue-socket.io-extended';
import io from 'socket.io-client';
import router from './router'

// const socket = io('http://socketserver.com:1923');
const socket = io('http://localhost:5005/');

Vue.use(VueSocketIOExt, socket, {store});

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')

