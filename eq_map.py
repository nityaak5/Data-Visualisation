import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename='csv/data/eq.json'
with open(filename) as f:
    all_eq_data= json.load(f)

readable_file='csv/data/eq_readable.json'
with open(readable_file,'w') as f:
    json.dump(all_eq_data,f,indent=4)

eq_list= all_eq_data['features']

mags,lons,lats, hover=[],[],[],[]

for x in eq_list:
    magnitude= x['properties']['mag']
    mags.append(magnitude)

    lon=x['geometry']['coordinates'][0]
    lons.append(lon)

    lat=x['geometry']['coordinates'][1]
    lats.append(lat)
    
    title=x['properties']['title']
    hover.append(title)
    
# PLOTTING THE DATA
data=[
    {
    'type': 'scattergeo',
    'lon':lons, 
    'lat':lats,
    'text': hover,
    'marker': {
        'size': [5* mag for mag in mags],
        'color': mags,
        'colorscale':'Viridis',
        'colorbar': {'title': 'MAGNITUDE'},
        
    },
    }
    ]
my_layout= Layout(title='Global Earthquakes')

fig={
    'data': data,
    'layout': my_layout
}
offline.plot(fig,filename='eaartquake.html')