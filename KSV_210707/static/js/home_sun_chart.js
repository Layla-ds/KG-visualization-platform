Highcharts.theme = {
    chart: {
	  backgroundColor: '#ffffff',
    },

    title: {
      style: {
          color: '#000',
          font: 'bold 16px "Trebuchet MS", Verdana, sans-serif'
      }
  },
    lang: {
        thousandsSep: ','
    }
}
Highcharts.setOptions(Highcharts.theme);

// Splice in transparent for the center circle
Highcharts.getOptions().colors.splice(0, 0, 'transparent');


Highcharts.chart('chartContainer1', {
    chart: {
        height: '100%',
         // float: top,
    },

    title: {
        text: 'Label Type Sun Chart',
        floating: true,
        margin:0
    },
    series: [{
        type: "sunburst",
        data: d11,
        allowDrillToNode: true,
        cursor: 'pointer',
        dataLabels: {
            /**
             * A custom formatter that returns the name only if the inner arc
             * is longer than a certain pixel size, so the shape has place for
             * the label.
             */
            formatter: function () {
                var shape = this.point.node.shapeArgs;

                var innerArcFraction = (shape.end - shape.start) / (2 * Math.PI);
                var perimeter = 2 * Math.PI * shape.innerR;

                var innerArcPixels = innerArcFraction * perimeter;

                if (innerArcPixels > 16) {
                    return this.point.name;
                }
            }
        },
        levels: [{
            level: 2,
            colorByPoint: true,
            dataLabels: {
                rotationMode: 'parallel'
            }
        },
        {
            level: 3,
            colorVariation: {
                key: 'brightness',
                to: 0.5
            }
        }, {
            level: 4,
            colorVariation: {
                key: 'brightness',
                to: 0.5
            }
        }, {
            level: 5,
            colorVariation: {
                key: 'brightness',
                to: 0.5
            }
        }, {
            level: 6,
            colorVariation: {
                key: 'brightness',
                to: 0.5
            }
        }]
    }],
    tooltip: {
        pointFormat: 'Number of <b>{point.name}</b>：<b>{point.value}</b>'
    },
    credits: {
                enabled:false
    },
    exporting: {
                enabled:false
    },
     // colors: ['#ffffff','#058DC7', '#50B432', '#ED561B', '#DDDF00', '#24CBE5', '#64E572', '#FF9655', '#FFF263', '#6AF9C4','#60418F', '#ED561B', '#EF8E19','#43C565','#179587','#7697DE','#B362A5','#58C1DA'],
    // colors: ['#ffffff','#60418F', '#ED561B', '#EF8E19','#43C565','#179587','#7697DE','#B362A5','#58C1DA'],
     //可以规定颜色了
});