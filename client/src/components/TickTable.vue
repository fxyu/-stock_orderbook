<template>
  <div class="m-0 p-0">
        <div class="m-0 p-0" 
            style="border:1px solid; overflow-y: scroll; height: 200px">
            <div id="row_tempalte" class="row m-0 p-0">
                <div class="col-4">
                    Time
                </div>
                <div class="col-4">
                    Price
                </div>
                <div class="col-4">
                    Volumn
                </div>
            </div>
            <!-- For loop the entry -->
            <TickTableEntry/>
        </div>
    </div>
</template>

<script>
import TickTableEntry from './TickTableEntry'

export default {
    name: 'TickTable',
    components: {
        TickTableEntry
    }
}
</script>

<style scoped>

</style>