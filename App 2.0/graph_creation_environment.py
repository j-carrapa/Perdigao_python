# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 17:46:08 2022

@author: Joao
"""

# Falta rever directorios e pastas

# Graph Creation environment

import graph_functions as gf
import numpy as np
import pandas as pd
import tower_location as tl

def rmse_bias (hour_period,va,sta,he,nvars,heights,rmse,bias,df_rmse_bias):
    
    i = df.columns.get_loc(v_name)
    j = df_ventos.columns.get_loc(v_name)
    
    
    exp = pf_2d_array[:, i]
    sim = data[:, j]
    
    if v_name == 'dir':
        
        for k in range(nhour):
            
            exp = pf_2d_array[k*hour_period*12:k*hour_period*12+12*hour_period,i]
            sim = data[k*hour_period*12:k*hour_period*12+12*hour_period,j]
            
            err[k,va,he], mse[k,va,he], rmse[k,va,he], bias[k,va,he] = gf.rmse_f(exp, sim, True)
            
            #if height == heights[-1]:
                
                #mean_e[k,va], mean_s[k,va] = gf.mean_vars(exp, sim)
                
        va +=1
        
    else:
        
        for k in range(nhour):
            
            exp = pf_2d_array[k*hour_period*12:k*hour_period*12+12*hour_period,i]
            sim = data[k*hour_period*12:k*hour_period*12+12*hour_period,j]
            
            err[k,va,he], mse[k,va,he], rmse[k,va,he], bias[k,va,he] = gf.rmse_f(exp, sim)
            
            #if height == heights[-1]:
                
                #mean_e[k,va], mean_s[k,va] = gf.mean_vars(exp, sim)
            
        va +=1
        
    if hour_period == 6:
        
        pass
    
    return rmse, bias, va, he, df_rmse_bias

# Changeable parameters

plot_type = 1
table_rmse = 0
    
rmse_var = 0
towers = np.array(["tse04", "tnw09"])#, "tnw09", "tnw10"])#"tnw01", "tnw02", "tnw03", "tnw04", "tnw05"])#, "tnw06", "tnw07", "tnw08", "tnw09", "tnw10"])#

highlight = 1

#tower_p = 'tnw04'
hour_period = 1

index_df = np.arange(185)
df_rmse_bias = pd.DataFrame(0, columns= ['sonic', 'rmse_24h', 'bias_24h','rmse_0-6h', 'bias_0-6h', 'rmse_6-12h', 'bias_6-12h','rmse_12-18h', 'bias_12-18h', 'rmse_18-24h', 'bias_18-24h'], index=index_df)

if towers.size == 1:
    
    j = tl.tower_index_pos(towers)

    #heights = np.array(["10", "20", "30", "40", "60", "80", "100"])
    heights = tl.sonics_available_name(j)

    direc_pf = r'C:\Users\Baba\Desktop\João\Tese\Python\Teste_1\Perdigao_python\App 2.0\data_pf'
    path_ventos_sonics_coord = r'C:\Users\Baba\Desktop\João\Tese\Python\Teste_1\Perdigao_python\App 2.0\sonics_coord_est_nor_z.csv'
    direc_sim = r'C:\Users\Baba\Desktop\João\Tese'

    '''-------------'''

    if plot_type == 1:
        
        a_name = "vh"
        b_name = "dir"
        c_name = "tke"
        
    if plot_type == 2:
        
        a_name = "u"
        b_name = "v"
        c_name = "w"
        
    if plot_type == 3:
        
        a_name = "uu"
        b_name = "vv"
        c_name = "ww"
        
    if plot_type == 4:
        
        a_name = "vh"
        b_name = "dir"
        c_name = "tke"
        
    # This last option does not plot anything, just produces RMSE's tables
        
    if plot_type == 5:
        
        a_name = "vh"
        b_name = "dir"
        c_name = "tke"
        table_rmse = 1


    nvars = np.array(a_name)
    nvars = np.append(a_name, [b_name, c_name])

    sta = 0
    he = 0

    for height in heights:
        
        ''' Perdigao File '''

        path_pf = r'{}\{}m_{}_20170514_20170515_0-18h_P-5min.csv'.format(direc_pf,height,towers)

        df, pf_2d_array, pf_num_rows = gf.df_perdigao_file(path_pf)

        ''' VENTOS File V2'''

        df_ventos, data = gf.df_ventos_file(towers,height,direc_sim,path_ventos_sonics_coord)

        va = 0

        for v_name in nvars:
            
            nh = int(pf_num_rows/hour_period)

            if sta == 0:
                
                nhour = int(nh/12)
                var = len(nvars)
                h = len(heights)

                err = np.zeros((nhour,var,h))
                mse = np.zeros((nhour,var,h))
                rmse = np.zeros((nhour,var,h))
                bias = np.zeros((nhour,var,h))
                r = np.zeros((nhour,var,h))
                ss = np.zeros((nhour,var,h))
                mean_e = np.zeros((nhour,var))
                mean_s = np.zeros((nhour,var))
                sta = 1
            
            rmse, bias ,va ,he ,df_rmse_bias = rmse_bias(hour_period, va, sta, he, nvars, heights,rmse,bias,df_rmse_bias)
            
        he +=1
        continue
            
    

    rmse_min = np.zeros((nhour,var))
    rmse_max = np.zeros((nhour,var))


    for va in range(var):
        
        for k in range(nhour):
            
            a = 0
            for he in range(h):
                
                rm = rmse[k,va,he]
                
                if a == 0:
                    rmse_min[k,va] = rm
                    rmse_max[k,va] = rm
                    a = 1
                
                if rm < rmse_min[k,va]:
                    rmse_min[k,va] = rm
                    
                if rm > rmse_max[k,va]:
                    rmse_max[k,va] = rm

    '''-------------'''

    # Plot

    for height in heights:
        
        ''' Perdigao File '''

        path_pf = r'{}\{}m_{}_20170514_20170515_0-18h_P-5min.csv'.format(direc_pf,height,towers)

        df, pf_2d_array, pf_num_rows = gf.df_perdigao_file(path_pf)

        ''' VENTOS File V2'''

        df_ventos, data = gf.df_ventos_file(towers,height,direc_sim,path_ventos_sonics_coord)

        if plot_type == 1:
            
            gf.plot_v_dir_t(path_pf, pf_2d_array, a_name, b_name, c_name, df, df_ventos, data, highlight)

        if plot_type == 2:
            
            gf.plot_uvw(path_pf,pf_2d_array,df,df_ventos,data,highlight)

        if plot_type == 3:
            
            gf.plot_variances(path_pf,pf_2d_array,df,df_ventos,data,highlight)
            
        if plot_type == 4:
            
            gf.plot_rmse_v_dir_t(path_pf,pf_2d_array,nvars,df,df_ventos,rmse_min,rmse_max,nhour,data,highlight=1)
            

    # Tables

    if table_rmse != 0:
        
        df_rmse, rmse_v = gf.tab_rmse_v(rmse, rmse_var,nhour,heights)
        gf.save_rmse_table(df_rmse,path_pf,rmse_var,a_name,b_name,c_name,towers)

    

else:
    
    for tower_p in towers:
        
        j = tl.tower_index_pos(tower_p)

        #heights = np.array(["10", "20", "30", "40", "60", "80", "100"])
        heights = tl.sonics_available_name(j)

        direc_pf = r'C:\Users\Baba\Desktop\João\Tese\Python\Teste_1\Perdigao_python\App 2.0\data_pf'
        path_ventos_sonics_coord = r'C:\Users\Baba\Desktop\João\Tese\Python\Teste_1\Perdigao_python\App 2.0\sonics_coord_est_nor_z.csv'
        direc_sim = r'C:\Users\Baba\Desktop\João\Tese'

        '''-------------'''

        if plot_type == 1:
            
            a_name = "vh"
            b_name = "dir"
            c_name = "tke"
            
        if plot_type == 2:
            
            a_name = "u"
            b_name = "v"
            c_name = "w"
            
        if plot_type == 3:
            
            a_name = "uu"
            b_name = "vv"
            c_name = "ww"
            
        if plot_type == 4:
            
            a_name = "vh"
            b_name = "dir"
            c_name = "tke"
            
        # This last option does not plot anything, just produces RMSE's tables
            
        if plot_type == 5:
            
            a_name = "vh"
            b_name = "dir"
            c_name = "tke"
            table_rmse = 1


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

            va = 0

            for v_name in nvars:
                
                nh = int(pf_num_rows/hour_period)

                if sta == 0:
                    
                    nhour = int(nh/12)
                    var = len(nvars)
                    h = len(heights)

                    err = np.zeros((nhour,var,h))
                    mse = np.zeros((nhour,var,h))
                    rmse = np.zeros((nhour,var,h))
                    bias = np.zeros((nhour,var,h))
                    r = np.zeros((nhour,var,h))
                    ss = np.zeros((nhour,var,h))
                    mean_e = np.zeros((nhour,var))
                    mean_s = np.zeros((nhour,var))
                    sta = 1
                
                rmse, bias ,va ,he ,df_rmse_bias = rmse_bias(hour_period, va, sta, he, nvars, heights,rmse,bias,df_rmse_bias)
                
            he +=1
            continue
                
        

        rmse_min = np.zeros((nhour,var))
        rmse_max = np.zeros((nhour,var))


        for va in range(var):
            
            for k in range(nhour):
                
                a = 0
                for he in range(h):
                    
                    rm = rmse[k,va,he]
                    
                    if a == 0:
                        rmse_min[k,va] = rm
                        rmse_max[k,va] = rm
                        a = 1
                    
                    if rm < rmse_min[k,va]:
                        rmse_min[k,va] = rm
                        
                    if rm > rmse_max[k,va]:
                        rmse_max[k,va] = rm
             
            
        '''-------------'''

        # Plot

        for height in heights:
            
            ''' Perdigao File '''

            path_pf = r'{}\{}m_{}_20170514_20170515_0-18h_P-5min.csv'.format(direc_pf,height,tower_p)

            df, pf_2d_array, pf_num_rows = gf.df_perdigao_file(path_pf)

            ''' VENTOS File V2'''

            df_ventos, data = gf.df_ventos_file(tower_p,height,direc_sim,path_ventos_sonics_coord)

            if plot_type == 1:
                
                gf.plot_v_dir_t(path_pf, pf_2d_array, a_name, b_name, c_name, df, df_ventos, data, highlight)

            if plot_type == 2:
                
                gf.plot_uvw(path_pf,pf_2d_array,df,df_ventos,data,highlight)

            if plot_type == 3:
                
                gf.plot_variances(path_pf,pf_2d_array,df,df_ventos,data,highlight)
                
            if plot_type == 4:
                
                gf.plot_rmse_v_dir_t(path_pf,pf_2d_array,nvars,df,df_ventos,rmse_min,rmse_max,nhour,data,highlight=1)
                

        # Tables

        if table_rmse != 0:
            
            df_rmse, rmse_v = gf.tab_rmse_v(rmse, rmse_var,nhour,heights)
            gf.save_rmse_table(df_rmse,path_pf,rmse_var,a_name,b_name,c_name,tower_p)

        
            


#rmse, bias = rmse_bias(hour_period, va, sta, he, nvars, heights)

'''

#print("va:{}".format(va))

    i = df.columns.get_loc(v_name)
    j = df_ventos.columns.get_loc(v_name)

    if sta == 0:
        
        nhour = int(pf_num_rows/12)
        var = len(nvars)
        h = len(heights)

        err = np.zeros((nhour,var,h))
        mse = np.zeros((nhour,var,h))
        rmse = np.zeros((nhour,var,h))
        bias = np.zeros((nhour,var,h))
        r = np.zeros((nhour,var,h))
        ss = np.zeros((nhour,var,h))
        mean_e = np.zeros((nhour,var))
        mean_s = np.zeros((nhour,var))
        sta = 1
    
    exp = pf_2d_array[:, i]
    sim = data[:, j]
    
    if v_name == 'dir':
        
        for k in range(nhour):
            
            exp = pf_2d_array[k*12:k*12+12,i]
            sim = data[k*12:k*12+12,j]
            
            err[k,va,he], mse[k,va,he], rmse[k,va,he], bias[k,va,he] = gf.rmse_f(exp, sim, True)
            
            if height == heights[-1]:
                
                mean_e[k,va], mean_s[k,va] = gf.mean_vars(exp, sim)
                
        va +=1
        continue
    
    else:
        
        for k in range(nhour):
            
            exp = pf_2d_array[k*12:k*12+12,i]
            sim = data[k*12:k*12+12,j]
            
            err[k,va,he], mse[k,va,he], rmse[k,va,he], bias[k,va,he] = gf.rmse_f(exp, sim)
            
            if height == heights[-1]:
                
                mean_e[k,va], mean_s[k,va] = gf.mean_vars(exp, sim)
            
        va +=1
        continue

he +=1
continue

'''
def rmse_bias_2 (pf_2d_array,data,v_name,period):
    
    i = df.columns.get_loc(v_name)
    j = df_ventos.columns.get_loc(v_name)
    
    #exp_data = pf_2d_array[:, i]
    #sim_data = data[:, j]
    
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
            sim = data[k*period*12:k*period*12+period*12,i]
                
            if v_name == 'dir':

                err[k], mse[k], rmse[k], bias[k] = gf.rmse_f(exp, sim, True)
                
            else:
                
                err[k], mse[k], rmse[k], bias[k] = gf.rmse_f(exp, sim)
                
    return rmse, bias


'''
period = 6
v_name = 'vh'
nhour = int(pf_num_rows/period/12)
rmse = np.zeros(nhour)
bias = np.zeros(nhour)

rmse, bias = rmse_bias_2(pf_2d_array,data,v_name,period)


tower = 'tnw01'

j = tl.tower_index_pos(tower_p)

heights = tl.sonics_available_name(j)
'''
#direc_pf = r'C:\Users\Baba\Desktop\João\Tese\Python\Teste_1\Perdigao_python\App 2.0\data_pf'
#path_ventos_sonics_coord = r'C:\Users\Baba\Desktop\João\Tese\Python\Teste_1\Perdigao_python\App 2.0\sonics_coord_est_nor_z.csv'
#direc_sim = r'C:\Users\Baba\Desktop\João\Tese'
'''
a_name = "vh"
b_name = "dir"
c_name = "tke"

nvars = np.array(a_name)
nvars = np.append(a_name, [b_name, c_name])

'''
    
    
