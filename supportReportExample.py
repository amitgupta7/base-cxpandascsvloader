## python -m venv .venv
## source .venv/bin/activate
## pip install cxcsvtopandas
## python supportReportExample.py

import cxcsvtopandas.dataframeloader as dfl
root = '../jupyter-python-local-venv/.dataDir/'
fromDt = '2024-11-10'
toDt = '2024-12-10'
metricsArr = ['cpu_used','task_queue_length', 'memory_used']
daterange=[fromDt, toDt]
df = dfl.loadApplianceTimeSeriesData(root, metricsArr, daterange)
appliance_id='58e98e10-1b19-4c84-93c0-db2ad5903b80'
fig  = dfl.plotMetricsFacetForApplianceId(df, appliance_id).show()