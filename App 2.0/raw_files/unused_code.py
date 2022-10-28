# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:44:12 2022

@author: Joao
"""

# unused code

import pandas as pd
import numpy as np
import math

# tower location

#df_coord = coordinates_file_creation()

#file_name = r'C:\Users\Baba\Desktop\João\Tese\Python\Teste_1\Perdigao_python\App 2.0\sonics_coordinates.xls'
#sheet =  'Sheet1'

#df_coord = pd.read_excel(io=file_name, sheet_name=sheet)
'''
x = 'tnw01'
y = 2

df_coord = pd.read_csv ('sonics_coordinates.csv', usecols= ['sonic','Z','lat','lon'])
sonic_array = df_coord.iloc[:,0]
coord_index_array = np.array(-1)



a = 0

if a == 0:
    
    name = '{}.{}m'.format(x,y)
    i = 0

    for sonic in sonic_array:
        if name in sonic:
            
            coord_index_array = np.append(coord_index_array, i)
            a = 1
        i +=1


x = 'tse02'
y = 10


if a == 1:
    
    name = '{}.{}m'.format(x,y)
    i = 0

    for sonic in sonic_array:
        if name in sonic:
            
            coord_index_array = np.append(coord_index_array, i)
        i +=1


coord_index_array = np.unique(coord_index_array)
coord_index_array = coord_index_array[1:]

df_sonics = df_coord.loc[coord_index_array]

df_sonics.to_csv('selected_sonics_coordinates.csv')

df_sonics.to_excel('selected_sonics_coordinates.xls')

'''

# Correction of sonic coordinates

#file_name = r'C:\Users\Baba\Desktop\João\Tese\sonics_coord.xlsx'
#sheet =  'Sheet1'
'''
df = pd.read_excel(io=file_name, sheet_name=sheet)

lk = np.arange(0,185)

for i in lk:
    
    if i > 98:
        
        name = df.iat[i,0]
        name = "!" + name[4:]
        df.iat[i,0] = name
        i+=1
    
    if i < 99 and i>8:
        
        name = df.iat[i,0]
        name = "!" + name[3:]
        df.iat[i,0] = name
        i+=1
        
    if i < 9:
        
        name = df.iat[i,0]
        name = "!" + name[2:]
        df.iat[i,0] = name
        i+=1
    
    


df.to_csv('sonics_coord_corrected.csv', index=False)

df.to_excel('sonics_coord_corrected.xls', index=False)

df.to_csv('sonics_coord_corrected.dat', sep = " ", index=False)

'''

'''
lat_lon = lat_lon_towers()
lat = lat_lon[0]
lon = lat_lon[1]

data = Dataset("20170601.nc", 'r')
#print(data.variables.keys())

print(data['latitude_tnw01'])

x = 'tnw02'

lat_data = data.variables['latitude_{}'.format(x)][:]
lon_data = data.variables['longitude_{}'.format(x)][:]

#print(tentativa1.data_model)


#print(tentativa1.dimensions)


#print(tentativa1)

#print(tentativa1.variables)

#print(tentativa1)

#print(tentativa1.groups)
'''

#df_24 = pd.read_csv('rmse_24h_table_20170514_20170515_0-18h')


# Graph functions


def save2(df_rmse, path_pf, rmse_var, a_name, b_name, c_name, tower_p):
    
    if rmse_var == 0:
        
        name = a_name
    
    if rmse_var == 1:
        
        name = b_name
        
    if rmse_var == 2:
        
        name = c_name
        
    date_index = path_pf.find('201')
    s = path_pf[date_index:date_index+23]
    
    direc = r'C:\Users\Baba\Desktop\João\Tese\Python\Teste_1\Perdigao_python\App 2.0\tables'
    
    df_rmse.to_csv(os.path.join(r'{}'.format(direc),'rmse_{}_{}_table_last_24h_{}.csv'.format(name,tower_p,s)))
    df_rmse.to_excel(os.path.join(r'{}'.format(direc),'rmse_{}_{}_table_last_24h_{}.xls'.format(name,tower_p,s)))
    df_rmse = df_rmse.to_numpy()
    np.savetxt(os.path.join(r'{}'.format(direc),'rmse_{}_{}_table_last_24h_{}.txt'.format(name,tower_p,s)), df_rmse, fmt = "%.4f")
    
    
def coordinates_file_creation_first_try():
    
    df = pd.read_csv(r'C:\Users\Baba\Desktop\João\Tese\sonics_coord_corrected.csv') 

    data = df.iloc[:,0]
    lat_lon = lat_lon_towers()
    lat = lat_lon[0]
    lon = lat_lon[1]
    t_name = towers_name()

    latit = np.zeros(185)
    longit = np.zeros(185)

    i=0
    j= 0

    for tower in t_name:
        
        for st in data:
            
            if tower in st:
                latit[i] = lat[j]
                longit[i] = lon[j]
                i +=1
                
            
            continue
        
        j+=1
        continue

        
    df['lat'] = latit
    df['lon'] = longit
    
    df = df[['lat', 'lon', 'Z', 'sonic']]

    df.to_csv('sonics_coordinates.csv', index=False)

    #df.to_excel('sonics_coordinates.xls')
    
    df.to_csv('sonics_coordinates.dat', sep = " ", index=False)

    
    return df

#df = pd.read_csv(r'C:/Users/Baba/Desktop/João/Tese/Python/Teste_1/Perdigao_python/App 2.0/rmse_24h_table_20170514_20170515_0-18h.csv', index_col=[0])

#num = df.to_numpy()
#num = np.loadtxt("num2.txt")

#df2 = df.copy()


'''
vh = df.iloc[:,0]

vh_num = vh.to_numpy()

i=0

for a in vh_num:
    
    if math.isnan(a):
        
        vh_num[i] = 1
    i +=1
    
vh_max_index_col = np.argmax(vh_num)
vh_min = np.where(vh_num == np.amin(vh_num))
'''
'''
di = df.iloc[:,2]

dir_num = di.to_numpy()

i=0

for a in dir_num:
    
    if math.isnan(a):
        
        dir_num[i] = 75
    i +=1
    
di_max_index_col = np.argmax(dir_num)
di_min = np.where(dir_num == np.amin(dir_num))
'''
'''
tk = df.iloc[:,4]

tk_num = tk.to_numpy()

i=0

for a in tk_num:
    
    if math.isnan(a):
        
        tk_num[i] = 0.5
    i +=1
    
tk_max_index_col = np.argmax(tk_num)
tk_min = np.where(tk_num == np.amin(tk_num))
'''

#num = num.round(decimals=4)

#df = df.round(decimals=4)

#df.to_csv(r'C:/Users/Baba/Desktop/João/Tese/Python/Teste_1/Perdigao_python/App 2.0/rmse_24h_table_20170514_20170515_0-18h.txt', sep=' & ', line_terminator=' \\\\\n')

#np.savetxt("num2.txt", num, fmt='%1.4f')

#df_vh = pd.read_csv(r'C:/Users/Baba/Desktop/João/Tese/Python/Teste_1/Perdigao_python/App 2.0/rmse_6h_vh_table_20170514_20170515_0-18h.csv', index_col=[0])
#df_dir = pd.read_csv(r'C:/Users/Baba/Desktop/João/Tese/Python/Teste_1/Perdigao_python/App 2.0/rmse_6h_dir_table_20170514_20170515_0-18h.csv', index_col=[0])
#df_tke = pd.read_csv(r'C:/Users/Baba/Desktop/João/Tese/Python/Teste_1/Perdigao_python/App 2.0/rmse_6h_tke_table_20170514_20170515_0-18h.csv', index_col=[0])

#num_vh = df_vh.to_numpy()
#num_dir = df_dir.to_numpy()
#num_tke = df_tke.to_numpy()

#num_vh = num_vh.round(decimals=4)
#num_dir = num_dir.round(decimals=4)
#num_tke = num_tke.round(decimals=4)

#df_vh = df_vh.round(decimals=4)
#df_dir = df_dir.round(decimals=4)
#df_tke = df_tke.round(decimals=4)

#df_vh.to_csv(r'C:/Users/Baba/Desktop/João/Tese/Python/Teste_1/Perdigao_python/App 2.0/rmse_6h_vh_table_20170514_20170515_0-18h.txt', sep='&', line_terminator=' \\\\\n')
#df_dir.to_csv(r'C:/Users/Baba/Desktop/João/Tese/Python/Teste_1/Perdigao_python/App 2.0/rmse_6h_dir_table_20170514_20170515_0-18h.txt', sep='&', line_terminator=' \\\\\n')
#df_tke.to_csv(r'C:/Users/Baba/Desktop/João/Tese/Python/Teste_1/Perdigao_python/App 2.0/rmse_6h_tke_table_20170514_20170515_0-18h.txt', sep='&', line_terminator=' \\\\\n')

#np.savetxt("num_vh.txt", num_vh, delimiter=' & ', fmt='%1.4f', newline=' \\\\\n')
#np.savetxt("num_dir.txt", num_dir, delimiter=' & ', fmt='%1.4f', newline=' \\\\\n')
#np.savetxt("num_tke.txt", num_tke, delimiter=' & ', fmt='%1.4f', newline=' \\\\\n')


#df = pd.read_csv(r'C:/Users/Baba/Desktop/João/Tese/Python/Teste_1/Perdigao_python/App 2.0/tables/rmse_vh_tnw07_table_last_24h_20170514_20170515_0-18h.csv', index_col=[0])

#num3 = df.to_numpy()

#df = df.round(decimals=4)

#num3 = num3.round(decimals=4)
#num30 = num3[0]
#num4 = ('%.2f' %num30)

#df.to_csv(r'C:/Users/Baba/Desktop/João/Tese/Python/Teste_1/Perdigao_python/App 2.0/hourly.txt', sep='&', line_terminator=' \\\\\n')


#df = pd.read_csv(r'C:/Users/Baba/Desktop/João/Tese/Python/Teste_1/Perdigao_python/App 2.0/tables/rmse_vh_tnw09_table_last_24h_20170514_20170515_0-18h.csv', index_col=[0])
#df = df.round(decimals=4)
#df.to_csv(r'C:/Users/Baba/Desktop/João/Tese/Python/Teste_1/Perdigao_python/App 2.0/hourlytnw09.txt', sep='&', line_terminator=' \\\\\n')

#import requests
#import time
#from netCDF4 import Dataset
#import matplotlib.pyplot as plt
#from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
#url = 'http://windsptds.fe.up.pt/thredds/fileServer/flux/NCAR-EOL%20Quality%20Controlled%205-minute%20ISFS%20surface%20flux%20data,%20geographic%20coordinate,%20tilt%20corrected/isfs_qc_tiltcor_20170514.nc'

#r = requests.get(url)

#open('20170514.nc','wb').write(r.content)

def extract_time_save_experience_perdigao ():
    
    data = Dataset('20170514.nc','r')

    x = 'tnw01'
    y = '10'

    u = data.variables['u_{}m_{}'.format(y,x)]
    v = data.variables['v_{}m_{}'.format(y,x)]
    w = data.variables['w_{}m_{}'.format(y,x)]

    uu = data.variables['u_u__{}m_{}'.format(y,x)]
    vv = data.variables['v_v__{}m_{}'.format(y,x)]
    ww = data.variables['w_w__{}m_{}'.format(y,x)]

    uv = data.variables['u_v__{}m_{}'.format(y,x)]
    uw = data.variables['u_w__{}m_{}'.format(y,x)]
    vw = data.variables['v_w__{}m_{}'.format(y,x)]

    direc = data.variables['dir_{}m_{}'.format(y,x)]
    spd = data.variables['spd_{}m_{}'.format(y,x)]

    basetime = data.variables['base_time']
    reltime = data.variables['time']

    starting_time = data.variables['time'].units[14:29] + '2:30'
    ending_time = data.variables['time'].units[14:25] + '23:57:30'

    time_range = pd.date_range(start=starting_time, end=ending_time, periods=288)

    df = pd.DataFrame(0, columns= ['basetime', 'time', 'u', 'v', 'w', 'vh', 'dir', 'uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index=time_range)

    dt = np.arange(0, data.variables['time'].size)

    for time_index in dt:
        
        df.iloc[time_index] = basetime[time_index], reltime[time_index], u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]
    
    return df


# time save experience comparison tools

def turbulence_5min_ventos (dfc):
    '''Takes the data frame containing the variables retrieved from the sonic (pandas Data Frame), Returns the same data frame with three new columns with calculated values of turbulence kinetic energy, turbulence intensity and turbulence intensity from horizontal components for data of 5 min period (pandas Data Frame)'''
    dt = np.arange(0, dfc.size/16, dtype=int)

    i = 0
    for a in dt:
        
        if i == 0:
            
            u = dfc.iat[a,3]
            v = dfc.iat[a,4]
            w = dfc.iat[a,5]
            
            uu = dfc.iat[a,13]
            vv = dfc.iat[a,14]
            ww = dfc.iat[a,15]
            
            tke = (1/2)*(uu+vv+ww)
            ti = np.sqrt(tke*(2/3))/np.sqrt(u*u+v*v+w*w)
            tih = np.sqrt((1/3)*(uu+vv))/np.sqrt(u*u+v*v)
            
            tke_arr = np.array(tke, dtype='float')
            ti_arr = np.array(ti, dtype='float')
            tih_arr = np.array(tih, dtype='float')
            
            i = 1

        else:
            u = dfc.iat[a,3]
            v = dfc.iat[a,4]
            w = dfc.iat[a,5]
            
            uu = dfc.iat[a,13]
            vv = dfc.iat[a,14]
            ww = dfc.iat[a,15]
            
            tke = (1/2)*(uu+vv+ww)
            ti = np.sqrt(tke*(2/3))/np.sqrt(u*u+v*v+w*w)
            tih = np.sqrt((1/3)*(uu+vv))/np.sqrt(u*u+v*v)
            
            temp = np.array(tke, dtype='float')
            temp2 = np.array(ti, dtype='float')
            temp3 = np.array(tih, dtype='float')
            
            tke_arr = np.append(tke_arr, [temp])
            ti_arr = np.append(ti_arr, [temp2])
            tih_arr = np.append(tih_arr, [temp3])

    dfc['tke'] = tke_arr.tolist()
    dfc['ti'] = ti_arr.tolist()
    dfc['tih'] = tih_arr.tolist()

    return dfc


def graph_qualquer():
    
    df_perdigao = pd.read_csv(r'C:/Users/Baba/Desktop/João/Tese/Python/Teste_1/Perdigao_python/App 2.0/data_pf/2m_tnw01_20170514_20170515_0-18h_P-5min.csv', index_col=[0])

    k = int((df_perdigao.iat[1,1] - df_perdigao.iat[0,1])/2)

    k = int((df_perdigao.iat[1, 1] - df_perdigao.iat[0, 1])/2)

    dt = np.arange(0, len(df_perdigao.index), dtype=int)

    for a in dt:
        
        df_perdigao.iat[a, 1] = df_perdigao.iat[a, 1] + k


    perdigao_data = df_perdigao.to_numpy()

    ventos_data = np.genfromtxt(r'C:\Users\Baba\Desktop\João\Tese\Simulações\all_sonics_v2\all_sonics_v2\af_series00001.plt',  skip_header=7)

    df_ventos = pd.DataFrame(ventos_data, columns = ['seconds', 'TP', 'N^2', 'u', 'v', 'w', 'vh', 'dir', 'wdeg', 'shear', 'te_v', 'ti_v', 'tih_v', 'uu', 'vv', 'ww'])

    df_ventos = turbulence_5min_ventos(df_ventos)

    ventos_data = df_ventos.to_numpy()

    ventos_data = ventos_data[1:]

    highlight=1

    a_name = 'vh'
    b_name = 'dir'
    c_name = 'tke'

    a1 = 5
    b1 = 6
    c1 = 13

    a2 = 6
    b2 = 7
    c2 = 16


    # Plot formatting:
    plt.rcParams['font.family'] = 'sans-serif'
    #plt.rcParams.update({'font.sans-serif':'Helvetica'})
    SMALL_SIZE = 10
    MEDIUM_SIZE = 12
    ANOT_SIZE = SMALL_SIZE - 2
    NUMBER_SIZE = SMALL_SIZE
    plt.rc('font', size=SMALL_SIZE)        # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)   # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    shadecolor = 'lavenderblush'

    x = perdigao_data[:, 1]
    xlim_l = int(x[0])
    xlim_r = int(x[-1])

    #

    fig = plt.figure()  # an empty figure with no axes

    resolution_value = 200

    plt.rcParams["figure.figsize"] = (12,6)

    plt.rcParams['figure.dpi'] = resolution_value

    t_title = 'tnw01'
    h_title = '2m'

    fig, ax_lst = plt.subplots(3, 1)  # a figure with a 2x2 grid of Axes

    fig.suptitle('Tower {} at {} height'.format(t_title, h_title), fontsize=16)

    #subtitle = 'Wind Speed Components  U,V,W'

    # A

    a_ylabel = 'Wind Speed (m s$^{-1}$)'

    axa = plt.subplot(311)

    axa.set_ylabel(r'{}'.format(a_ylabel))
    #axa.set_ylim(0, 8.5)
    axa.set_xlim(xlim_l, xlim_r)
    axa.xaxis.set_tick_params(labelbottom=False)
    axa.grid(color='k', linestyle='-', linewidth=0.7, alpha=0.2)
    axa.yaxis.set_major_locator(MultipleLocator(2))
    axa.yaxis.set_minor_locator(MultipleLocator(0.4))
    axa.tick_params(which='major', length=7, width=1, direction='in', top=True, right=True)
    axa.tick_params(which='minor', length=3, width=1, direction='in', top=True, right=True)

    x = perdigao_data[:, 1]
    y1 = perdigao_data[:,a1]

    y2 = ventos_data[:,a2]

    plt.plot(x, y1, 'teal', label='Measurements')
    plt.plot(x, y2, 'orangered', label='Simulation')

    if highlight == 1:
        
        axa.fill_between(x, 0, 1, where=x > 18*3600, color=shadecolor, alpha=0.5, transform=axa.get_xaxis_transform())
        


    #leg = axa.legend(loc='upper left', frameon=False)
    leg = axa.legend(frameon=False)

    # B

    b_ylabel = 'Direction ($\degree$)'

    axb = plt.subplot(312, sharex=axa)
    axb.set_ylabel(r'{}'.format(b_ylabel))
    # axb.xaxis.set_visible(False)
    axb.set_xticklabels([])
    axb.xaxis.set_tick_params(labelbottom=False)
    axb.set_ylim(0, 360)
    # plt.setp(axb.get_xticklabels(), visible=False)
    axb.grid(color='k', linestyle='-', linewidth=0.7, alpha=0.2)
    axb.yaxis.set_major_locator(MultipleLocator(90))
    axb.yaxis.set_minor_locator(MultipleLocator(18))
    axb.tick_params(which='major', length=7, width=1, direction='in', top=True, right=True)
    axb.tick_params(which='minor', length=3, width=1, direction='in', top=True, right=True)

    y3 = perdigao_data[:,b1]

    y4 = ventos_data[:,b2]

    plt.plot(x, y3, 'teal', x, y4, 'orangered')

    if highlight == 1:
        
        axb.fill_between(x, 0, 1, where=x > 18*3600, color=shadecolor, alpha=0.5, transform=axb.get_xaxis_transform())
        

    # C

    c_ylabel = 'TKE (m$^2$ s$^{-2}$)'

    axc = plt.subplot(313, sharex=axa)
    axc.set_ylabel(r'{}'.format(c_ylabel))
    axc.set_xlabel(r'Time')
    # plt.setp(axc.get_xticklabels(), visible=False)
    axc.grid(color='k', linestyle='-', linewidth=0.7, alpha=0.2)
    #axc.set_ylim(-0.1, 2.1)
    axc.yaxis.set_major_locator(MultipleLocator(1))
    axc.yaxis.set_minor_locator(MultipleLocator(0.2))
    axc.tick_params(which='major', length=7, width=1, direction='in', top=True, right=True)
    axc.tick_params(which='minor', length=3, width=1, direction='in', top=True, right=True)
    xtcks = np.arange(0*3600, 43*3600, 3600*6)
    lbl = ['0:00','6:00', '12:00', '18:00', '00:00', '6:00', '12:00', '18:00']
    axc.annotate('May 14', (0.09, 0.05), xycoords='figure fraction', fontsize=ANOT_SIZE, color='k')
    axc.annotate('May 15', (0.528, 0.05), xycoords='figure fraction', fontsize=ANOT_SIZE, color='k')

    axc.set_xticks(ticks=xtcks)
    axc.set_xticklabels(lbl)
    axc.annotate('a)', (.03, .82), xycoords='figure fraction', fontsize=SMALL_SIZE, color='k')
    axc.annotate('b)', (.03, .57), xycoords='figure fraction', fontsize=SMALL_SIZE, color='k')
    axc.annotate('c)', (.03, .3), xycoords='figure fraction', fontsize=SMALL_SIZE, color='k')

    y5 = perdigao_data[:,c1]

    y6 = ventos_data[:,c2]

    plt.plot(x, y5, 'teal', x, y6, 'orangered')

    if highlight == 1:
        
        axc.fill_between(x, 0, 1, where=x > 18*3600, color=shadecolor, alpha=0.5, transform=axc.get_xaxis_transform())
        


    #plt.safig(r'C:\Users\Baba\Desktop\João\Tese\Python\Teste_1\Perdigao_python\App 2.0\graphs\tnw01_2m_vh_dir_tke_experience.png', format="png", dpi=resolution_value)


    #plt.savefig(os.path.join(r'{}'.format(direc_graphs),"{}_{}_{}_{}_{}.png".format(t_title,h_title,a_name,b_name,c_name)), format="png", dpi=resolution_value)














