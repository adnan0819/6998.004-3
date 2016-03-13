var w = 600;
var h = 250;
var dataset;
var jdata;
var xScale; 
var yScale; 

d3.json("http://127.0.0.1:5000/histogram", function(error, data){
  console.log(data);
  
  jdata=JSON.parse(data);
  console.log(jdata);
//  console.log(jdata[0].bin);
 // console.log(jdata.length);
  counting=[];

  var rows=[];
  var cols=[];

  for (i=0;i<jdata.length;i++){
    //console.log(jdata[i].bin);
    //rows.push(i);
    if(jdata[i].bin==="food") jdata[i].bin=0;
    if(jdata[i].bin==="fire") jdata[i].bin=1;
    if(jdata[i].bin==="earthquake") jdata[i].bin=2;
    if(jdata[i].bin==="l4l") jdata[i].bin=3;
    if(jdata[i].bin==="selfie") jdata[i].bin=4;
    if(jdata[i].bin==="rain") jdata[i].bin=5;
    if(jdata[i].bin==="storm") jdata[i].bin=6;
    if(jdata[i].bin==="snow") jdata[i].bin=7;
    if(jdata[i].bin==="rain") jdata[i].bin=8;
    if(jdata[i].bin==="flood") jdata[i].bin=9;
    if(jdata[i].bin==="hurricane") jdata[i].bin=10;
}
dataset=jdata;


    



xScale = d3.scale.ordinal()
				.domain(d3.range(dataset.length))
				.rangeRoundBands([0, w], 0.05); 

yScale = d3.scale.linear()
				.domain([0, d3.max(dataset, function(d) {return d.count;})])
				.range([0, h]);
			


 console.log(dataset);
var bin = function(d) {
	return d.bin;
};

//Create SVG element
var svg = d3.select("body")
			.append("svg")
			.attr("width", w)
			.attr("height", h);

//Create bars
svg.selectAll("rect")
   .data(dataset, bin)
   .enter()
   .append("rect")
   .attr("x", function(d, i) {
//   	console.log(xScale);
		return xScale(i);
   })
   .attr("y", function(d) {
		return h - yScale(d.count);
   })
   .attr("width", xScale.rangeBand())
   .attr("height", function(d) {
		return yScale(d.count);
   })
   .attr("fill", function(d) {
		return "rgb(0, 0, " + (d.count * 10) + ")";
   })

	//Tooltip
	.on("mouseover", function(d) {
		//Get this bar's x/y counts, then augment for the tooltip
		var xPosition = parseFloat(d3.select(this).attr("x")) + xScale.rangeBand() / 2;
		var yPosition = parseFloat(d3.select(this).attr("y")) + 14;
		
		//Update Tooltip Position & count
		d3.select("#tooltip")
			.style("left", xPosition + "px")
			.style("top", yPosition + "px")
			.select("#count")
			.text(d.count);
		d3.select("#tooltip").classed("hidden", false)
	})
	.on("mouseout", function() {
		//Remove the tooltip
		d3.select("#tooltip").classed("hidden", true);
	})	;

//Create labels
svg.selectAll("text")
   .data(dataset, bin)
   .enter()
   .append("text")
   .text(function(d) {
		return d.count;
   })
   .attr("text-anchor", "middle")
  
   .attr("x", function(d, i) {
   	console.log(xScale("Here"));
   		console.log(xScale(i));
		return xScale(i) + xScale.rangeBand() / 2;
   })

   .attr("y", function(d) {
		return h - yScale(d.count) + 14;
   })
    .attr('class', jdata.bin)
   .attr("font-family", "sans-serif") 
   .attr("font-size", "11px")
   .attr("fill", "white");


   
var sortOrder = false;
var sortBars = function () {
    sortOrder = !sortOrder;
    
    sortItems = function (a, b) {
        if (sortOrder) {
            return a.count - b.count;
        }
        return b.count - a.count;
    };

    svg.selectAll("rect")
        .sort(sortItems)
        .transition()
        .delay(function (d, i) {
        return i * 50;
    })
        .duration(1000)
        .attr("x", function (d, i) {
        return xScale(i);
    });

    svg.selectAll('text')
        .sort(sortItems)
        .transition()
        .delay(function (d, i) {
        return i * 50;
    })
        .duration(1000)
        .text(function (d) {
        return d.count;
    })
        .attr("text-anchor", "middle")
        .attr("x", function (d, i) {
        return xScale(i) + xScale.rangeBand() / 2;
    })
        .attr("y", function (d) {
        return h - yScale(d.count) + 14;
    });
};
// Add the onclick callback to the button
d3.select("#sort").on("click", sortBars);
d3.select("#reset").on("click", reset);
function randomSort() {

	
	svg.selectAll("rect")
        .sort(sortItems)
        .transition()
        .delay(function (d, i) {
        return i * 50;
    })
        .duration(1000)
        .attr("x", function (d, i) {
        return xScale(i);
    });

    svg.selectAll('text')
        .sort(sortItems)
        .transition()
        .delay(function (d, i) {
        return i * 50;
    })
        .duration(1000)
        .text(function (d) {
        return d.count;
    })
        .attr("text-anchor", "middle")
        .attr("x", function (d, i) {
        return xScale(i) + xScale.rangeBand() / 2;
    })
        .attr("y", function (d) {
        return h - yScale(d.count) + 14;
    });
}
function reset() {
	svg.selectAll("rect")
		.sort(function(a, b){
			return a.bin - b.bin;
		})
		.transition()
        .delay(function (d, i) {
        return i * 50;
		})
        .duration(1000)
        .attr("x", function (d, i) {
        return xScale(i);
		});
		
	svg.selectAll('text')
        .sort(function(a, b){
			return a.bin - b.bin;
		})
        .transition()
        .delay(function (d, i) {
        return i * 50;
    })
        .duration(1000)
        .text(function (d) {
        return d.count;
    })
        .attr("text-anchor", "middle")
        .attr("x", function (d, i) {
        return xScale(i) + xScale.rangeBand() / 2;
    })
        .attr("y", function (d) {
        return h - yScale(d.count) + 4;
    });
    };
});