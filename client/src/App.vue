<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <Charts />
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Charts from './components/Charts'

export default {
  name: 'App',
  components: {
    Charts
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
