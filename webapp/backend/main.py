from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from modularCluster import *

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
        longs = []
        lats = []
        centers, edges = analyze(timedf, n)
        for i in range(len(centers)):
            for j, k in edges[i]:
                x1 = float(centers[i][j][0])
                y1 = float(centers[i][j][1])
                x2 = float(centers[i][k][0])
                y2 = float(centers[i][k][1])
                longs.append(x1)
                longs.append(x2)
                lats.append(y1) 
                lats.append(y2)
        return {"longitudes" : list(longs), "latitudes" : list(lats)}

