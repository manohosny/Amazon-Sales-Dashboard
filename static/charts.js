// Function to fetch data and update the pie chart
 function fetchDataAndUpdatePieChart(apiEndpoint, chartId) {
        fetch(apiEndpoint)
            .then(response => response.json())
            .then(data => {
                createAndUpdatePieChart(chartId, data);
            })
            .catch(error => console.error('Error:', error));
    }

    function createAndUpdatePieChart(chartId, data) {
        am5.ready(function () {
            var root = am5.Root.new(chartId);
            root.setThemes([am5themes_Animated.new(root)]);

            var chart = root.container.children.push(
                am5percent.PieChart.new(root, {
                    endAngle: 270
                })
            );

            var series = chart.series.push(
                am5percent.PieSeries.new(root, {
                    valueField: "product_count",
                    categoryField: "main_category",
                    endAngle: 270
                })
            );

            series.states.create("hidden", {
                endAngle: -90
            });
            series.get('colors').set('colors',[
                am5.color("#4d4376"),
                am5.color("#ef894a"),
                am5.color("#ffba42"),
                am5.color("#fee19c"),
            // Add more colors as needed
            ]);
            series.labels.template.set('visible', false);
            series.data.setAll(data);
            legend.data.setAll(data);
            legend.appear(1000, 100);

            series.appear(1000, 100);
        });
    }

    // Call the function to fetch data and update the pie chart
// Function to fetch data and update the bar chart
function fetchDataAndUpdateBarChart(apiEndpoint, valueField, categoryField, chartId) {
        fetch(apiEndpoint)
            .then(response => response.json())
            .then(data => {
                createAndUpdateBarChart(chartId, data, valueField, categoryField);
            })
            .catch(error => console.error('Error:', error));
    }

    function createAndUpdateBarChart(chartId, data, valueField, categoryField) {
    am5.ready(function () {
        var root = am5.Root.new(chartId);
        root.setThemes([am5themes_Animated.new(root)]);

        var chart = root.container.children.push(am5xy.XYChart.new(root, {
            panX: true,
            panY: true,
            wheelX: "panX",
            wheelY: "zoomX",
            pinchZoomX: true,
            paddingLeft: 0,
            paddingRight: 1
        }));

        var cursor = chart.set("cursor", am5xy.XYCursor.new(root, {}));
        cursor.lineY.set("visible", false);

        var xRenderer = am5xy.AxisRendererX.new(root, {
            strokeOpacity: 0.1,
            grid: {
                template: {
                    visible: false // Set visible to false to hide the grids
                }
            }
        });

        var xAxis = chart.xAxes.push(am5xy.CategoryAxis.new(root, {
            maxDeviation: 0.3,
            categoryField: categoryField,
            renderer: xRenderer,
            tooltip: am5.Tooltip.new(root, {})
        }));

        var yRenderer = am5xy.AxisRendererY.new(root, {
            minGridDistance: 30,
            grid: {
                template: {
                    visible: false // Set visible to false to hide the grids
                }
            }
        });

        yRenderer.labels.template.setAll({
            rotation: 0,
            centerX: am5.p50,
            paddingBottom: 15
        });

        var yAxis = chart.yAxes.push(am5xy.ValueAxis.new(root, {
            maxDeviation: 0.3,
            renderer: yRenderer
        }));

        var series = chart.series.push(am5xy.ColumnSeries.new(root, {
            name: "Series 1",
            xAxis: xAxis,
            yAxis: yAxis,
            valueYField: valueField,
            sequencedInterpolation: true,
            categoryXField: categoryField,
            tooltip: am5.Tooltip.new(root, {
                labelText: "{valueY}"
            })
        }));
        var colors = [
            am5.color("#4d4376"),
            am5.color("#ef894a"),
            am5.color("#ffba42"),
            am5.color("#fee19c"),
            // Add more colors as needed
        ];

        series.columns.template.setAll({ cornerRadiusTL: 5, cornerRadiusTR: 5, strokeOpacity: 0 });
        series.columns.template.adapters.add("fill", function (fill, target) {
            return colors[series.columns.indexOf(target)];
        });

        series.columns.template.adapters.add("stroke", function (stroke, target) {
            return colors[series.columns.indexOf(target)];
        });

        xAxis.data.setAll(data);
        series.data.setAll(data);

        series.appear(1000);
        chart.appear(1000, 100);
    });
}



    // Call the function to fetch data and update the first bar chart
fetchDataAndUpdateBarChart('/get-barchart', 'total_ratings', 'main_category', 'bar-chart');
fetchDataAndUpdateBarChart('/get-barchart/Electronics', 'total_ratings', 'main_category', 'bar-chart1')
fetchDataAndUpdateBarChart('/get-barchart/Home&Kitchen', 'total_ratings', 'main_category', 'bar-chart2')
fetchDataAndUpdateBarChart('/get-barchart/Computers&Accessories', 'total_ratings', 'main_category', 'bar-chart3')
fetchDataAndUpdateBarChart('/get-barchart/OfficeProducts', 'total_ratings', 'main_category', 'bar-chart4')
// Call the function to fetch data and update the second bar chart
fetchDataAndUpdateBarChart('/get-bar', 'total_sales', 'main_category', 'bar');
fetchDataAndUpdateBarChart('/get-bar/Electronics', 'total_sales', 'main_category', 'bar1');
fetchDataAndUpdateBarChart('/get-bar/Home&Kitchen', 'total_sales', 'main_category', 'bar2');
fetchDataAndUpdateBarChart('/get-bar/Computers&Accessories', 'total_sales', 'main_category', 'bar3');
fetchDataAndUpdateBarChart('/get-bar/OfficeProducts', 'total_sales', 'main_category', 'bar4');

fetchDataAndUpdatePieChart('/get-piechart', 'pie-chart');
fetchDataAndUpdatePieChart('/get-piechart/Electronics', 'pie-chart1');
fetchDataAndUpdatePieChart('/get-piechart/Home&Kitchen', 'pie-chart2');
fetchDataAndUpdatePieChart('/get-piechart/Computers&Accessories', 'pie-chart3');
fetchDataAndUpdatePieChart('/get-piechart/OfficeProducts', 'pie-chart4');

