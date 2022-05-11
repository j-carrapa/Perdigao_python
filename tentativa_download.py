# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:07:11 2022

@author: João
"""

# Tentativa de download automatico dos files todos


import requests
import numpy as np

dates = np.arange(627,631)

for date in dates:
    url1 = 'http://windsptds.fe.up.pt/thredds/fileServer/flux/NCAR-EOL%20Quality%20Controlled%205-minute%20ISFS%20surface%20flux%20data,%20geographic%20coordinate,%20tilt%20corrected/isfs_qc_tiltcor_20170'+ str(date) +'.nc'
    r = requests.get(url1)
    open(str(date)+'.nc','wb').write(r.content)


#Funcionou!!!


