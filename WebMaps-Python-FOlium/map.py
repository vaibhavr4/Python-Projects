import folium
import pandas


def color_mapper(elev):
    if(elev<1000):
        return 'green'
    elif(elev>=1000 and elev<3000):
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[42.346240, -71.094248],zoom_start=6,tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name='Volcanoes')
df = pandas.read_csv("Volcanoes.txt")

lat = list(df['LAT'])
lon = list(df['LON'])
elev = list(df['ELEV'])

fgp = folium.FeatureGroup(name="Population")

for lt,lg,el in zip(lat,lon,elev):

    fgv.add_child(folium.CircleMarker(location=[lt,lg],popup=str(el)+" m",fill_color=color_mapper(el),color='grey',fill=True,fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
                            style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
                                                     else 'orange' if 10000000<= x['properties']['POP2005'] < 20000000
                                                     else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
