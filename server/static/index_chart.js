$(document).ready(function(){
    chart = c3.generate({
        bindto: '#chart',
        data: {
            json: [],
            keys: {
                x: 'price', // it's possible to specify 'x' when category axis
                value: ['bid','ask']
            },
            // columns : [

            // ],
            type: 'bar',
            labels: {
                format: function (v, id, i, j) { if (v>0) return v; }
            },
            groups: [
                ['bid','ask']
            ]
        },
        grid: {
            y: {
                lines: [{value:0}]
            }
        },
        axis: {
            x: {
                type: 'category',
                tick: {
                    rotate: 90,
                    multiline: false,
                }
            },
            y: {
                min : 0,
                max : 30,
                padding: {top:0, bottom:0}
            }

        },
        bar: {
            width: {
                ratio: 0.95
            }
        },
        transition: {
            duration: 30
        }
    });
})