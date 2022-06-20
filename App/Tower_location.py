# -*- coding: utf-8 -*-
"""
Created on Wed May 11 15:33:47 2022

@author: João
"""

# Tower codes and geo location

from netCDF4 import Dataset
import numpy as np

# Reading the netcd file

data = Dataset("20170601.nc", 'r')

# Create an array with the towers code names

t_name = np.array(["tnw01", "tnw02", "tnw03", "tnw04", "tnw05", "tnw06", "tnw07", "tnw08", "tnw09", "tnw10", "tnw11", "tnw12", "tnw13", "tnw14", "tnw15", "tnw16", "tse01", "tse02", "tse04", "tse05", "tse06", "tse07", "tse08", "tse09", "tse10", "tse11", "tse12", "tse13", "rsw01", "rsw02", "rsw03", "rsw04", "rsw05", "rsw06", "rsw07", "rsw08", "rne01", "rne02", "rne03", "rne04", "rne06", "rne07", "v01", "v03", "v04", "v05", "v06", "v07", "Extreme_SW", "Extreme_NE"])

# Create empty numpy arrays that will contain the latitude and longitude for each tower

lat_n = np.empty(50)
lon_n = np.empty(50)

# Saving the coordinates on arrays
# The prints that appear in comments where used to learn which towers didn't have coordinates info, which will be introduced manually later

i = 0

for x in t_name:
    try:
        lat = data.variables['latitude_{}'.format(x)]
        lat_data = data.variables['latitude_{}'.format(x)][:]

        lon = data.variables['longitude_{}'.format(x)]
        lon_data = data.variables['longitude_{}'.format(x)][:]
    except KeyError:
        #print("The {} variable has no geo coordinates".format(x))
        continue
    except:
        #print("There is other problem with the {} variable".format(x))
        continue
    else:
        lat_n[i] = lat_data
        lon_n[i] = lon_data
    finally:
        i = i + 1

# Insert manually the coordinates of the towers that had missing info
# Data retrieved from Perdigao Site, data was in Degrees/Minutes/Seconds (DMS) format and was converted to Decimal Degrees (DD) to match the rest of the data

# tnw04 7°44′47.12″W 39°42′44.37″N

lat_n[3] = 39.712325
lon_n[3] = -7.746422

# tnw12 7°44′7.64″W 39°43′8.65″N

lat_n[11] = 39.719069
lon_n[11] = -7.735456

# tnw13 7°44′5.74″W 39°43′10.59″N

lat_n[12] = 39.719608
lon_n[12] = -7.734928

# tnw14 7°44′2.37″W 39°43′11.88″N

lat_n[13] = 39.719967
lon_n[13] = -7.733992

# tnw15 7°44′0.18″W 39°43′12.72″N

lat_n[14] = 39.720200
lon_n[14] = -7.733383

# tnw16 7°43′56.95″W 39°43′13.53″N

lat_n[15] = 39.720425
lon_n[15] = -7.732486

# tse05 7°44′31.24″W 39°42′24.82″N

lat_n[19] = 39.706894
lon_n[19] = -7.742011

# Extreme_SW 7°45′51.49″W 39°42′2.64″N

lat_n[48] = 39.700733
lon_n[48] = -7.764303

# Extreme_NE 7°43′44.56″W 39°43′23.41″N

lat_n[49] = 39.723169
lon_n[49] = -7.729044


# Map which heights the wind speed sonics are in each tower

# 2m, 4m, 6m, 8m, 10m, 12m, 20m, 30m, 40m, 60m, 80m, 100,

# Create array with sonics possible heights

height = np.array(["2", "4", "6", "8", "10", "20", "30", "40", "60", "80", "100"])
  
# Create an numpy array that will be filled with info on which sonics each tower has.
# This 2D array is initiallized with zeros "0"

m = np.zeros((11,50))

# This 'for loop' will check in each tower, if there are wind speed values for the different heights. If true, it will change the 'm' array from '0' to '1' in the correspondent position for the height in each tower
# In the end, the 'm' array contains boolean info on whether or not one specific tower has a sonic in a specific heihgt, for every tower, and every heights

j = 0

for a in t_name:
    
    i = 0
    
    for b in height:
        try:
            u = data.variables['u_{}m_{}'.format(b, a)][:]

        except KeyError:
            #print("The {} height is not present in tower {}".format(b, a))
            continue
        except:
            #print("There is other problem with the {} variable".format(a))
            continue
        else:
            m[i,j] = 1

        finally:
            i = i + 1
    j = j +1

# The 'prints' on the exceptions where used to test the construction of m

# Array with tower name code

t_n = t_name

# Array with tower heights

h = height

# function retrieves a boolean array containing sonics height for a specific tower
# input argument is a variable containing a string with tower code name, ex: 'tnw01'

def sonics_height (t):
    j = np.where(t_name == t)
    j = j[0]
    i = 0
    global result_bool_t
    result_bool_t = np.array(m[i,j], dtype='i4')
    i = 1
    while i < 11:
        result_bool_t = np.append(result_bool_t, m[i,j])
        i += 1
        continue
    return result_bool_t
    
# function retrieves a boolean array that says if there is a tower that has a sonic for the specified heigt
# input argument is a variable containing a string with sonic height, ex: '10'

def tower_available (d):
    i = np.where(height == d)
    i = i[0]
    j = 0
    global result_bool_h
    result_bool_h = np.array(m[i,j], dtype='i4')
    j = 1
    while j < 50:
        result_bool_h = np.append(result_bool_h, m[i,j])
        j += 1
        continue
    return result_bool_h

# This function retrieves a array containing the heights code names available for the selected tower (j)

def sonics_available_name (j):
    
    he = np.empty([11], dtype=int)

    v = 0
    i = 0
    while i < 11:
        if m[i,j] == 1:
        
            he[v] = height[i]
            v += 1
        
        i = i + 1
        continue
    
    global hei

    hei = he[0:v]
    return hei

# This function retrieves a array containing the towers code names available for the selected sonic height (j)

def tower_avaliable_name (i):
    
    to = t_name.copy()

    t = 0
    j = 0
    while j < 50:
        if m[i,j] == 1:
        
            to[t] = t_name[j]
            t += 1
        
        j = j + 1
        continue
    
    global tow
    tow = to[0:t]
    return tow