/*
Steven Schoenmaker 10777679
Sources
- https://bl.ocks.org/larsenmtl/e3b8b7c2ca4787f77d78f58d41c3da91
- https://bl.ocks.org/mbostock/3884955
- https://bl.ocks.org/mbostock/3883245
- http://bl.ocks.org/jhubley/17aa30fd98eb0cc7072f
- https://github.com/markmarkoh/datamaps/blob/master/README.md#using-custom-maps
*/

var eu_topo;
var previousProvince = [];
// var clickedProvince = ["Overijssel"];
var projection = d3.geo.mercator()
    .scale(1)
    .translate([0, 0]);
var path = d3.geo.path()
    .projection(projection);
var clicked = 0;
// create d3 tooltip to show on mouseover 
var mapTip = d3.tip()
    .attr("class", "tip")
    .attr("id", "mapTip")
    .offset([-10, 0])
    .html(function(currentCountry) {
        return "<text style='color:red'>"+ currentCountry +":</text><div>"});

// draws map of the netherlands including legend and year number 

function mapGraph(dataTopo) {

    function makeTitle() {
        d3.select('.map').select('g')
            .append('text')
            .attr('class', 'mapTitle')
            .text('Average, maximum and minimum sunhours measured per province in the Netherlands in 1996')
            .attr('text-anchor', 'middle')
            .attr('x', widthMap / 2 + 100)
            .attr('y', (heightMap / 2) - 355)
            .attr("font-size", "20px")
    };
    // sets maps element
    var map = d3.select(".map")
        .append("g")
        .attr("width", 1000)
        .attr("height", 500);

    // enable provinces to be colored
    var color = d3.scale.category10();

    // sets parameters to set json topo data in map element
    var l = topojson.feature(dataTopo, dataTopo.objects.europe).features[3],
        b = path.bounds(l),
        s = .2 / Math.max((b[1][0] - b[0][0]) / widthMap, (b[1][1] - b[0][1]) / heightMap),
        t = [-325, 6405];

    makeTitle();

    // create the map of the netherlands 
    projection.scale(500)
        .translate([400, 1000]);
    eu_topo = map.selectAll("path")
        .data(topojson.feature(dataTopo, dataTopo.objects.europe).features).enter()
        .append("path")
        .attr("class", function(d, i) { return d.properties.name})
        // only provinces of the Netherlands, not all parts (St Eustatius, Bonaire..)

        .attr("d", path)
        .style("stroke", "black")
        .style("fill", "green")
        // sets opacity, use a scale between 751 and 0 (instead of 1751 and 0)
        .attr("stroke-width", "1px")

    
};