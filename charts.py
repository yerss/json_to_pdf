from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.graphics.charts.barcharts import (
    VerticalBarChart
)
from reportlab.lib.formatters import DecimalFormatter


def getVetricalBarChart(taxes_int):
    values = []
    years = []
    font = 'Arial'
    for year in taxes_int:
        years.append(year)
        values.append(taxes_int[year])

    data = [values]
    chart = VerticalBarChart()
    chart.height = 180
    chart.width = 450
    chart.data = data

    chart.valueAxis.valueMin = 0
    chart.barWidth = 20
    chart.groupSpacing = 5
    chart.barLabels.fontName = font
    chart.barLabels.fontSize = 8
    chart.bars[0].fillColor = colors.cornflowerblue
    chart.barLabelFormat = '%d тг'
    chart.barLabels.nudge = 7

    chart.categoryAxis.labels.fontName = font
    chart.categoryAxis.labels.fontSize = 8
    chart.categoryAxis.categoryNames = years

    chart.valueAxis.labels.fontName = font
    chart.valueAxis.labels.fontSize = 8
    # chart.valueAxis.gridStrokeDashArray = strokeDashArray
    # chart.valueAxis.gridStrokeWidth = strokeWidth
    # chart.valueAxis.strokeDashArray = strokeDashArray
    # chart.valueAxis.strokeWidth = strokeWidth


    drawing = Drawing(300)
    drawing.add(chart)
    return drawing
