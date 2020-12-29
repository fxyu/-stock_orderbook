<template>
  <b-card no-body class="p-0 m-0 ">
      <b-card-title class="pt-4 pl-2 ml-2 pr-4 title">{{title[0]}}</b-card-title>
      <b-card-sub-title class="mb-0 pl-2 ml-2 subtitle">{{title[1]}}</b-card-sub-title>
      <hr class="p-0 mt-3 mb-0"/>
      <b-container class="pl-4 pr-4 pt-2 vol_table overflow-auto" style="height: 350px">
        <!-- <b-row class="mb-1">
          <b-col cols="3" class="p-0 text-left">Time</b-col>
          <b-col cols="3" class="text-left">Price</b-col>
          <b-col cols="6" class="text-right">Vol.</b-col>
        </b-row> -->
        <b-row v-for="(item, index) in tickItems" :key="index" class="mb-1">
          <b-col col class="pl-2 text-left">{{ item.Time }}</b-col>
          <b-col col class="text-left">{{ item.Price }}</b-col>
          <b-col col class="text-right">{{ item.Volume }}</b-col>
        </b-row>
      </b-container>
  </b-card>
</template>

<script>
import store from "../store";

export default {
  name: "TickTableV2",
  components: {},
  props: ["tickItems","title"],
  data() {
    return {
      // small: true,
    };
  },
};
</script>

<style scoped>
.title {
  font-weight: bold;
  color: purple;
}

.subtitle{
  font-weight: bold;
}

.vol_table {
  font-weight: bold;
  font-size: 14px;
  font-family: 微軟正黑體修正, 微軟正黑體修正2, 微軟正黑體, "Microsoft JhengHei",
    Arial;
}


/* b-col{
  padding: 0px;
} */


::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #f1f1f1; 
}
 
/* Handle */
::-webkit-scrollbar-thumb {
  background: #888; 
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555; 
}
</style>
