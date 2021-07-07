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
            toolTipContent: "<b>{label}:</b> {y} (#percent%)",
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
            toolTipContent: "<b>{label}:</b> {y} (#percent%)",
            dataPoints:d1,
        //         [
		// 	{ y: 67, label: "Inbox" },
		// 	{ y: 28, label: "Archives" },
		// 	{ y: 10, label: "Labels" },
		// 	{ y: 7, label: "Drafts"},
		// 	{ y: 15, label: "Trash"},
		// 	{ y: 6, label: "Spam"}
		// ],
        }]
    });
chart1.render();
chart2.render();
}