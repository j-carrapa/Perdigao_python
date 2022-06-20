# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:50:12 2022

@author: Joao
"""

import requests
import numpy as np

# Download the netcd files defined by the user from perdigao site

def download (dates_def):
    print("Downloading...")

    # Just to explain user what is happening
    
    if dates_def.size == 1:
        date = int(dates_def)
        url = 'http://windsptds.fe.up.pt/thredds/fileServer/flux/NCAR-EOL%20Quality%20Controlled%205-minute%20ISFS%20surface%20flux%20data,%20geographic%20coordinate,%20tilt%20corrected/isfs_qc_tiltcor_'+ str(date) +'.nc'
        r = requests.get(url)
        open(str(date)+'.nc','wb').write(r.content)
    else:
        for date in dates_def:
            url = 'http://windsptds.fe.up.pt/thredds/fileServer/flux/NCAR-EOL%20Quality%20Controlled%205-minute%20ISFS%20surface%20flux%20data,%20geographic%20coordinate,%20tilt%20corrected/isfs_qc_tiltcor_'+ str(date) +'.nc'
            r = requests.get(url)
            open(str(date)+'.nc','wb').write(r.content)