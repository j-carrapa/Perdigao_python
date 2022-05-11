# -*- coding: utf-8 -*-
"""
Created on Thu May  5 01:02:58 2022

@author: João
"""

# Primeira abordagem aos ficheiros do perdigao

'''import netCDF4 as nc

fn = 'C:/Users/Baba/Desktop/João/Tese/Python/Teste_1/isfs_qc_tiltcor_20161129.nc'

ds = nc.Dataset(fn)'''# a dar erro



from netCDF4 import Dataset
tentativa1 = Dataset("isfs_qc_tiltcor_20170630.nc", "r", format="NETCDF4")

print(tentativa1.data_model)


print(tentativa1.dimensions)


print()

#print(tentativa1.variables)

#print(tentativa1)

#print(tentativa1.groups)

tentativa1.close()

#height = '10'
#twr = 'tse05
#u=np.array(ncfile[f'u_{height}m_])
