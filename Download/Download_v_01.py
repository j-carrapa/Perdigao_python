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

# Dias de Novembro e Dezembro de 2016 - meses em que não existem dados para todos os dias

dates = np.array([61129, 61201, 61202, 61205], dtype='i4')

i = 7


while i<10:
    s = '6120'+ str(i)
    temp = np.array(s, dtype='i4')
    dates = np.append(dates, [temp])
    i = i+1

dates = np.append(dates, [61210])




j = 1
i = 16

# 1- Janeiro, 3- Março, 5- Maio meses de 31 dias
# 2- Fevereiro - 29 dias
# 4- Abril, 6- Junho

while j<7:
    if j == 1 or j == 3 or j == 5:
        while i < 10:
            s = '70' + str(j)+'0'+ str(i)
            temp = np.array(s, dtype='i4')
            dates = np.append(dates, [temp])
            i = i+1
        else:
            while i <32:
                s = '70' + str(j)+ str(i)
                temp = np.array(s, dtype='i4')
                dates = np.append(dates, [temp])
                i = i+1
            else:
                i=1
        
    if j == 2:
        while i <10:
            s = '70' + str(j)+ '0' + str(i)
            temp = np.array(s, dtype='i4')
            dates = np.append(dates, [temp])
            i = i+1
        else:
            while i <29:
                s = '70' + str(j)+ str(i)
                temp = np.array(s, dtype='i4')
                dates = np.append(dates, [temp])
                i = i+1
            else:
                i = 1
    if j == 4 or j == 6:
        while i <10:
            s = '70' + str(j)+ '0' + str(i)
            temp = np.array(s, dtype='i4')
            dates = np.append(dates, [temp])
            i = i+1
        else:
            while i < 31:
                s = '70' + str(j)+ str(i)
                temp = np.array(s, dtype='i4')
                dates = np.append(dates, [temp])
                i = i+1
            else:
                i = 1
    j = j+1

else:
    dates = np.append(dates, [70701])

#print(dates)
#Só para verificação


'''----- PARTE 2 ----------'''

#esta parte foi retirada de : https://www.youtube.com/watch?v=XGUS6DYZfCc&list=PLLxyyob7YmEE8S3QDs1PZQkiBxA4zn_Gx&index=7

for date in dates:
    url = 'http://windsptds.fe.up.pt/thredds/fileServer/flux/NCAR-EOL%20Quality%20Controlled%205-minute%20ISFS%20surface%20flux%20data,%20geographic%20coordinate,%20tilt%20corrected/isfs_qc_tiltcor_201'+ str(date) +'.nc'
    r = requests.get(url)
    open('201' + str(date)+'.nc','wb').write(r.content)









