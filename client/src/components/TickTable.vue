<template>
    <b-table 
      responsive 
      hover 
      :items="tickItems"
      :striped=true
      :small=true
    ></b-table>
</template>

<script>
import store from '../store'

export default {
  name: "TickTable",
  components: {

  },
  props: ['tickItems'],
  data() {
    return {
      small: true,
    };
  },
};
</script>

<style scoped>

</style>
