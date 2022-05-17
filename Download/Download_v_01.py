# -*- coding: utf-8 -*-
"""
Created on Fri May  6 16:06:07 2022

@author: João
"""

# Download v.01

'''este módulo destina-se a fazer o download dos ficheiros .nc do site do Perdigão
a primeira parte do código - PARTE 1 - serve para criar um array que contém
os códigos de data que existem para cada ficheiro diferente
Posteriormente esse array servirá para fazer a iteração de 
download de todos os ficheiros na - PARTE 2 -.'''

# Módulo está funcional, faz download automático dos ficheiros do site do perdigão
#Neste caso está a ir buscar os ficheiros "NCAR-EOL Quality Controlled 5-minute ISFS surface flux data, geographic coordinate, tilt corrected"
#Após o download os ficheiros ficam com a seguinte designação: 'YYYYMMDD.nc'

# Próximos passos:
# se o ficheiro já existir, saltar o download, para evitar duplicados
# criar outro módulo que serve de interface para selecionar outro tipo de dados para download



import requests
import numpy as np



'''----- PARTE 1 ----------'''

# The array 'dates' will contain all the dates of the days with available data

dates = np.array([20161129, 20161201, 20161202, 20161205], dtype='i4')


i = 7


while i<10:
    s = '2016120'+ str(i)
    temp = np.array(s, dtype='i4')
    dates = np.append(dates, [temp])
    i = i+1

dates = np.append(dates, [20161210])

# Array with the dates of the days with available data for the months of November and Dezember of 2016

dates_16 = dates

# Filling the 'dates' array with the remaining dates of the year 2017

j = 1
i = 16

# Array with the dates of the days with available data for the months from January until July of 2017

# 1- January, 3- March, 5- May months with 31 days
# 2- February - 29 days
# 4- April, 6- June

while j<7:
    if j == 1 or j == 3 or j == 5:
        while i < 10:
            s = '20170' + str(j)+'0'+ str(i)
            temp = np.array(s, dtype='i4')
            dates = np.append(dates, [temp])
            i = i+1
        else:
            while i <32:
                s = '20170' + str(j)+ str(i)
                temp = np.array(s, dtype='i4')
                dates = np.append(dates, [temp])
                i = i+1
            else:
                i=1
        
    if j == 2:
        while i <10:
            s = '20170' + str(j)+ '0' + str(i)
            temp = np.array(s, dtype='i4')
            dates = np.append(dates, [temp])
            i = i+1
        else:
            while i <29:
                s = '20170' + str(j)+ str(i)
                temp = np.array(s, dtype='i4')
                dates = np.append(dates, [temp])
                i = i+1
            else:
                i = 1
    if j == 4 or j == 6:
        while i <10:
            s = '20170' + str(j)+ '0' + str(i)
            temp = np.array(s, dtype='i4')
            dates = np.append(dates, [temp])
            i = i+1
        else:
            while i < 31:
                s = '20170' + str(j)+ str(i)
                temp = np.array(s, dtype='i4')
                dates = np.append(dates, [temp])
                i = i+1
            else:
                i = 1
    j = j+1

else:
    dates = np.append(dates, [20170701])


dates_tot = dates

#print(dates)
#just for checking


'''----- PARTE 2 ----------'''

#esta parte foi retirada de : https://www.youtube.com/watch?v=XGUS6DYZfCc&list=PLLxyyob7YmEE8S3QDs1PZQkiBxA4zn_Gx&index=7
#antes
'''
for date in dates:
    url = 'http://windsptds.fe.up.pt/thredds/fileServer/flux/NCAR-EOL%20Quality%20Controlled%205-minute%20ISFS%20surface%20flux%20data,%20geographic%20coordinate,%20tilt%20corrected/isfs_qc_tiltcor_201'+ str(date) +'.nc'
    r = requests.get(url)
    open('201' + str(date)+'.nc','wb').write(r.content)
'''

#Depois

for date in dates:
    url = 'http://windsptds.fe.up.pt/thredds/fileServer/flux/NCAR-EOL%20Quality%20Controlled%205-minute%20ISFS%20surface%20flux%20data,%20geographic%20coordinate,%20tilt%20corrected/isfs_qc_tiltcor_'+ str(date) +'.nc'
    r = requests.get(url)
    open(str(date)+'.nc','wb').write(r.content)






