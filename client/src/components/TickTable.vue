<template>
  <div class="m-0 p-0">
    <b-table hover :items="tickItems"></b-table>
  </div>
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
    };
  },
};
</script>

<style scoped></style>
