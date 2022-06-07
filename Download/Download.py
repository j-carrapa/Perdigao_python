# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:50:12 2022

@author: Joao
"""

import requests
import numpy as np


#dates def as a function?

# Download the netcd files defined by the user from perdigao site

def download (dates_def):
    print("Downloading...")

    # Just to explain user what is happening

    for date in dates_def:
        url = 'http://windsptds.fe.up.pt/thredds/fileServer/flux/NCAR-EOL%20Quality%20Controlled%205-minute%20ISFS%20surface%20flux%20data,%20geographic%20coordinate,%20tilt%20corrected/isfs_qc_tiltcor_'+ str(date) +'.nc'
        r = requests.get(url)
        open(str(date)+'.nc','wb').write(r.content)



'''
#Checking if the function is working - Apparently it is
dates_def = np.array([20170601, 20170602, 20170603])

download(dates_def)
#'''