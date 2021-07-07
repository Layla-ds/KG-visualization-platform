Highcharts.theme = {
  // colors: ['#058DC7', '#50B432', '#ED561B', '#DDDF00', '#24CBE5', '#64E572',
  //          '#FF9655', '#FFF263', '#6AF9C4'],
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


var home1 = [['Event', 'Event', 51176],
 ['Event', 'Organisation', 48008],
 ['Event', 'Others', 5015],
 ['Event', 'Person', 132908],
 ['Event', 'Place', 48146],
 ['Event', 'Species', 13],
 ['Event', 'TimePeriod', 92],
 ['Event', 'Work', 1216],
 ['Organisation', 'Event', 48008],
 ['Organisation', 'Organisation', 501908],
 ['Organisation', 'Others', 169353],
 ['Organisation', 'Person', 1533144],
 ['Organisation', 'Place', 584568],
 ['Organisation', 'Species', 1016],
 ['Organisation', 'TimePeriod', 846724],
 ['Organisation', 'Work', 499153],
 ['Others', 'Event', 5015],
 ['Others', 'Organisation', 169353],
 ['Others', 'Others', 194020],
 ['Others', 'Person', 344508],
 ['Others', 'Place', 106866],
 ['Others', 'Species', 2782],
 ['Others', 'TimePeriod', 356],
 ['Others', 'Work', 382517],
 ['Person', 'Event', 132908],
 ['Person', 'Organisation', 1533144],
 ['Person', 'Others', 344508],
 ['Person', 'Person', 1264716],
 ['Person', 'Place', 2066443],
 ['Person', 'Species', 57055],
 ['Person', 'TimePeriod', 1006846],
 ['Person', 'Work', 1175704],
 ['Place', 'Event', 48146],
 ['Place', 'Organisation', 584568],
 ['Place', 'Others', 106866],
 ['Place', 'Person', 2066443],
 ['Place', 'Place', 3872734],
 ['Place', 'Species', 7816],
 ['Place', 'TimePeriod', 314],
 ['Place', 'Work', 123087],
 ['Species', 'Event', 13],
 ['Species', 'Organisation', 1016],
 ['Species', 'Others', 2782],
 ['Species', 'Person', 57055],
 ['Species', 'Place', 7816],
 ['Species', 'Species', 1186832],
 ['Species', 'TimePeriod', 14],
 ['Species', 'Work', 686],
 ['TimePeriod', 'Event', 92],
 ['TimePeriod', 'Organisation', 846724],
 ['TimePeriod', 'Others', 356],
 ['TimePeriod', 'Person', 1006846],
 ['TimePeriod', 'Place', 314],
 ['TimePeriod', 'Species', 14],
 ['TimePeriod', 'Work', 196],
 ['Work', 'Event', 1216],
 ['Work', 'Organisation', 499153],
 ['Work', 'Others', 382517],
 ['Work', 'Person', 1175704],
 ['Work', 'Place', 123087],
 ['Work', 'Species', 686],
 ['Work', 'TimePeriod', 196],
 ['Work', 'Work', 1017106]];

Highcharts.chart('chartContainer2', {
    title: {
        text: 'Relationship Chord Chart'
    },
    series: [{
        keys: ['from', 'to', 'weight'],
        data: home1,
        type: 'dependencywheel',
        name: 'Number of relationship from',
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

