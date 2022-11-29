from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from modularCluster import *
import websocket

app = FastAPI(debug=True)

@app.get('/')
def read_root():
    return {"result" : "Successfully connnected to nikolaj's API."}

@app.get('/allocate/{type_gen}')
def generate_figure(type_gen: str, city_name:str, n: int, start: str, end: str):
    df = assign(city_name)
    timedf = timeFilter(df, start, end)
    if type_gen == "Heatmap":
        lon = timedf['Longitude'].to_list()
        lat = timedf['Latitude'].to_list()
        z = timedf['type'].to_list()
        return {"type" : "densitymapbox", "lon" : lon, "lat" : lat, "z" : z}
    elif type_gen == "Routes":
        centers, edges = analyze(timedf, n)
        longs = []
        lats = []
        for i in range(len(centers)):
            tempcen = centers[i]
            for j, k in edges[i]:
                x = tempcen[[j, k], 0]
                y = tempcen[[j, k], 1]
                longs.append(x.tolist())
                lats.append(y.tolist())
        return {"lats" : lats, "lons" : longs}


# @app.websocket('/')