#Importing libaries
import netCDF4 as nc
import numpy as np
import pandas as pd

#importing datasets
ds1 = nc.Dataset('temp_anomaly_ex1.nc')
ds2 = nc.Dataset('temp_anomaly_ex2.nc')
ds3 = nc.Dataset('temp_anomaly_ex3.nc')

ex1 = True
ex2 = True
ex3 = True

if ex1:
    lats = ds1.variables['lat'][:]
    longs = ds1.variables['lat'][:]

    X,Y = np.meshgrid(lats,longs)
    predictions = []
    for i in range(12):
        Tempdata = np.array(ds1.variables['tempanomaly'][1408+i,:,:])
        print(i)
        x,y=5,5
        dist = np.array(1/np.sqrt((X-lats[y])**2+(Y-longs[x])**2)**4)
        dist[5,5]=0
        distweight = dist/dist.sum()
        Tempdata[x,y]=(Tempdata*distweight).sum()
        predictions.append(Tempdata)
    data_CSV = []
    for i in range(12):
        data_CSV.append(predictions[i][5,5])
    df= pd.DataFrame(data_CSV)
    df.to_csv("ex1.csv",index=False)

if ex2:
    lats = ds2.variables['lat'][:]
    longs = ds2.variables['lat'][:]

    X,Y = np.meshgrid(lats,longs)
    predictions = []
    for i in range(12):
        Tempdata = np.array(ds2.variables['tempanomaly'][1408+i,:,:])
        print(i)
        for x in range(5,7):
            for y in range(4,6):
                dist = np.array(1/np.sqrt((X-lats[y])**2+(Y-longs[x])**2)**4)
                dist[5:7,4:6]=0
                distweight = dist/dist.sum()
                Tempdata[x,y]=(Tempdata*distweight).sum()
        predictions.append(Tempdata)
    data_CSV = []
    for i in range(12):
        data_CSV.append(predictions[i][5,5])
    df= pd.DataFrame(data_CSV)
    df.to_csv("ex2.csv",index=False)

if ex3:
    lats = ds3.variables['lat'][:]
    longs = ds3.variables['lat'][:]

    X,Y = np.meshgrid(lats,longs)
    predictions = []
    for i in range(12):
        Tempdata = np.array(ds3.variables['tempanomaly'][1408+i,:,:])
        print(i)
        for x in range(4,7):
            for y in range(4,7):
                dist = np.array(1/np.sqrt((X-lats[y])**2+(Y-longs[x])**2)**4)
                dist[4:7,4:7]=0
                distweight = dist/dist.sum()
                Tempdata[x,y]=(Tempdata*distweight).sum()
        predictions.append(Tempdata)
    data_CSV = []
    for i in range(12):
        data_CSV.append(predictions[i][5,5])
    df= pd.DataFrame(data_CSV)
    df.to_csv("ex3.csv",index=False)
    













