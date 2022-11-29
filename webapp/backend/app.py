import numpy as np
import pandas as pd
from fastapi import FastAPI
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
        hm = genHeatMap(timedf)
        return {"Figure" : hm}
    elif type_gen == "Routes":
        longs = []
        lats = []
        centers, edges = analyze(n, start, end)
        for i in range(len(centers)):
            for j, k in edges[i]:
                longs.append(centers[i][j])
                lats.append(centers[i][k])
        return {"longitudes" : longs, "latitudes" : lats}