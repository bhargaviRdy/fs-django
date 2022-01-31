from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
# Include the `fusioncharts.py` file that contains functions to embed the charts.

from .fusioncharts import FusionCharts
from .fusioncharts import FusionTable
from .fusioncharts import TimeSeries
import requests

def myFirstChart(request):

  data = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/line-chart-with-time-axis-data.json').text
  schema = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/line-chart-with-time-axis-schema.json').text

  fusionTable = FusionTable(schema, data)
  timeSeries = TimeSeries(fusionTable)

  timeSeries.AddAttribute('chart', '{"timeSpread": {"unit":"month"}}')
  timeSeries.AddAttribute('caption', '{"text":"Sales Analysis"}')
  timeSeries.AddAttribute('subcaption', '{"text":"Grocery"}')
  timeSeries.AddAttribute('yaxis', '[{"plot":{"value":"Grocery Sales Value"},"format":{"prefix":"$"},"title":"Sale Value"}]')


  # Create an object for the chart using the FusionCharts class constructor
  fcChart = FusionCharts("timeseries", "ex1", 700, 450, "myFirstchart-container", "json", timeSeries)

  #adding events to add realtimeDate
  fcChart.addEvent('rendered', "addRealTimeData")
  fcChart.addEvent('disposed', "dispose")
  
  # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
  return  render(request, 'index.html', {'output' : fcChart.render()})