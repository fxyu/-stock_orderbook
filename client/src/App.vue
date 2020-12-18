<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <Charts />
    <p>Hello</p>
    <TickTable />
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Charts from './components/Charts'
import TickTable from './components/TickTable'

export default {
  name: 'App',
  components: {
    Charts,
    TickTable,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

@import './assets/c3.min.css';
</style>
