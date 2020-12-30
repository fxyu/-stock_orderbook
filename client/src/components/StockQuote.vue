<template>
  <div>
    <div class="mx-4 mt-2">
      <h3 class="p-0 m-0">{{stock_quote.code}}</h3>
      <!-- <h5 class="p-0 m-0">{{stock_quote.data_date}}</h5> -->
    </div>
    <hr class="m-1">

    <b-container class="mx-2">
        <b-row>
            <b-col cols=4 order="6">
                <div class="data text-nowrap">{{stock_quote.low_price}}  —  {{stock_quote.high_price}}</div>
                <div class="data_title">Range</div>
            </b-col>
            <b-col cols=2>
                <div class="data">{{stock_quote.prev_close_price}}</div>
                <div class="data_title">Prev</div>
            </b-col>
            <b-col cols=2>
                <div class="data">{{stock_quote.open_price}}</div>
                <div class="data_title">Open</div>
            </b-col>
            <b-col cols=2>
                <div class="data">{{stock_quote.volume}}</div>
                <div class="data_title">Volume</div>
            </b-col>
        </b-row>
    </b-container>
    <hr class="m-1">

  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    name: 'StockQuote',
    computed: mapState([
        'stock_quote'
    ])
}
</script>

<style scoped>
.data{
  font-family: Trebuchet MS,roboto,ubuntu,sans-serif;
  font-size: 18px;
  color: #131722;
}

.data_title{
  font-size: 11px;
  line-height: 1;
  color: #787b86;
  letter-spacing: .4px;
  text-transform: uppercase;
}
</style>