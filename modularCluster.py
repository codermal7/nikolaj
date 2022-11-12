# this .py file is intended to be the module that can be inserted into any code and can be used to generate desired output.
import numpy as np
import pandas as pd
from sklearn.cluster import *
import datetime as dt
import matplotlib.pyplot as plt
from sklearn import preprocessing as pp
import plotly.express as px

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

def genHeatMap():
    fig = px.density_mapbox(cleandf, lat='Latitude', lon='Longitude', z='type',
                        mapbox_style="stamen-terrain", radius=1, width=650, height=650)
    return fig

def timeFilter(start: str, end: str) -> pd.DataFrame:
    start = dt.datetime.strptime(start, '%H:%M:%S')
    end = dt.datetime.strptime(end, '%H:%M:%S')
    if (start < end):
        return cleandf.loc[(df['Time'] >= start) & (df['Time'] < end)]
    else:
        return cleandf.loc[(df['Time'] >= start) | (df['Time'] < end)]

def cluster(nCluster: int):
    nCluster = nCluster
    model = KMeans(n_clusters=nCluster)
    results = model.fit_predict(cleandf.loc(axis=1)['Latitude':'Longitude'])
    return results