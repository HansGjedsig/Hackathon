#Importing libaries
import netCDF4 as nc
import numpy as np
import pandas as pd

#importing datasets
ds1 = nc.Dataset('temp_anomaly_ex1.nc')
ds2 = nc.Dataset('temp_anomaly_ex2.nc')
ds3 = nc.Dataset('temp_anomaly_ex3.nc')


lats = ds3.variables['lat'][:]
longs = ds3.variables['lat'][:]

X,Y = np.meshgrid(lats,longs)

predictions = []
for i in range(13):
    Tempdata = np.array(ds3.variables['tempanomaly'][1419-i,:,:])
    print(i)
    for x in range(4,7):
        for y in range(4,7):
            dist = np.array(1/np.sqrt((X-lats[y])**2+(Y-longs[x])**2)**4)
            dist[4:7,4:7]=0
            distweight = dist/dist.sum()
            Tempdata[x,y]=(Tempdata*distweight).sum()
    predictions.append(Tempdata)




print(predictions[0][4:7,4:7])







