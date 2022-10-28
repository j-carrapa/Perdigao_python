# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 16:23:29 2022

@author: Joao
"""

# Status: Reviewed

# Turbulence Module - contains functions to calc turbulence parameters
# For time periods different than 5 min the turbulence parameters calculated should be reviewed

import numpy as np

# Adding turbulence parameters to the original Data Frame

def turbulence_5min (dfc):
    '''Takes the data frame containing the variables retrieved from the sonic (pandas Data Frame), Returns the same data frame with three new columns with calculated values of turbulence kinetic energy, turbulence intensity and turbulence intensity from horizontal components for data of 5 min period (pandas Data Frame)'''
    dt = np.arange(0, dfc.size/13, dtype=int)

    i = 0
    for a in dt:
        
        if i == 0:
            
            u = dfc.iat[a,2]
            v = dfc.iat[a,3]
            w = dfc.iat[a,4]
            
            uu = dfc.iat[a,7]
            vv = dfc.iat[a,8]
            ww = dfc.iat[a,9]
            
            tke = (1/2)*(uu+vv+ww)
            ti = np.sqrt(tke*(2/3))/np.sqrt(u*u+v*v+w*w)
            tih = np.sqrt((1/3)*(uu+vv))/np.sqrt(u*u+v*v)
            
            tke_arr = np.array(tke, dtype='float')
            ti_arr = np.array(ti, dtype='float')
            tih_arr = np.array(tih, dtype='float')
            
            i = 1

        else:
            u = dfc.iat[a,2]
            v = dfc.iat[a,3]
            w = dfc.iat[a,4]
            
            uu = dfc.iat[a,7]
            vv = dfc.iat[a,8]
            ww = dfc.iat[a,9]
            
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


# Creation of arrays with variances and covariances for time periods different from 5 min

def var_k (dfc, k):
    '''Takes the data frame containing the variables retrieved from the sonic (pandas Data Frame) and time period conversion value (int), Returns arrays containing the values of variances for the desired time periods (np array of float)'''
    dt = np.arange(0, dfc.size/13, dtype=int)
    
    i = 0
    j = 0

    for a in dt:
        
        u = dfc.iat[a,2]
        v = dfc.iat[a,3]
        w = dfc.iat[a,4]
        
        uu = dfc.iat[a,7]
        vv = dfc.iat[a,8]
        ww = dfc.iat[a,9]
        
        if i == 0:
            u_m1 = u*u
            uu_m2 = uu
            u_m3 = u
            
            v_m1 = v*v
            vv_m2 = vv
            v_m3 = v
            
            w_m1 = w*w
            ww_m2 = ww
            w_m3 = w
        
        if i > 0 and i < k:
            u_m1 = u_m1 + u*u
            uu_m2 = uu_m2*uu
            u_m3 = u_m3 + u
            
            v_m1 = v_m1 + v*v
            vv_m2 = vv_m2*vv
            v_m3 = v_m3 + v
            
            w_m1 = w_m1 + w*w
            ww_m2 = ww_m2*ww
            w_m3 = w_m3 + w
            
        i += 1
        
        if i == k:
            u_var = (u_m1/k)+(uu_m2/k)-(u_m3/k)*(u_m3/k)
            v_var = (v_m1/k)+(vv_m2/k)-(v_m3/k)*(v_m3/k)
            w_var = (w_m1/k)+(ww_m2/k)-(w_m3/k)*(w_m3/k)
            
            if j == 0:
                uu_arr = np.array(u_var, dtype='float')
                vv_arr = np.array(v_var, dtype='float')
                ww_arr = np.array(w_var, dtype='float')
                
            if j > 0:
                
                temp_uu = np.array(u_var, dtype='float')
                temp_vv = np.array(v_var, dtype='float')
                temp_ww = np.array(w_var, dtype='float')
                
                uu_arr = np.append(uu_arr, [temp_uu])
                vv_arr = np.append(vv_arr, [temp_vv])
                ww_arr = np.append(ww_arr, [temp_ww])
                
            j += 1
                
            i = 0
            
    return uu_arr, vv_arr, ww_arr

# Creation of array with turbulence kinetic energy for time periods different from 5 min

def tke_k (dfc, k):
    '''Takes the data frame containing the variables retrieved from the sonic (pandas Data Frame) and time period conversion value (int), Returns array containing the values of turbulence kinetic energy for the desired time periods (np array of float)'''
    dt = np.arange(0, dfc.size/13, dtype=int)
    
    i = 0
    j = 0

    for a in dt:
        
        u = dfc.iat[a,2]
        v = dfc.iat[a,3]
        w = dfc.iat[a,4]
        
        uu = dfc.iat[a,7]
        vv = dfc.iat[a,8]
        ww = dfc.iat[a,9]
        
        if i == 0:
            u_m1 = u*u
            uu_m2 = uu
            u_m3 = u
            
            v_m1 = v*v
            vv_m2 = vv
            v_m3 = v
            
            w_m1 = w*w
            ww_m2 = ww
            w_m3 = w
        
        if i > 0 and i < k:
            u_m1 = u_m1 + u*u
            uu_m2 = uu_m2*uu
            u_m3 = u_m3 + u
            
            v_m1 = v_m1 + v*v
            vv_m2 = vv_m2*vv
            v_m3 = v_m3 + v
            
            w_m1 = w_m1 + w*w
            ww_m2 = ww_m2*ww
            w_m3 = w_m3 + w
            
        i += 1
        
        if i == k:
            u_var = (u_m1/k)+(uu_m2/k)-(u_m3/k)*(u_m3/k)
            v_var = (v_m1/k)+(vv_m2/k)-(v_m3/k)*(v_m3/k)
            w_var = (w_m1/k)+(ww_m2/k)-(w_m3/k)*(w_m3/k)
            
            tke = (1/2)*(u_var+v_var+w_var)
            
            if j == 0:
                tke_arr = np.array(tke, dtype='float')
                
            if j > 0:
                
                temp = np.array(tke, dtype='float')
                
                tke_arr = np.append(tke_arr, [temp])
                
            j += 1
                
            i = 0
            
    return tke_arr


# Creation of array with turbulence intensity for time periods different from 5 min

def ti_k (dfc, k):
    '''Takes the data frame containing the variables retrieved from the sonic (pandas Data Frame) and time period conversion value (int), Returns array containing the values of turbulence intensity for the desired time periods (np array of float)'''    
    dt = np.arange(0, dfc.size/13, dtype=int)
    
    i = 0
    j = 0

    for a in dt:
        
        u = dfc.iat[a,2]
        v = dfc.iat[a,3]
        w = dfc.iat[a,4]
        
        uu = dfc.iat[a,7]
        vv = dfc.iat[a,8]
        ww = dfc.iat[a,9]
        
        if i == 0:
            u_m1 = u*u
            uu_m2 = uu
            u_m3 = u
            
            v_m1 = v*v
            vv_m2 = vv
            v_m3 = v
            
            w_m1 = w*w
            ww_m2 = ww
            w_m3 = w
        
        if i > 0 and i < k:
            u_m1 = u_m1 + u*u
            uu_m2 = uu_m2*uu
            u_m3 = u_m3 + u
            
            v_m1 = v_m1 + v*v
            vv_m2 = vv_m2*vv
            v_m3 = v_m3 + v
            
            w_m1 = w_m1 + w*w
            ww_m2 = ww_m2*ww
            w_m3 = w_m3 + w
            
        i += 1
        
        if i == k:
            u_var = (u_m1/k)+(uu_m2/k)-(u_m3/k)*(u_m3/k)
            v_var = (v_m1/k)+(vv_m2/k)-(v_m3/k)*(v_m3/k)
            w_var = (w_m1/k)+(ww_m2/k)-(w_m3/k)*(w_m3/k)
            
            tke = (1/2)*(u_var+v_var+w_var)
            ti = np.sqrt(tke*(2/3))/(np.sqrt((u_m3/k)*(u_m3/k)+(v_m3/k)*(v_m3/k)+(w_m3/k)*(w_m3/k)))
            
            if j == 0:
                ti_arr = np.array(ti, dtype='float')
                
                
            if j > 0:
                
                temp = np.array(ti, dtype='float')
                
                ti_arr = np.append(ti_arr, [temp])
            j += 1
                
            i = 0
    
    return ti_arr


# Creation of array with turbulence intensity from horizontal components for time periods different from 5 min

def tih_k (dfc, k):
    '''Takes the data frame containing the variables retrieved from the sonic (pandas Data Frame) and time period conversion value (int), Returns array containing the values of turbulence intensity from horizontal components for the desired time periods (np array of float)'''    
    dt = np.arange(0, dfc.size/13, dtype=int)
    
    i = 0
    j = 0

    for a in dt:
        
        u = dfc.iat[a,2]
        v = dfc.iat[a,3]
        
        uu = dfc.iat[a,7]
        vv = dfc.iat[a,8]
        
        if i == 0:
            u_m1 = u*u
            uu_m2 = uu
            u_m3 = u
            
            v_m1 = v*v
            vv_m2 = vv
            v_m3 = v
        
        if i > 0 and i < k:
            u_m1 = u_m1 + u*u
            uu_m2 = uu_m2*uu
            u_m3 = u_m3 + u
            
            v_m1 = v_m1 + v*v
            vv_m2 = vv_m2*vv
            v_m3 = v_m3 + v
            
        i += 1
        
        if i == k:
            u_var = (u_m1/k)+(uu_m2/k)-(u_m3/k)*(u_m3/k)
            v_var = (v_m1/k)+(vv_m2/k)-(v_m3/k)*(v_m3/k)
            
            tih = np.sqrt((u_var+v_var)/3)/(np.sqrt((u_m3/k)*(u_m3/k)+(v_m3/k)*(v_m3/k)))
            
            if j == 0:
                tih_arr = np.array(tih, dtype='float')
                  
            if j > 0:
                
                temp = np.array(tih, dtype='float')
                
                tih_arr = np.append(tih_arr, [temp])
            j += 1
                
            i = 0
    
    return tih_arr
            

# Append variance arrays to the new data frame with the time period adjusted

def var_append(dfc, uu, vv, ww):
    '''Takes time period adjusted data frame (pandas Data Frame), three arrays containing variances time period adjusted parameteres(np arrays of float), Returns complete data frame (pandas Data Frame)'''
    dfc['uu'] = uu.tolist()
    dfc['vv'] = vv.tolist()
    dfc['ww'] = ww.tolist()

    return dfc


# Append variance arrays to the new data frame with the time period adjusted

def covar_append(dfc, uv, uw, vw):
    '''Takes time period adjusted data frame (pandas Data Frame), three arrays containing covariances time period adjusted parameteres(np arrays of float), Returns complete data frame (pandas Data Frame)'''
    dfc['uv'] = uv.tolist()
    dfc['uw'] = uw.tolist()
    dfc['vw'] = vw.tolist()

    return dfc


# Append turbulence arrays to the new data frame with the time period adjusted

def turb_append(dfc, tke_arr, ti_arr, tih_arr):
    '''Takes time period adjusted data frame (pandas Data Frame), three arrays containing turbulence time period adjusted parameteres(np arrays of float), Returns complete data frame (pandas Data Frame)'''
    dfc['tke'] = tke_arr.tolist()
    dfc['ti'] = ti_arr.tolist()
    dfc['tih'] = tih_arr.tolist()

    return dfc

