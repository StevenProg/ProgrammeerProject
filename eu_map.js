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
var clickedProvince = ["Sweden"];
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

function mapGraph(dataTopo, dataLines) {

    function makeTitle() {
        d3.select('.map').select('g')
            .append('text')
            .attr('class', 'mapTitle')
            // .text('European countries to choose from')
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
        // create mouse events 
        .call(mapTip)
        .on("mouseover", drawTooltip)
        .on("mouseout", removeTooltip)
        .on("click", onClick);
        // hoover over function, shows province name and hours of sun
        function drawTooltip() {
            // currentProvince = d3.select(this).attr("class");
            // hoursOfSun = d3.select(this).attr("sunHours");
            // mapTip.show(currentProvince, hoursOfSun);
            d3.select(this)
                .style("fill", "crimson")
        };
        function removeTooltip() {
            mapTip.hide()
            d3.select(this)
                .style("fill", "green");
        }

        function onClick() {
            console.log('this', this)
            currentProvinceClick = d3.select(this).attr("class");
            // prevent double date and data formatting


            // colours the clicked crimson and gives them a yellow edge, update the multiline
            if (clicked == 0) {
                map.selectAll("path").style("fill", "green").style("stroke", "none");
                d3.select(this)
                    .style("stroke", "yellow")
                    .style("stroke-width", "5px")
                    .style("fill", "crimson");
                updateGraph(dataLines, currentProvinceClick);
                updatePie(dataAgeGlob[currentYear][currentProvinceClick])

                clicked = 1;
            }

            // if the same province is clicked again, remove yellow lines
            else if (currentProvinceClick == previousProvince) {
                map.selectAll("path")
                .style("stroke", "black")
                .style("fill", "green")
                .style("stroke-width", "1px")
                clicked = 0;
            }

            // if a different province is clicked, with yellow lines being active, change them to the clicked province
            else {
                map.selectAll("path").style("fill", "green").style("stroke", "none");
                console.log(this)
                d3.select(this)
                    .style("stroke", "yellow")
                    .style("stroke-width", "5px")
                    .style("fill", "crimson");
                updateGraph(dataLines, currentProvinceClick);
                updatePie(dataAgeGlob[currentYear][currentProvinceClick])
 
                clicked = 1;
            }
            previousProvince = currentProvinceClick;
        }    
};

function updateMap(countryNumber) {
    var map = d3.select(".map");
    map.selectAll("path").style("fill", "green").style("stroke", "none");
    d3.select(map.selectAll("path")[0][countryNumber])
        .style("stroke", "yellow")
        .style("stroke-width", "5px")
};