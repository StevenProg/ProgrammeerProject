/*
Steven Schoenmaker 10777679
Sources
- https://bl.ocks.org/larsenmtl/e3b8b7c2ca4787f77d78f58d41c3da91
- https://bl.ocks.org/mbostock/3884955
- https://bl.ocks.org/mbostock/3883245
- http://bl.ocks.org/jhubley/17aa30fd98eb0cc7072f
*/

var marginMap = {top: 20, right: 20, bottom: 40, left: 20};
var widthMap = 700 - marginMap.left - marginMap.right;
var heightMap = 800 - marginMap.top - marginMap.bottom;

var margin = 50;
var map; 
var width = 1000 - margin * 2;
var height = 600 - margin * 2;
var previousViews = [];
var g;
var data = {};
var dataMapGlob;
var dataTopoGlob;
var dataLinesGlob;
var currentYear = 1996
// loads the 3 used json files
window.onload = function() {
    queue()
        .defer(d3.json, "data/eu.topo.json")
        .defer(d3.json, 'data/tempData.json')
        .defer(d3.json, 'data/ageTestData.json')
        .await(mainExecute);   
};

function mainExecute(error, dataTopo, dataTemp, dataAge) {
    if (error) {
        alert("Could not load data!");
        throw error;
    }
    // sets json input as variables
    dataTopoGlob = dataTopo;
    dataTempGlob = dataTemp;
    dataAgeGlob = dataAge;
    mapGraph(dataTopo, dataTempGlob);
    linesGraph(dataTempGlob);
    console.log(dataAge[1996]["Sweden"]);
    pieGraph(dataAge[1996]["Sweden"]);
    var selectedYear = d3.select("#slider1").attr("value");
    d3.select("#slider1-value").text(selectedYear);
    d3.select("#slider1").on("change", function(){
        var selectedYear = d3.select("#slider1").attr("value");
        d3.select("#slider1-value").text(selectedYear);})
};


function Class(str)
{
    var select = document.getElementById("dropdown-countries");
    var option = select.options[select.selectedIndex];
    updateMap(option.id)
    updateGraph(dataTempGlob, option.innerHTML)
    updatePie(dataAgeGlob[currentYear][option.innerHTML])
}