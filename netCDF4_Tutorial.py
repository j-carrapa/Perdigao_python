# -*- coding: utf-8 -*-
"""
Created on Tue May  3 16:20:02 2022

@author: João
"""


# NetCDF4 Tutorial

# Criar um objecto do tipo netCDF4 e grupos dentro dele

from netCDF4 import Dataset
rootgrp = Dataset("test.nc", "r", format="NETCDF4")
print(rootgrp.data_model)
rootgrp.close()

#mudando o argumento de "w" (write) para "r" (read) deixa de dar problema, não sei se dá para alterar coisas assim???

print()

rootgrp = Dataset("test.nc", "a")
fcstgrp = rootgrp.createGroup("forecasts")
anagrp = rootgrp.createGroup("analyses")
print (rootgrp.groups)

fcstgrp = rootgrp.createGroup("/forecasts/model1")
fcstgrp = rootgrp.createGroup("/forecasts/model2")

print()


def walktree(top):
     yield top.groups.values()
     for value in top.groups.values():
         yield from walktree(value)
print(rootgrp)

for children in walktree(rootgrp):
     for child in children:
         print(child)
         
print()

level = rootgrp.createDimension("level", None)
time = rootgrp.createDimension("time", None)
lat = rootgrp.createDimension("lat", 73)
lon = rootgrp.createDimension("lon", 144)

print(rootgrp.dimensions)


print()

print(len(lon))
print(lon.isunlimited())
print(time.isunlimited())

print()

for dimobj in rootgrp.dimensions.values():
     print(dimobj)
    

times = rootgrp.createVariable("time","f8",("time",))
levels = rootgrp.createVariable("level","i4",("level",))
latitudes = rootgrp.createVariable("lat","f4",("lat",))
longitudes = rootgrp.createVariable("lon","f4",("lon",))
# two dimensions unlimited
temp = rootgrp.createVariable("temp","f4",("time","level","lat","lon",))
temp.units = "K"    

print(temp)

print()

ftemp = rootgrp.createVariable("/forecasts/model1/temp","f4",("time","level","lat","lon",))

print(rootgrp["/forecasts/model1"])  # a Group instance

print(rootgrp["/forecasts/model1/temp"])

print()

print(rootgrp.variables)

import time
rootgrp.description = "bogus example script"
rootgrp.history = "Created " + time.ctime(time.time())
rootgrp.source = "netCDF4 python module tutorial"
latitudes.units = "degrees north"
longitudes.units = "degrees east"
levels.units = "hPa"
temp.units = "K"
times.units = "hours since 0001-01-01 00:00:00.0"
times.calendar = "gregorian"

print()
print('----------')
print()

for name in rootgrp.ncattrs():
     print("Global attr {} = {}".format(name, getattr(rootgrp, name)))


print()

print(rootgrp.__dict__)


