Highcharts.theme = {
colors: ['#EF8E19','#60418F','#58C1DA', '#ED561B', '#43C565','#179587','#7697DE','#B362A5'],
  chart: {
	  backgroundColor: '#ffffff',
  },
  title: {
      style: {
          color: '#000',
          font: 'bold 16px "Trebuchet MS", Verdana, sans-serif'
      }
  }}
Highcharts.setOptions(Highcharts.theme);

Highcharts.chart('chartContainer22', {
    title: {
        text: 'Neighbor Chord Chart'
    },
    series: [{
        keys: ['from', 'to', 'weight'],
        data: d22,
        type: 'dependencywheel',
        name: 'Neighbor Nodes',
        dataLabels: {
            color: '#333',
            textPath: {
                enabled: true,
                attributes: {
                    dy: 5
                }
            },
            distance: 10
        },
        size: '95%'
    }],

     credits: {
                enabled:false
    },
    exporting: {
                enabled:false
    }
});