# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 16:23:29 2022

@author: Joao
"""

# Turbulence Module - contains functions to calc turbulence parameters

import numpy as np

def turbulence_5min (dfc):
    
    dt = np.arange(0, dfc.size/13, dtype=int)
    
    i = 0
    for a in dt:
        
        if i == 0:
            tke = 0
            tke_arr = np.array(tke, dtype='float')
            ti = 0
            ti_arr = np.array(ti, dtype='float')
            tih = 0
            tih_arr = np.array(tih, dtype='float')

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
            
        
        i +=1
        

    dfc['tke'] = tke_arr.tolist()
    dfc['ti'] = ti_arr.tolist()
    dfc['tih'] = tih_arr.tolist()

    global df
    df = dfc.copy()
    return df



def tke_k (dfc, k):
    
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
            
    global tke_a
    tke_a = tke_arr.copy()
    return tke_a


def ti_k (dfc, k):
    
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
    
    global ti_a
    ti_a = ti_arr.copy()
    return ti_a




def tih_k (dfc, k):
    
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
    
    global tih_a
    tih_a = tih_arr.copy()
    return tih_a
            


def turb_append(dfc, tke_arr, ti_arr, tih_arr):
    
    dfc['tke'] = tke_arr.tolist()
    dfc['ti'] = ti_arr.tolist()
    dfc['tih'] = tih_arr.tolist()

    global df1
    df1 = dfc.copy()
    return df1
