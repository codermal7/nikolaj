# this .py file is intended to be the module that can be inserted into any code and can be used to generate desired output.
import numpy as np
import pandas as pd
from sklearn.cluster import *
import datetime as dt
from sklearn import preprocessing as pp
import plotly.express as px
from scipy.spatial import Delaunay
import warnings


warnings.filterwarnings("ignore")
df = pd.read_csv('datasets/crimedata2016.csv')
timelist = []
for i in range(len(df)):
    datetime_object = dt.datetime.strptime(df['Date'][i][-11:], '%I:%M:%S %p')
    timelist.append(datetime_object)
df['Time'] = timelist

lp = pp.LabelEncoder()
op = pp.OrdinalEncoder()
# creating a manual encoder for descriptions
cleandf = df.drop(['Date', 'X Coordinate', 'Y Coordinate', 'Beat', 'Year', 'FBI Code'], axis=1)
basicCrime = list(set(cleandf['Primary Type']))
basicCrime
primList = {'NON - CRIMINAL': 0, 'NON-CRIMINAL (SUBJECT SPECIFIED)': 0, 'NON-CRIMINAL': 0,
            'INTIMIDATION': 1, 'OBSCENITY': 1, 'OTHER OFFENSE': 1, 'PUBLIC INDECENCY': 1,
            'LIQUOR LAW VIOLATION': 2, 'PUBLIC PEACE VIOLATION': 2, 'CONCEALED CARRY LICENSE VIOLATION': 2,
            'PROSTITUTION': 3, 'GAMBLING': 3, 'INTERFERENCE WITH PUBLIC OFFICER': 3, 'STALKING': 3,
            'ARSON': 6, 'BURGLARY': 5, 'BATTERY': 2, 'ROBBERY': 5, 'SEX OFFENSE': 5, 'ASSAULT': 3,
            'THEFT': 4, 'DECEPTIVE PRACTICE': 5, 'CRIMINAL TRESPASS': 4, 'CRIMINAL DAMAGE': 4, 'WEAPONS VIOLATION' : 5,
            'MOTOR VEHICLE THEFT': 5, 'OFFENSE INVOLVING CHILDREN': 5, 'KIDNAPPING': 5, 'NARCOTICS': 5,
            'OTHER NARCOTIC VIOLATION' : 4,'HUMAN TRAFFICKING' : 6,'CRIM SEXUAL ASSAULT' : 6, 'HOMICIDE' : 6}
encodePrim = [primList[i] for i in cleandf['Primary Type']]
cleandf['desc'] = lp.fit_transform(cleandf['Description'])
cleandf['locdesc'] = lp.fit_transform(cleandf['Location Description'])
cleandf['type'] = encodePrim

def alpha_shape(points, alpha, only_outer=True):
    assert points.shape[0] > 3, "Need at least four points"
    def add_edge(edges, i, j):
        if (i, j) in edges or (j, i) in edges:
            assert (j, i) in edges, "Can't go twice over same directed edge right?"
            if only_outer:
                edges.remove((j, i))
            return
        edges.add((i, j))
    tri = Delaunay(points)
    edges = set()
    for ia, ib, ic in tri.vertices:
        pa = points[ia]
        pb = points[ib]
        pc = points[ic]
        a = np.sqrt((pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2)
        b = np.sqrt((pb[0] - pc[0]) ** 2 + (pb[1] - pc[1]) ** 2)
        c = np.sqrt((pc[0] - pa[0]) ** 2 + (pc[1] - pa[1]) ** 2)
        s = (a + b + c) / 2.0
        area = np.sqrt(s * (s - a) * (s - b) * (s - c))
        circum_r = a * b * c / (4.0 * area)
        if circum_r < alpha:
            add_edge(edges, ia, ib)
            add_edge(edges, ib, ic)
            add_edge(edges, ic, ia)
    return edges

def genHeatMap(df):
    fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='type',
                        mapbox_style="stamen-terrain", radius=1, width=650, height=650)
    return fig

def timeFilter(start: str, end: str) -> pd.DataFrame:
    start = dt.datetime.strptime(start, '%H:%M:%S')
    end = dt.datetime.strptime(end, '%H:%M:%S')
    if (start < end):
        return cleandf.loc[(df['Time'] >= start) & (df['Time'] < end)]
    else:
        return cleandf.loc[(df['Time'] >= start) | (df['Time'] < end)]

def cluster(nCluster: int, df: pd.DataFrame):
    nCluster = nCluster
    model = KMeans(n_clusters=nCluster)
    results = model.fit_predict(df.loc(axis=1)['Latitude':'Longitude'])
    return results

def analyze(nCluster: int, start: str, end: str):
    tdf = timeFilter(start, end)
    results = cluster(nCluster, tdf)
    tdf['cluster'] = results
    Hcenters = []
    Pedges = []
    hm = genHeatMap(tdf)
    for i in range(len(set(results))):
        fildf = tdf[tdf['cluster'] == i]
        nmod = KMeans(int(np.power(len(fildf), 0.25)))
        nmod.fit([[i, j] for i, j in zip(fildf['Longitude'], fildf['Latitude'])])
        centers = nmod.cluster_centers_
        try:
            edges = alpha_shape(centers, alpha=1, only_outer=True)
        except:
            continue
        Hcenters.append(centers)
        Pedges.append(edges)
    return (hm, Hcenters, Pedges)

if __name__ == '__main__':
    hm, centers, edges = analyze(85, '08:45:00', '17:35:00')
    print(len(centers))
    print(edges)