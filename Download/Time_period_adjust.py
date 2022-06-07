# -*- coding: utf-8 -*-
"""
Created on Fri May 27 15:29:56 2022

@author: Joao
"""

# Time period adjust

'''----- PART 4 ----------'''
# - Ask for the period time of the sample, multiples of 5 min: 5, 10, 15, 20, 30min or 1h

period_val = input("Type one of the options for time period in min:\n5, 10, 15, 20, 30 or 60:")

period_conv = int(period_val)/5


# Creating an empty pandas dataframe
starting_time = data.variables['time'].units[14:29]+ '2:30'
ending_time = data.variables['time'].units[14:25]+ '23:57:30'
time_range = pd.date_range(start= starting_time, end= ending_time, periods= 288)

df = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)
df1 = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)
df2 = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)
dfmean = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)




# Create a numpy array with the size of the time variable

dt = np.arange(0, data.variables['time'].size)





if period_conv == 2:
    p = 1
    for time_index in dt:
        df.iloc[time_index] = basetime[time_index], reltime[time_index] + 86400*n, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]
        if p//2 == 1:
            df1.iloc[time_index] = basetime[time_index], reltime[time_index] + 86400*n, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]
            p += 1
        if p//2 == 0:
            df2.iloc[time_index] = basetime[time_index], reltime[time_index] + 86400*n, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]
            p += 1
            dfmean.iloc[time_index] = df1[time_index,0], (df1[time_index,1] + df1[time_index,1])/2 + 86400*n#, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]
            




if period_conv == 2:
    while i < 288:
        dfmean