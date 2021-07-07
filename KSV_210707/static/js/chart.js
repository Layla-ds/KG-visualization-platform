window.onload = function () {
    var chart1 = new CanvasJS.Chart("chartContainer2", {
        animationEnabled: true,
        title:{
            text: "Relationship Distribution",
            fontSize:"15",
            margin: 5,
            verticalAlign: "top",
            horizontalAlign: "center"
        },
        data: [{
            type: "doughnut",
            startAngle: 60,
            //innerRadius: 60,
            indexLabelFontSize: 10,
            indexLabel: "{label} - #percent%",
            toolTipContent: "<b>{label}:</b> (#percent%)",
            dataPoints: d2,
        }]
    });
    var chart2 = new CanvasJS.Chart("chartContainer1", {
        animationEnabled: true,
        title:{
            text: "Neighbor Nodes Distribution",
            fontSize:"15",
            margin: 5,
            verticalAlign: "top",
            horizontalAlign: "center"
        },
        data: [{
            type: "doughnut",
            startAngle: 60,
            //innerRadius: 60,
            indexLabelFontSize: 10,
            indexLabel: "{label} - #percent%",
            toolTipContent: "<b>{label}:</b> (#percent%)",
            dataPoints:d1,
        }]
    });
chart1.render();
chart2.render();
}