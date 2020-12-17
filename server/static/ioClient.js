var socket = null

$(document).ready(function () {
    // var url = 'http://localhost';
    var url = window.location.origin;
    var port = '5000';
    // console.log(url + ':' + port)
    console.log(url)
    socket = io.connect(url);
    
    socket.on('connect', function () {
        console.log('Connected!')
        console.log('getHistory!')
        socket.emit('client_history',null,function(history){
            console.log(history)
            history.forEach(function(newData, idx){
                newTickDataHandler(newData)
            })
        })
    })

    socket.on('server_newOrderBookData', function(newData) {
        // console.log(newData)
        $('#code').text(newData.code)
        $('#last_update').text(newData.time)

        ob = newData.data

        if ($('#check_auto').is(":checked")){
            low_price = Math.round(ob[0].price / 5 ) * 5 - 10
            high_price = low_price + 40  
        }
        else{
            low_price = $('#range_low').val()
            high_price = $('#range_high').val()

            if (high_price-low_price > 300){
                low_price = Math.round(ob[0].price / 5 ) * 5 - 10
                high_price = low_price + 40  
            }
        }
        

        var tmp1 = []
        for(var n=low_price; n<ob[0].price; n++ ){
            tmp1.push({
                price : n,
                ask : 0,
                bid : 0
            })
        }

        var tmp2 = []
        for(var n=ob[ob.length-1].price + 1; n<=high_price; n++ ){
            tmp2.push({
                price : n,
                ask : 0,
                bid : 0
            })
        }

        ob = tmp1.concat(ob).concat(tmp2)

        chart.load({
            json: ob,
            keys: {
                x: 'price',
                value: ['ask', 'bid']
            }
        });

        $('.c3 .c3-axis-x .tick text').each(function(){
            $(this).css('stroke', '');
            if (!($(this).text()%10)){
                $(this).css('stroke', 'red');
            } 
            if (!($(this).text()%20)){
                $(this).css('stroke', 'black');
            } 
        });
    })

    //server_newTickData
    socket.on('server_newTickData', function(newData) {
        newTickDataHandler(newData)
    })

    function newTickDataHandler(newData){
        data = newData[0].split(' ')

        $new_template = $('#row_tempalte').clone().removeAttr('id')
        $allDiv = $new_template.find('div')
        data.forEach((val, idx) => {
            $allDiv.eq(idx).text(val)
        })
        $('#row_tempalte').after($new_template)

        // console.log(newData)
        //tickData
        if(newData[1] >= 50){
            $new_template.addClass('redColor')
            $('#row_tempalte_large').after($new_template)
        }
        else if(newData[1] >= 10){
            $new_template.addClass('yellowColor')
            $('#row_tempalte_large').after($new_template)
        }
        else if(newData[1] >= 5){
            $new_template.addClass('brownColor')
            $('#row_tempalte_large').after($new_template)
        }
    }

    setInterval(function(){ 
        $('div.m-0').eq(0).find('div.row:gt(50)').remove()
    }, 5000);


    socket.on('server_test', function(){
        console.log('Test from server')
    })

    btn_range_group = [-20,-10,10,20]
    $("#range_btn_group").find('button').each(function(idx,val){
        $(this).click(function(){
            $('#range_low').val(parseInt($('#range_low').val())+btn_range_group[idx])
            $('#range_high').val(parseInt($('#range_high').val())+btn_range_group[idx])
        })
    })

    $("#btn_start").click(function(){
        $.ajax({url: "start", success: function(result){
            console.log(result)
        }});        
    })

    $("#btn_stop").click(function(){
        $.ajax({url: "stop", success: function(result){
            console.log(result)
        }});        
    })

    $("#btn_test").click(function(){
        $.ajax({url: "test", success: function(result){
            console.log(result)
        }});        
    })
}); 