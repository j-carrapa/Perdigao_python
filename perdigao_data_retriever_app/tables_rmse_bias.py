# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:38:28 2022

@author: Joao
"""

# RMSE, BIAS tables

import graph_functions as gf
import numpy as np
import pandas as pd
import tower_location as tl
import os.path

def rmse_bias_2 (pf_2d_array,data,v_name,period):
    
    i = df.columns.get_loc(v_name)
    j = df_ventos.columns.get_loc(v_name)
    
    pf_num_rows = len(pf_2d_array)
    
    if period == 24:
        
        exp = pf_2d_array[-24*12:,i]
        sim = data[-24*12:,j]
        
        if v_name == 'dir':
            
            err, mse, rmse, bias = gf.rmse_f(exp, sim, True)
            
        else:
            
            err, mse, rmse, bias = gf.rmse_f(exp, sim)
        
    else:
        
        nhour = int(pf_num_rows/period/12)
        err = np.zeros(nhour)
        mse = np.zeros(nhour)
        rmse = np.zeros(nhour)
        bias = np.zeros(nhour)
        
        for k in range(nhour):
                
            exp = pf_2d_array[k*period*12:k*period*12+period*12,i]
            sim = data[k*period*12:k*period*12+period*12,j]
                
            if v_name == 'dir':

                err[k], mse[k], rmse[k], bias[k] = gf.rmse_f(exp, sim, True)
                
            else:
                
                err[k], mse[k], rmse[k], bias[k] = gf.rmse_f(exp, sim)
                
    return rmse, bias

#t_name = np.array(["tnw01", "tnw02", "tnw03", "tnw04", "tnw05", "tnw06", "tnw07", "tnw08", "tnw09", "tnw10", "tnw11", "tnw12", "tnw13", "tnw14", "tnw15", "tnw16", "tse01", "tse02", "tse04", "tse05", "tse06", "tse07", "tse08", "tse09", "tse10", "tse11", "tse12", "tse13", "rsw01", "rsw02", "rsw03", "rsw04", "rsw05", "rsw06", "rsw07", "rsw08", "rne01", "rne02", "rne03", "rne04", "rne06", "rne07", "v01", "v03", "v04", "v05", "v06", "v07", "Extreme_SW", "Extreme_NE"])
towers = np.array(["v01", "v03", "v04", "v05", "v06", "v07"])#"v01", "v03", "v04", "v05", "v06", "v07"])#, "tse05", "tse06", "tse07", "tse08", "tse09", "tse10", "tse11", "tse12", "tse13"])#"tnw01", "tnw02", "tnw03", "tnw04", "tnw05"])#, "tnw06", "tnw07", "tnw08", "tnw09", "tnw10"])#

#towers = t_name
#tower_p = 'tnw05'
period = 6

if period == 24:
    
    #df_24 = pd.DataFrame(columns = ['sonic', 'rmse_24h_vh', 'bias_24h_vh', 'rmse_24h_dir', 'bias_24h_dir', 'rmse_24h_tke', 'bias_24h_tke'])

    df_24 = pd.read_csv('rmse_24h_table_20170514_20170515_0-18h.csv', index_col=False)

if period == 6:
    
    #df_6_vh = pd.DataFrame(columns = ['sonic', 'rmse_0-6h_vh', 'bias_0-6h_vh', 'rmse_6-12h_vh', 'bias_6-12h_vh', 'rmse_12-18h_vh', 'bias_12-18h_vh', 'rmse_18-24h_vh', 'bias_18-24h_vh'])
    #df_6_dir = pd.DataFrame(columns = ['sonic', 'rmse_0-6h_dir', 'bias_0-6h_dir', 'rmse_6-12h_dir', 'bias_6-12h_dir', 'rmse_12-18h_dir', 'bias_12-18h_dir', 'rmse_18-24h_dir', 'bias_18-24h_dir'])
    #df_6_tke = pd.DataFrame(columns = ['sonic', 'rmse_0-6h_tke', 'bias_0-6h_tke', 'rmse_6-12h_tke', 'bias_6-12h_tke', 'rmse_12-18h_tke', 'bias_12-18h_tke', 'rmse_18-24h_tke', 'bias_18-24h_tke'])

    df_6_vh = pd.read_csv('rmse_6h_vh_table_20170514_20170515_0-18h.csv', index_col=False)
    df_6_dir = pd.read_csv('rmse_6h_dir_table_20170514_20170515_0-18h.csv', index_col=False)
    df_6_tke = pd.read_csv('rmse_6h_tke_table_20170514_20170515_0-18h.csv', index_col=False)
    
for tower_p in towers:
    
    j = tl.tower_index_pos(tower_p)

    heights = tl.sonics_available_name(j)

    direc_pf = r'C:\Users\Baba\Desktop\João\Tese\Python\Teste_1\Perdigao_python\App 2.0\data_pf'
    path_ventos_sonics_coord = r'C:\Users\Baba\Desktop\João\Tese\Python\Teste_1\Perdigao_python\App 2.0\sonics_coord_est_nor_z.csv'
    direc_sim = r'C:\Users\Baba\Desktop\João\Tese'

    a_name = "vh"
    b_name = "dir"
    c_name = "tke"

    nvars = np.array(a_name)
    nvars = np.append(a_name, [b_name, c_name])


    sta = 0
    he = 0

    for height in heights:
        
        ''' Perdigao File '''

        path_pf = r'{}\{}m_{}_20170514_20170515_0-18h_P-5min.csv'.format(direc_pf,height,tower_p)

        df, pf_2d_array, pf_num_rows = gf.df_perdigao_file(path_pf)

        ''' VENTOS File V2'''

        df_ventos, data = gf.df_ventos_file(tower_p,height,direc_sim,path_ventos_sonics_coord)
        
        sonic = '{}.{}m'.format(tower_p, height)
        
        if sta ==0:
            nh = int(pf_num_rows/period/12)
            var = len(nvars)
            h = len(heights)

            rmse_s = np.zeros((nh,var,h))
            bias_s = np.zeros((nh,var,h))
            rmse_24 = np.zeros((var,h))
            bias_24 = np.zeros((var,h))
            
            sta=1

        va = 0

        for v_name in nvars:
            
            rmse, bias = rmse_bias_2(pf_2d_array,data,v_name,period)
            
            if period == 24:
                
                rmse_24[va,he] = rmse
                bias_24[va,he] = bias
            
            else:
                
                rmse_s[:,va,he] = rmse
                bias_s[:,va,he] = bias
            
            va+=1
            
        if period == 24:
            
            df_24 = df_24.append({'sonic' : sonic, 'rmse_24h_vh':rmse_24[0,he], 'bias_24h_vh':bias_24[0,he], 'rmse_24h_dir':rmse_24[1,he], 'bias_24h_dir':bias_24[1,he], 'rmse_24h_tke':rmse_24[2,he], 'bias_24h_tke':bias_24[2,he]}, ignore_index = True)
            
        if period == 6:
            
            df_6_vh = df_6_vh.append({'sonic' : sonic, 'rmse_0-6h_vh':rmse_s[-4,0,he], 'bias_0-6h_vh':bias_s[-4,0,he], 'rmse_6-12h_vh':rmse_s[-3,0,he], 'bias_6-12h_vh':bias_s[-3,0,he], 'rmse_12-18h_vh':rmse_s[-2,0,he], 'bias_12-18h_vh':bias_s[-2,0,he], 'rmse_18-24h_vh':rmse_s[-1,0,he], 'bias_18-24h_vh':bias_s[-1,0,he]}, ignore_index = True)
            df_6_dir = df_6_dir.append({'sonic' : sonic, 'rmse_0-6h_dir':rmse_s[-4,1,he], 'bias_0-6h_dir':bias_s[-4,1,he], 'rmse_6-12h_dir':rmse_s[-3,1,he], 'bias_6-12h_dir':bias_s[-3,1,he], 'rmse_12-18h_dir':rmse_s[-2,1,he], 'bias_12-18h_dir':bias_s[-2,1,he], 'rmse_18-24h_dir':rmse_s[-1,1,he], 'bias_18-24h_dir':bias_s[-1,1,he]}, ignore_index = True)
            df_6_tke = df_6_tke.append({'sonic' : sonic, 'rmse_0-6h_tke':rmse_s[-4,2,he], 'bias_0-6h_tke':bias_s[-4,2,he], 'rmse_6-12h_tke':rmse_s[-3,2,he], 'bias_6-12h_tke':bias_s[-3,2,he], 'rmse_12-18h_tke':rmse_s[-2,2,he], 'bias_12-18h_tke':bias_s[-2,2,he], 'rmse_18-24h_tke':rmse_s[-1,2,he], 'bias_18-24h_tke':bias_s[-1,2,he]}, ignore_index = True)            
            
        
        he+=1

#date_index = path_pf.find('201')
#s = path_pf[date_index:date_index+23]

#direc = r'C:\Users\Baba\Desktop\João\Tese\Python\Teste_1\Perdigao_python\App 2.0\tables'

#df_24.to_csv(os.path.join(r'{}'.format(direc),'rmse_24h_table_{}.csv'.format(s)))
if period == 24:
    
    df_24.to_csv('rmse_24h_table_20170514_20170515_0-18h.csv', index=None)

if period == 6:
    
    #df_6_vh.to_csv('rmse_6h_vh_table_20170514_20170515_0-18h.csv', index=None)
    #df_6_dir.to_csv('rmse_6h_dir_table_20170514_20170515_0-18h.csv', index=None)
    #df_6_tke.to_csv('rmse_6h_tke_table_20170514_20170515_0-18h.csv', index=None)
    pass
    



'''
sonic = 'EXTREME_NE'
from math import nan
n1 = nan

df_24 = df_24.append({'sonic' : sonic, 'rmse_24h_vh':n1, 'bias_24h_vh':n1, 'rmse_24h_dir':n1, 'bias_24h_dir':n1, 'rmse_24h_tke':n1, 'bias_24h_tke':n1}, ignore_index = True)

df_6_vh = df_6_vh.append({'sonic' : sonic, 'rmse_0-6h_vh':n1, 'bias_0-6h_vh':n1, 'rmse_6-12h_vh':n1, 'bias_6-12h_vh':n1, 'rmse_12-18h_vh':n1, 'bias_12-18h_vh':n1, 'rmse_18-24h_vh':n1, 'bias_18-24h_vh':n1}, ignore_index = True)
df_6_dir = df_6_dir.append({'sonic' : sonic, 'rmse_0-6h_dir':n1, 'bias_0-6h_dir':n1, 'rmse_6-12h_dir':n1, 'bias_6-12h_dir':n1, 'rmse_12-18h_dir':n1, 'bias_12-18h_dir':n1, 'rmse_18-24h_dir':n1, 'bias_18-24h_dir':n1}, ignore_index = True)
df_6_tke = df_6_tke.append({'sonic' : sonic, 'rmse_0-6h_tke':n1, 'bias_0-6h_tke':n1, 'rmse_6-12h_tke':n1, 'bias_6-12h_tke':n1, 'rmse_12-18h_tke':n1, 'bias_12-18h_tke':n1, 'rmse_18-24h_tke':n1, 'bias_18-24h_tke':n1}, ignore_index = True)
'''