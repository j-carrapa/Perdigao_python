# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:49:20 2022

@author: João
"""

# Directories File - Contains functions to define directories, sub_directories and other paths

# When the app is downloaded it is necessary to change the main directory path so that the app can work propperly

'''-------- Changeable directory ----------------'''

def main_directory():
    '''Takes none, Returns main directory path (string)'''
    d = r'C:\Users\Baba\Desktop\João\Tese\Python\Perdigao_github'
    return d

'''-----------------------------------------------'''


# Shouldn't be necessary to change these functions


def perdigao_files_directory(main_d):
    '''Takes none, Returns perdigão files directory path (string)'''
    d = r'{}\perdigao_data_retriever_app\data_pf'.format(main_d)
    return d


def raw_files_directory(main_d):
    '''Takes none, Returns raw files directory path (string)'''
    d = r'{}\perdigao_data_retriever_app\raw_files'.format(main_d)
    return d

