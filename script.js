var margin ={top:20, right:30, bottom:30, left:40},
    width=960-margin.left - margin.right, 
    height=500-margin.top-margin.bottom;

// scale to ordinal because x axis is not numericalfreqfreq
var x = d3.scale.ordinal().rangeRoundBands([0, width], .1);

//scale to numerical value by height
var y = d3.scale.linear().range([height, 0]);

var chart = d3.select("#chart")  
              .append("svg")  //append svg element inside #chart
              .attr("width", width+(2*margin.left)+margin.right)    //set width
              .attr("height", height+margin.top+margin.bottom);  //set height
var xAxis = d3.svg.axis()
              .scale(x)
              .orient("bottom");  //orient bottom because x-axis will appear below the bars

var yAxis = d3.svg.axis()
              .scale(y)
              .orient("left");

d3.json("http://127.0.0.1:5000/histogram", function(error, data){
  console.log(data);
  
  jdata=JSON.parse(data);
  console.log(jdata);
  console.log(jdata[0].bin);
  console.log(jdata.length);
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
    //cols.push(jdata[i].count);
    //console.log(jdata[i].count);

  }
  console.log(jdata[0]);

 

  var x = d3.scale.ordinal()
    .domain(["A", "B", "C", "D", "E", "F"])
    .rangeRoundBands([0, width], .1);

  //x.domain(r.map(function(d){ return d.bin}));
  y.domain([0, 0.1, 0.2, 0.3, 0.4, 0.5]);
  
  var bar = chart.selectAll("g")
                    .data(data)
                  .enter()
                    .append("g")
                    .attr("transform", function(d, i){
                      console.log(d.bin)
                      return "translate("+x(d.bin)+", 0)";
                    });
  
  bar.append("rect")
      .attr("y", function(d) { 
        console.log(d.count)
        return y(d.count); 
      })
      .attr("x", function(d,i){
        return x.rangeBand()+(margin.left/2);
      })
      .attr("height", function(d) { 
        return height - y(d.count); 
      })
      .attr("width", x.rangeBand());  //set width base on range on ordinal data

  bar.append("text")
      .attr("x", x.rangeBand()+margin.left )
      .attr("y", function(d) { return y(d.count) -10; })
      .attr("dy", ".75em")
      .text(function(d) { return d.count; });
  
  chart.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate("+margin.left+","+ height+")")        
        .call(xAxis);
  
  chart.append("g")
        .attr("class", "y axis")
        .attr("transform", "translate("+margin.left+",0)")
        .call(yAxis)
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .text("Count");
});

function type(d) {
    var a=0;
    console.log(d)
    d.bin = +d.bin; // coerce to number
    return d;
  }