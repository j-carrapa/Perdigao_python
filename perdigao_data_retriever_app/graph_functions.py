# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 17:49:06 2022

@author: Joao
"""

# Graph Functions

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import os.path

direc_graphs = r'C:\Users\Baba\Desktop\João\Tese\Python\Teste_1\Perdigao_python\App 2.0\graphs'

# Array containing all towers names

def towers_name ():
    '''Takes none, Returns array with towers code name (np array of string)'''
    t_name = np.array(["tnw01", "tnw02", "tnw03", "tnw04", "tnw05", "tnw06", "tnw07", "tnw08", "tnw09", "tnw10", "tnw11", "tnw12", "tnw13", "tnw14", "tnw15", "tnw16", "tse01", "tse02", "tse04", "tse05", "tse06", "tse07", "tse08", "tse09", "tse10", "tse11", "tse12", "tse13", "rsw01", "rsw02", "rsw03", "rsw04", "rsw05", "rsw06", "rsw07", "rsw08", "rne01", "rne02", "rne03", "rne04", "rne06", "rne07", "v01", "v03", "v04", "v05", "v06", "v07", "Extreme_SW", "Extreme_NE"])
    return t_name


# Array containing all sonics heights

def sonics_height_array ():
    '''Takes none, Returns array with sonics heights (np array of string)'''
    # 2m, 4m, 6m, 8m, 10m, 12m, 20m, 30m, 40m, 60m, 80m, 100,

    height = np.array(["2", "4", "6", "8", "10", "12", "20", "30", "40", "60", "80", "100"])
    
    return height


# Sonic and tower info

def tower_title(path):
    '''Takes path (url), Returns tower name (str)'''
    t_name = towers_name()
    for a in t_name:    
        if a in path:            
            t_title = a           
    return t_title


def sonic_title(path):
    '''Takes path (url), Returns sonic height name (str)'''
    heights = sonics_height_array()
    for b in heights:
        b = b +'m'
        if b in path:
            h_title = b
    return h_title


# TKE recalculated for VENTOS File

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


# Error indicator functions:
    
def rmse_f(exp, sim, azimuth=False):

    ''' Calculate errors, bias and RMSE between measurements and forecast
        data '''
    ''' Use azimuth option for Wind Direction error '''

    delta = sim - exp
    if azimuth:
        # Check if it works.
        signm = np.reshape(np.concatenate((np.zeros(np.shape(delta)),
                                           np.sign(np.abs(delta) - 180.))),
                           (2, np.size(delta)))
        # print(signm)
        sign = np.max(signm, axis=0)
        # print(sign)
        abs_err = delta - 360. * np.sign(delta) * sign
        # print(abs_err)
    else:
        abs_err = delta

    # Error (prof., check for azimuth)
    err = np.sum(np.abs(abs_err)/exp)/np.size(sim)
    # Mean square error
    mse = (1/np.size(sim)) * np.sum(abs_err**2)
    # RMSE
    rmse = np.sqrt(mse)
    # Bias
    bias = (1/np.size(sim))*np.sum(abs_err)

    return err, mse, rmse, bias


# Mean Vars

def mean_vars(exp,sim):
    '''Takes exp (array), sim (array), Returns mean_e, mean_s, mean values of both arrays (float)'''
    mean_e = sum(exp)/np.size(exp)
    mean_s = sum(sim)/np.size(sim)
    return mean_e,mean_s


# Labels

def y_labels(var):
    '''Takes variable name (str), Returns appropriate variable label (str)'''
    if var == 'u':
        label = '$U$ (m s$^{-1}$)'
    if var == 'v':
        label = '$V$ (m s$^{-1}$)'
    if var == 'w':
        label = '$W$ (m s$^{-1}$)'
    if var == 'vh':
        label = 'Wind Speed\n(m s$^{-1}$)'
    if var == 'dir':
        label = 'Direction ($\degree$)'
    if var == 'uu':
        label = '$U$ $Var$\n(m$^2$ s$^{-2}$)'
    if var == 'vv':
        label = '$V$ $Var$\n(m$^2$ s$^{-2}$)'
    if var == 'ww':
        label = '$W$ $Var$\n(m$^2$ s$^{-2}$)'
    if var == 'tke':
        label = 'TKE (m$^2$ s$^{-2}$)'
    if var == 'ti':
        label = 'TI'
    if var == 'tih':
        label = 'TIH'
    return label


def y_labels_rmse(var):
    '''Takes variable name (str), Returns appropriate variable label (str)'''
    if var == 'u':
        label = 'RMSE\n$U$ (m s$^{-1}$)'
    if var == 'v':
        label = 'RMSE\n$V$ (m s$^{-1}$)'
    if var == 'w':
        label = 'RMSE\n$W$ (m s$^{-1}$)'
    if var == 'vh':
        label = 'RMSE Wind\nSpeed (m s$^{-1}$)'
    if var == 'dir':
        label = 'RMSE\nDirection ($\degree$)'
    if var == 'uu':
        label = 'RMSE $U$ $Var$ (m$^2$ s$^{-2}$)'
    if var == 'vv':
        label = 'RMSE $V$ $Var$ (m$^2$ s$^{-2}$)'
    if var == 'ww':
        label = 'RMSE $W$ $Var$ (m$^2$ s$^{-2}$)'
    if var == 'tke':
        label = 'RMSE TKE\n(m$^2$ s$^{-2}$)'
    if var == 'ti':
        label = 'RMSE TI'
    if var == 'tih':
        label = 'RMSE TIH'
    return label
    

# Plot rmse

def plot_rmse_v_dir_t(path_pf,pf_2d_array,nvars,df,df_ventos,rmse_min,rmse_max,nhour,data,highlight=0):
    '''Takes path of Perdigão file (str), data from Perdigão file (2D np array of float), array containing variables names (array of str), data frame with Perdigão data (pandas DataFrame), data frame with VENTOS®/M data (pandas DataFrame), array with max RMSE per tower for all variables (np array of float), array with min RMSE per tower for all variables (np array of float), number of hourly periods to be plotted (int), data from VENTOS®/M file (2D np array of float), flag variable to learn if the shaded area of the last 24h is to be displayed or not, Returns none'''
    a_name = nvars[0]
    b_name = nvars[1]
    c_name = nvars[2]
    
    a1 = df.columns.get_loc(a_name)
    b1 = df.columns.get_loc(b_name)
    c1 = df.columns.get_loc(c_name)
    a2 = df_ventos.columns.get_loc(a_name)
    b2 = df_ventos.columns.get_loc(b_name)
    c2 = df_ventos.columns.get_loc(c_name)

    # Plot formatting:
    plt.rcParams['font.family'] = 'sans-serif'
    #plt.rcParams.update({'font.sans-serif':'Helvetica'})
    SMALL_SIZE = 10
    MEDIUM_SIZE = 12
    ANOT_SIZE = SMALL_SIZE - 2
    NUMBER_SIZE = SMALL_SIZE
    plt.rc('font', size=SMALL_SIZE)        # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)   # fontsize of the axes title
    plt.rc('axes', labelsize=16)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    shadecolor = 'lavenderblush'

    #x = range(nhour)
    x = np.arange(0.5, nhour+0.5)
    xlim_l = int(x[0])
    xlim_r = int(x[-1])

    #

    fig = plt.figure()  # an empty figure with no axes

    resolution_value = 200

    plt.rcParams["figure.figsize"] = (12,6)

    plt.rcParams['figure.dpi'] = resolution_value

    t_title = tower_title(path_pf)
    #h_title = sonic_title(path_pf)

    fig, ax_lst = plt.subplots(3, 1)  # a figure with a 2x2 grid of Axes

    fig.suptitle("Tower {} RMSE's".format(t_title), fontsize=18)
    
    #subtitle = 'Wind Speed Components  U,V,W'
    

    # A

    a_ylabel = y_labels_rmse(a_name)

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
    
    #x = pf_2d_array[:,1]
    y1 = rmse_max[:,0]
    y2 = rmse_min[:,0]
    #y7 = mean_e[:,0]
    #y8 = mean_s[:,0]
    #plt.plot(x, y7, 'teal', x, y8, 'orangered')
    plt.plot(x, y1, 'b')
    plt.plot(x, y2, 'b')
    
    axa.fill_between(x, rmse_max[:,0], rmse_min[:,0], color='b',alpha=0.3, linewidth=0, label=r'RMSE')
    
    if highlight == 1:
        
        axa.fill_between(x, 0, 1, where=x > 18, color=shadecolor, alpha=0.5, transform=axa.get_xaxis_transform())
        
    
    
    #leg = axa.legend(loc='upper left', frameon=False)
    leg = axa.legend(frameon=False)

    # B

    b_ylabel = y_labels_rmse(b_name)

    axb = plt.subplot(312, sharex=axa)
    axb.set_ylabel(r'{}'.format(b_ylabel))
    # axb.xaxis.set_visible(False)
    axb.set_xticklabels([])
    axb.xaxis.set_tick_params(labelbottom=False)
    #axb.set_ylim(0, 360)
    # plt.setp(axb.get_xticklabels(), visible=False)
    axb.grid(color='k', linestyle='-', linewidth=0.7, alpha=0.2)
    axb.yaxis.set_major_locator(MultipleLocator(90))
    axb.yaxis.set_minor_locator(MultipleLocator(18))
    axb.tick_params(which='major', length=7, width=1, direction='in', top=True, right=True)
    axb.tick_params(which='minor', length=3, width=1, direction='in', top=True, right=True)

    y3 = rmse_max[:,1]

    y4 = rmse_min[:,1]

    #plt.plot(x, y3, 'teal', x, y4, 'orangered')
    plt.plot(x, y3, 'b')
    plt.plot(x, y4, 'b')
    
    axb.fill_between(x, rmse_max[:,1], rmse_min[:,1], color='b',alpha=0.3, linewidth=0)
    
    if highlight == 1:
        
        axb.fill_between(x, 0, 1, where=x > 18, color=shadecolor, alpha=0.5, transform=axb.get_xaxis_transform())
        
        

    # C

    c_ylabel = y_labels_rmse(c_name)

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
    xtcks = np.arange(0, 43, 6)
    lbl = ['0:00','6:00', '12:00', '18:00', '00:00', '6:00', '12:00', '18:00']
    axc.annotate('May 14', (0.06, 0.05), xycoords='figure fraction', fontsize=ANOT_SIZE, color='k')
    axc.annotate('May 15', (0.5, 0.05), xycoords='figure fraction', fontsize=ANOT_SIZE, color='k')

    axc.set_xticks(ticks=xtcks)
    axc.set_xticklabels(lbl)
    #axc.annotate('a)', (.03, .82), xycoords='figure fraction', fontsize=SMALL_SIZE, color='k')
    #axc.annotate('b)', (.03, .57), xycoords='figure fraction', fontsize=SMALL_SIZE, color='k')
    #axc.annotate('c)', (.03, .3), xycoords='figure fraction', fontsize=SMALL_SIZE, color='k')

    y5 = rmse_max[:,2]

    y6 = rmse_min[:,2]

    #plt.plot(x, y5, 'teal', x, y6, 'orangered')
    plt.plot(x, y5, 'b')
    plt.plot(x, y6, 'b')
    
    axc.fill_between(x, rmse_max[:,2], rmse_min[:,2], color='b',alpha=0.3, linewidth=0)

    
    
    if highlight == 1:
        
        axc.fill_between(x, 0, 1, where=x > 18, color=shadecolor, alpha=0.5, transform=axc.get_xaxis_transform())
        


    plt.savefig(os.path.join(r'{}'.format(direc_graphs),"rmse_{}_{}_{}_{}.png".format(t_title,a_name,b_name,c_name)), format="png", dpi=resolution_value)
    

# Plot u, v, w

def plot_uvw(path_pf,pf_2d_array,df,df_ventos,data,highlight=0):
    '''Takes path of Perdigão file (str), data from Perdigão file (2D np array of float), data frame with Perdigão data (pandas DataFrame), data frame with VENTOS®/M data (pandas DataFrame), data from VENTOS®/M file (2D np array of float), flag variable to learn if the shaded area of the last 24h is to be displayed or not, Returns none'''
    a_name = "u"
    b_name = "v"
    c_name = "w"
    a1 = df.columns.get_loc(a_name)
    b1 = df.columns.get_loc(b_name)
    c1 = df.columns.get_loc(c_name)
    a2 = df_ventos.columns.get_loc(a_name)
    b2 = df_ventos.columns.get_loc(b_name)
    c2 = df_ventos.columns.get_loc(c_name)

    # Plot formatting:
    plt.rcParams['font.family'] = 'sans-serif'
    #plt.rcParams.update({'font.sans-serif':'Helvetica'})
    SMALL_SIZE = 10
    MEDIUM_SIZE = 12
    ANOT_SIZE = SMALL_SIZE - 2
    NUMBER_SIZE = SMALL_SIZE
    plt.rc('font', size=SMALL_SIZE)        # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)   # fontsize of the axes title
    plt.rc('axes', labelsize=16)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    shadecolor = 'lavenderblush'

    x = pf_2d_array[:, 1]
    xlim_l = int(x[0])
    xlim_r = int(x[-1])

    #

    fig = plt.figure()  # an empty figure with no axes

    resolution_value = 200

    plt.rcParams["figure.figsize"] = (12,6)

    plt.rcParams['figure.dpi'] = resolution_value

    t_title = tower_title(path_pf)
    h_title = sonic_title(path_pf)

    fig, ax_lst = plt.subplots(3, 1)  # a figure with a 2x2 grid of Axes

    fig.suptitle('Tower {} at {} height'.format(t_title, h_title), fontsize=18)
    
    #subtitle = 'Wind Speed Components  U,V,W'
    

    # A

    a_ylabel = y_labels(a_name)

    axa = plt.subplot(311)

    axa.set_ylabel(r'{}'.format(a_ylabel))
    #axa.set_ylim(0, 8.5)
    axa.set_xlim(xlim_l, xlim_r)
    axa.xaxis.set_tick_params(labelbottom=False)
    axa.grid(color='k', linestyle='-', linewidth=0.7, alpha=0.2)
    axa.yaxis.set_major_locator(MultipleLocator(4))
    axa.yaxis.set_minor_locator(MultipleLocator(0.8))
    axa.tick_params(which='major', length=7, width=1, direction='in', top=True, right=True)
    axa.tick_params(which='minor', length=3, width=1, direction='in', top=True, right=True)
    
    x = pf_2d_array[:,1]
    y1 = pf_2d_array[:,a1]

    y2 = data[:,a2]

    plt.plot(x, y1, 'teal', label='Measurements')
    plt.plot(x, y2, 'orangered', label='Simulation')
    
    if highlight == 1:
        
        axa.fill_between(x, 0, 1, where=x > 18*3600, color=shadecolor, alpha=0.5, transform=axa.get_xaxis_transform())
        
    #leg = axa.legend(loc='upper left', frameon=False)
    leg = axa.legend(frameon=False)

    # B

    b_ylabel = y_labels(b_name)

    axb = plt.subplot(312, sharex=axa)
    axb.set_ylabel(r'{}'.format(b_ylabel))
    # axb.xaxis.set_visible(False)
    axb.set_xticklabels([])
    axb.xaxis.set_tick_params(labelbottom=False)
    #axb.set_ylim(0, 360)
    # plt.setp(axb.get_xticklabels(), visible=False)
    axb.grid(color='k', linestyle='-', linewidth=0.7, alpha=0.2)
    axb.yaxis.set_major_locator(MultipleLocator(2))
    axb.yaxis.set_minor_locator(MultipleLocator(0.4))
    axb.tick_params(which='major', length=7, width=1, direction='in', top=True, right=True)
    axb.tick_params(which='minor', length=3, width=1, direction='in', top=True, right=True)

    y3 = pf_2d_array[:,b1]

    y4 = data[:,b2]

    plt.plot(x, y3, 'teal', x, y4, 'orangered')
    
    if highlight == 1:
        
        axb.fill_between(x, 0, 1, where=x > 18*3600, color=shadecolor, alpha=0.5, transform=axb.get_xaxis_transform())

    # C

    c_ylabel = y_labels(c_name)

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
    axc.annotate('May 14', (0.06, 0.05), xycoords='figure fraction', fontsize=ANOT_SIZE, color='k')
    axc.annotate('May 15', (0.5, 0.05), xycoords='figure fraction', fontsize=ANOT_SIZE, color='k')

    axc.set_xticks(ticks=xtcks)
    axc.set_xticklabels(lbl)
    #axc.annotate('a)', (.03, .82), xycoords='figure fraction', fontsize=SMALL_SIZE, color='k')
    #axc.annotate('b)', (.03, .57), xycoords='figure fraction', fontsize=SMALL_SIZE, color='k')
    #axc.annotate('c)', (.03, .3), xycoords='figure fraction', fontsize=SMALL_SIZE, color='k')

    y5 = pf_2d_array[:,c1]

    y6 = data[:,c2]

    plt.plot(x, y5, 'teal', x, y6, 'orangered')
    
    if highlight == 1:
        
        axc.fill_between(x, 0, 1, where=x > 18*3600, color=shadecolor, alpha=0.5, transform=axc.get_xaxis_transform())


    plt.savefig(os.path.join(r'{}'.format(direc_graphs),"{}_{}_{}_{}_{}.png".format(t_title,h_title,a_name,b_name,c_name)), format="png", dpi=resolution_value)


# Plot v, dir, t

def plot_v_dir_t(path_pf,pf_2d_array,a_name,b_name,c_name,df,df_ventos,data,highlight=0):
    '''Takes path of Perdigão file (str), data from Perdigão file (2D np array of float), first variable name(str), second variable name(str), third variable name(str), data frame with Perdigão data (pandas DataFrame), data frame with VENTOS®/M data (pandas DataFrame), data from VENTOS®/M file (2D np array of float), flag variable to learn if the shaded area of the last 24h is to be displayed or not, returns none'''
    a1 = df.columns.get_loc(a_name)
    b1 = df.columns.get_loc(b_name)
    c1 = df.columns.get_loc(c_name)
    a2 = df_ventos.columns.get_loc(a_name)
    b2 = df_ventos.columns.get_loc(b_name)
    c2 = df_ventos.columns.get_loc(c_name)

    # Plot formatting:
    plt.rcParams['font.family'] = 'sans-serif'
    #plt.rcParams.update({'font.sans-serif':'Helvetica'})
    SMALL_SIZE = 10
    MEDIUM_SIZE = 12
    ANOT_SIZE = SMALL_SIZE - 2
    NUMBER_SIZE = SMALL_SIZE
    plt.rc('font', size=SMALL_SIZE)        # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)   # fontsize of the axes title
    plt.rc('axes', labelsize=16)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    shadecolor = 'lavenderblush'

    x = pf_2d_array[:, 1]
    xlim_l = int(x[0])
    xlim_r = int(x[-1])

    #

    fig = plt.figure()  # an empty figure with no axes

    resolution_value = 200

    plt.rcParams["figure.figsize"] = (12,6)

    plt.rcParams['figure.dpi'] = resolution_value

    t_title = tower_title(path_pf)
    h_title = sonic_title(path_pf)

    fig, ax_lst = plt.subplots(3, 1)  # a figure with a 2x2 grid of Axes
    
    #plt.subplots_adjust(hspace=0.3)

    fig.suptitle('Tower {} at {} height'.format(t_title, h_title), fontsize=18)
    
    #subtitle = 'Wind Speed Components  U,V,W'
    

    # A

    a_ylabel = y_labels(a_name)

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
    
    x = pf_2d_array[:,1]
    y1 = pf_2d_array[:,a1]

    y2 = data[:,a2]

    plt.plot(x, y1, 'teal', label='Measurements')
    plt.plot(x, y2, 'orangered', label='Simulation')
    
    if highlight == 1:
        
        axa.fill_between(x, 0, 1, where=x > 18*3600, color=shadecolor, alpha=0.5, transform=axa.get_xaxis_transform())
        
    
    
    #leg = axa.legend(loc='upper left', frameon=False)
    leg = axa.legend(frameon=False)

    # B

    b_ylabel = y_labels(b_name)

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

    y3 = pf_2d_array[:,b1]

    y4 = data[:,b2]

    plt.plot(x, y3, 'teal', x, y4, 'orangered')
    
    if highlight == 1:
        
        axb.fill_between(x, 0, 1, where=x > 18*3600, color=shadecolor, alpha=0.5, transform=axb.get_xaxis_transform())
        

    # C

    c_ylabel = y_labels(c_name)

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
    axc.annotate('May 14', (0.06, 0.05), xycoords='figure fraction', fontsize=ANOT_SIZE, color='k')
    axc.annotate('May 15', (0.5, 0.05), xycoords='figure fraction', fontsize=ANOT_SIZE, color='k')

    axc.set_xticks(ticks=xtcks)
    axc.set_xticklabels(lbl)
    #axc.annotate('a)', (.03, .82), xycoords='figure fraction', fontsize=SMALL_SIZE, color='k')
    #axc.annotate('b)', (.03, .57), xycoords='figure fraction', fontsize=SMALL_SIZE, color='k')
    #axc.annotate('c)', (.03, .3), xycoords='figure fraction', fontsize=SMALL_SIZE, color='k')

    y5 = pf_2d_array[:,c1]

    y6 = data[:,c2]

    plt.plot(x, y5, 'teal', x, y6, 'orangered')
    
    if highlight == 1:
        
        axc.fill_between(x, 0, 1, where=x > 18*3600, color=shadecolor, alpha=0.5, transform=axc.get_xaxis_transform())
        


    plt.savefig(os.path.join(r'{}'.format(direc_graphs),"{}_{}_{}_{}_{}.png".format(t_title,h_title,a_name,b_name,c_name)), format="png", dpi=resolution_value)


# Plot uu, vv, ww

def plot_variances(path_pf,pf_2d_array,df,df_ventos,data,highlight=0):
    '''Takes path of Perdigão file (str), data from Perdigão file (2D np array of float), data frame with Perdigão data (pandas DataFrame), data frame with VENTOS®/M data (pandas DataFrame), data from VENTOS®/M file (2D np array of float), flag variable to learn if the shaded area of the last 24h is to be displayed or not, returns none'''
    a_name = "uu"
    b_name = "vv"
    c_name = "ww"
    a1 = df.columns.get_loc(a_name)
    b1 = df.columns.get_loc(b_name)
    c1 = df.columns.get_loc(c_name)
    a2 = df_ventos.columns.get_loc(a_name)
    b2 = df_ventos.columns.get_loc(b_name)
    c2 = df_ventos.columns.get_loc(c_name)

    # Plot formatting:
    plt.rcParams['font.family'] = 'sans-serif'
    #plt.rcParams.update({'font.sans-serif':'Helvetica'})
    SMALL_SIZE = 10
    MEDIUM_SIZE = 12
    ANOT_SIZE = SMALL_SIZE - 2
    NUMBER_SIZE = SMALL_SIZE
    plt.rc('font', size=SMALL_SIZE)        # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)   # fontsize of the axes title
    plt.rc('axes', labelsize=16)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    shadecolor = 'lavenderblush'

    x = pf_2d_array[:, 1]
    xlim_l = int(x[0])
    xlim_r = int(x[-1])

    #

    fig = plt.figure()  # an empty figure with no axes

    resolution_value = 200

    plt.rcParams["figure.figsize"] = (12,6)

    plt.rcParams['figure.dpi'] = resolution_value

    t_title = tower_title(path_pf)
    h_title = sonic_title(path_pf)

    fig, ax_lst = plt.subplots(3, 1)  # a figure with a 2x2 grid of Axes

    fig.suptitle('Tower {} at {} height'.format(t_title, h_title), fontsize=18)
    
    #subtitle = 'Wind Speed Components  U,V,W'
    

    # A

    a_ylabel = y_labels(a_name)

    axa = plt.subplot(311)

    axa.set_ylabel(r'{}'.format(a_ylabel))
    #axa.set_ylim(0, 3)
    axa.set_xlim(xlim_l, xlim_r)
    axa.xaxis.set_tick_params(labelbottom=False)
    axa.grid(color='k', linestyle='-', linewidth=0.7, alpha=0.2)
    axa.yaxis.set_major_locator(MultipleLocator(1))
    axa.yaxis.set_minor_locator(MultipleLocator(0.2))
    axa.tick_params(which='major', length=7, width=1, direction='in', top=True, right=True)
    axa.tick_params(which='minor', length=3, width=1, direction='in', top=True, right=True)
    
    x = pf_2d_array[:,1]
    y1 = pf_2d_array[:,a1]

    y2 = data[:,a2]

    plt.plot(x, y1, 'teal', label='Measurements')
    plt.plot(x, y2, 'orangered', label='Simulation')
    
    if highlight == 1:
        
        axa.fill_between(x, 0, 1, where=x > 18*3600, color=shadecolor, alpha=0.5, transform=axa.get_xaxis_transform())
        
    
    
    #leg = axa.legend(loc='upper left', frameon=False)
    leg = axa.legend(frameon=False)

    # B

    b_ylabel = y_labels(b_name)

    axb = plt.subplot(312, sharex=axa)
    axb.set_ylabel(r'{}'.format(b_ylabel))
    # axb.xaxis.set_visible(False)
    axb.set_xticklabels([])
    axb.xaxis.set_tick_params(labelbottom=False)
    #axb.set_ylim(0, 3)
    # plt.setp(axb.get_xticklabels(), visible=False)
    axb.grid(color='k', linestyle='-', linewidth=0.7, alpha=0.2)
    axb.yaxis.set_major_locator(MultipleLocator(1))
    axb.yaxis.set_minor_locator(MultipleLocator(0.2))
    axb.tick_params(which='major', length=7, width=1, direction='in', top=True, right=True)
    axb.tick_params(which='minor', length=3, width=1, direction='in', top=True, right=True)

    y3 = pf_2d_array[:,b1]

    y4 = data[:,b2]

    plt.plot(x, y3, 'teal', x, y4, 'orangered')
    
    if highlight == 1:
        
        axb.fill_between(x, 0, 1, where=x > 18*3600, color=shadecolor, alpha=0.5, transform=axb.get_xaxis_transform())
        

    # C

    c_ylabel = y_labels(c_name)

    axc = plt.subplot(313, sharex=axa)
    axc.set_ylabel(r'{}'.format(c_ylabel))
    axc.set_xlabel(r'Time')
    # plt.setp(axc.get_xticklabels(), visible=False)
    axc.grid(color='k', linestyle='-', linewidth=0.7, alpha=0.2)
    #axc.set_ylim(0, 1)
    axc.yaxis.set_major_locator(MultipleLocator(0.5))
    axc.yaxis.set_minor_locator(MultipleLocator(0.1))
    axc.tick_params(which='major', length=7, width=1, direction='in', top=True, right=True)
    axc.tick_params(which='minor', length=3, width=1, direction='in', top=True, right=True)
    xtcks = np.arange(0*3600, 43*3600, 3600*6)
    lbl = ['0:00','6:00', '12:00', '18:00', '00:00', '6:00', '12:00', '18:00']
    axc.annotate('May 14', (0.06, 0.05), xycoords='figure fraction', fontsize=ANOT_SIZE, color='k')
    axc.annotate('May 15', (0.505, 0.05), xycoords='figure fraction', fontsize=ANOT_SIZE, color='k')

    axc.set_xticks(ticks=xtcks)
    axc.set_xticklabels(lbl)
    #axc.annotate('a)', (.03, .82), xycoords='figure fraction', fontsize=SMALL_SIZE, color='k')
    #axc.annotate('b)', (.03, .57), xycoords='figure fraction', fontsize=SMALL_SIZE, color='k')
    #axc.annotate('c)', (.03, .3), xycoords='figure fraction', fontsize=SMALL_SIZE, color='k')

    y5 = pf_2d_array[:,c1]

    y6 = data[:,c2]

    plt.plot(x, y5, 'teal', x, y6, 'orangered')
    
    if highlight == 1:
        
        axc.fill_between(x, 0, 1, where=x > 18*3600, color=shadecolor, alpha=0.5, transform=axc.get_xaxis_transform())
        


    plt.savefig(os.path.join(r'{}'.format(direc_graphs),"{}_{}_{}_{}_{}.png".format(t_title,h_title,a_name,b_name,c_name)), format="png", dpi=resolution_value)


# Path VENTOS V2

def ventos_file_name_v3(dfv2_sonic,tower_p,height,direc):
    '''Takes VENTOS total sonic list (pandas data frame), designation of the tower (str), sonic height (str) and directory path (str), Returns file path (str)'''
    sonic_list = dfv2_sonic.loc[:,'sonic']
    
    sl = '!{}.{}m'.format(tower_p,height)
    if sl == '!v03.2m':
        
        i = 166
        
    else:
        
        i = sonic_list[sonic_list == sl].index[0]
        
    i +=1
    
    if i < 10:
        
        path_ventos_v = direc + r'\Simulações\all_sonics_v2\all_sonics_v2\af_series0000{}.plt'.format(i)
    
    if i > 9 and i < 100:
        
        path_ventos_v = direc + r'\Simulações\all_sonics_v2\all_sonics_v2\af_series000{}.plt'.format(i)
    
    if i > 99:
        
        path_ventos_v = direc + r'\Simulações\all_sonics_v2\all_sonics_v2\af_series00{}.plt'.format(i)

    return path_ventos_v


# Get df and np 2d array on perdigao data

def df_perdigao_file(path_pf):
    '''Takes path to Perdigão file (str), Returns data frame (pandas DataFrame) and 2D array (2D np array) containing processed data from the Perdigão file and data number of rows (int)'''
    df = pd.read_csv(r'{}'.format(path_pf), index_col=[0])
    
    k = int((df.iat[1, 1] - df.iat[0, 1])/2)

    dt = np.arange(0, len(df.index), dtype=int)

    for a in dt:
        
        df.iat[a, 1] = df.iat[a, 1] + k

    pf_2d_array = df.to_numpy()

    pf_num_rows = len(pf_2d_array)
    #pf_num_cols = len(pf_2d_array[0])
    
    return df, pf_2d_array, pf_num_rows


# Get df and np 2d array on VENTOS data

def df_ventos_file(tower_p,height,direc_v,path_v):
    '''Takes tower name (str), height (int), directory path (str), file path (str), Returns data frame (pandas DataFrame) and 2D array (2D np array) containing processed data from the VENTOS file'''
    dfv2_sonic = pd.read_csv(r'{}'.format(path_v))
    
    path_ventos_v = ventos_file_name_v3(dfv2_sonic, tower_p, height, direc_v)
    
    data = np.genfromtxt(r'{}'.format(path_ventos_v), skip_header=7)
    
    data = data[1:]
        
    df_ventos = pd.DataFrame(data, columns = ['seconds', 'TP', 'N^2', 'u', 'v', 'w', 'vh', 'dir', 'wdeg', 'shear', 'te_v', 'ti_v', 'tih_v', 'uu', 'vv', 'ww'])
    
    df_ventos = turbulence_5min_ventos(df_ventos)

    data = df_ventos.to_numpy()
    
    return df_ventos, data


# RMSE table

def tab_rmse_v(rmse,var,nhour,heights):
    '''Takes RMSE 3D array (np 3D array of float), variable flag (int), number of hours of the data (int), array with all heights for selected tower (np array of int), Returns data frame (pandas DataFrame) and 2D array (2D np array) containing hourly RMSE data, for the last 24h for the selected variable, in the selected tower'''
    rmse_v = rmse[-24:,var,:]
    rmse_v = rmse_v.T
    
    hours_array = np.arange(nhour)
    hours_array = hours_array[-24:]

    i1 = 0
    for a in hours_array:
        
        b = a%24
        hours_array[i1] = b
        i1 += 1
        
    df_rmse = pd.DataFrame(rmse_v,index=heights,columns=hours_array)
    
    return df_rmse, rmse_v


def tab_bias_v(bias,var,nhour,heights):
    '''Takes RMSE 3D array (np 3D array of float), variable flag (int), number of hours of the data (int), array with all heights for selected tower (np array of int), Returns data frame (pandas DataFrame) and 2D array (2D np array) containing hourly RMSE data, for the last 24h for the selected variable, in the selected tower'''
    bias_v = bias[-24:,var,:]
    bias_v = bias_v.T
    
    hours_array = np.arange(nhour)
    hours_array = hours_array[-24:]

    i1 = 0
    for a in hours_array:
        
        b = a%24
        hours_array[i1] = b
        i1 += 1
        
    df_bias = pd.DataFrame(bias_v,index=heights,columns=hours_array)
    
    return df_bias, bias_v


# Save function for rmse table

def save_rmse_table(df_rmse,path_pf,rmse_var,a_name,b_name,c_name,tower_p):
    '''Takes hourly RMSE data frame (pandas DataFrame), Perdigão file path (str), variable flag (int), names of the three chosen variables for plotting (3*str), tower name (str), Returns none'''
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
        

