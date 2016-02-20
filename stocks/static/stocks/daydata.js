AmCharts.ready(function () {
    generateChartData();
});

var chartData = [];

function generateChartData() {
    $.ajax({
        url: "/stocks/"+ticker+"/getdaydata/",
        success: function (data) {
            chartData = jQuery.parseJSON(data.data)
            createStockChart();
        }
    });
}

function createStockChart() {
    var chart = new AmCharts.AmStockChart();


    // DATASET //////////////////////////////////////////
    var dataSet = new AmCharts.DataSet();
    dataSet.fieldMappings = [{
        fromField: "open",
        toField: "open"
    }, {
        fromField: "close",
        toField: "close"
    }, {
        fromField: "high",
        toField: "high"
    }, {
        fromField: "low",
        toField: "low"
    }, {
        fromField: "volume",
        toField: "volume"
    }];
    dataSet.color = "#7f8da9";
    dataSet.dataProvider = chartData;
    dataSet.title = "West Stock";
    dataSet.categoryField = "date";
    
    chart.dataSets = [dataSet];

    // PANELS ///////////////////////////////////////////
    var stockPanel = new AmCharts.StockPanel();
    stockPanel.title = "Close";
    stockPanel.showCategoryAxis = false;
    stockPanel.percentHeight = 70;

    var valueAxis = new AmCharts.ValueAxis();
    valueAxis.dashLength = 5;
    stockPanel.addValueAxis(valueAxis);

    stockPanel.categoryAxis.dashLength = 5;

    // graph of first stock panel
    var graph = new AmCharts.StockGraph();
    graph.type = "candlestick";
    graph.openField = "open";
    graph.closeField = "close";
    graph.highField = "high";
    graph.lowField = "low";
    graph.valueField = "close";
    graph.lineColor = "#7f8da9";
    graph.fillColors = "#7f8da9";
    graph.negativeLineColor = "#db4c3c";
    graph.negativeFillColors = "#db4c3c";
    graph.proCandlesticks = true;
    graph.fillAlphas = 1;
    graph.useDataSetColors = false;
    graph.comparable = true;
    graph.compareField = "close";
    graph.showBalloon = false;
    stockPanel.addStockGraph(graph);

    var stockLegend = new AmCharts.StockLegend();
    stockLegend.valueTextRegular = undefined;
    stockLegend.periodValueTextComparing = "[[percents.value.close]]%";
    stockPanel.stockLegend = stockLegend;

    var chartCursor = new AmCharts.ChartCursor();
    chartCursor.valueLineEnabled = true;
    chartCursor.valueLineAxis = valueAxis;
    stockPanel.chartCursor = chartCursor;



    chart.panels = [stockPanel];


    // OTHER SETTINGS ////////////////////////////////////
    var sbsettings = new AmCharts.ChartScrollbarSettings();
    sbsettings.graph = graph;
    sbsettings.graphType = "line";
    sbsettings.usePeriod = "DD";
    chart.chartScrollbarSettings = sbsettings;


    // PERIOD SELECTOR ///////////////////////////////////
    var periodSelector = new AmCharts.PeriodSelector();
    periodSelector.position = "bottom";
    periodSelector.periods = [{
        period: "DD",
        count: 1,
        label: "10 days"
    }, {
        period: "MM",
        selected: true,
        count: 20,
        label: "1 month"
    }, {
        period: "YYYY",
        count: 250,
        label: "1 year"
    }, {
        period: "YTD",
        label: "YTD"
    }, {
        period: "MAX",
        label: "MAX"
    }];
    chart.periodSelector = periodSelector;

    chart.write('chartdiv');
}