import csv
import plotly.express as px
import pandas as pd

filename = 'world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    lons, lats, brightnesses = [], [], []
    for row in reader:
        lons.append(float(row[0]))
        lats.append(float(row[1]))
        brightnesses.append(float(row[2]))
    
data = pd.DataFrame(
    data=zip(lons, lats, brightnesses), columns=['经度', '纬度', '亮度']
)
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球火灾亮度散点图',
    size='亮度',
    size_max=10,
    color='亮度',
    hover_name='亮度',
)
fig.write_html('global_fires.html')
fig.show()