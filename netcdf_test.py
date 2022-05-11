#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import glob
import netCDF4 as netcdf
import numpy as np
from datetime import datetime

os.chdir('/homes/up202001415/LIKE/DTU_Lidar/WS7')
nc = [f for f in glob.glob("*.nc")]

#for f in range(len(nc)):
f=0
ncfile = netcdf.Dataset(nc[f],'r')

time = np.array(ncfile['time'][:])
timeStr = [datetime.strptime(time[i], "%Y-%m-%dT%H:%M:%S.%fZ") for i in range(len(time))]
timeTup = [(i.year, i.month, i.day, i.hour, i.minute, i.second, i.microsecond) for i in timeL]
#dte_tp = np.array([excel_date((datesC[i])) for i in range(len(datesC))], dtype=np.float64)
dates = np.array(timeTup, dtype=np.int64)

# Get base date (convert time to seconds realative to base date)


vel=np.array(ncfile['VEL'][:])
x=np.array(ncfile['position_x'][:])
y=np.array(ncfile['position_y'][:])
z=np.array(ncfile['position_z'][:])
scan=np.array(ncfile['scan_type'][:]) # 5=RHI
cnr=np.array(ncfile['CNR'][:])
ele=np.array(ncfile['elevation_angle'][:])
eleS=np.array(ncfile['elevation_sweep'][:])
azi=np.array(ncfile['azimuth_angle'][:])
wid=np.array(ncfile['WIDTH'][:])
yaw=np.array(ncfile['yaw'][:])
pitch=np.array(ncfile['pitch'][:])
roll=np.array(ncfile['roll'][:])
ran=np.array(ncfile['range'][:])

print(vel)
