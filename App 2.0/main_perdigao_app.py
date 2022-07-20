# -*- coding: utf-8 -*-
"""
Created on Fri May 20 16:15:06 2022

@author: Joao
"""

# Falta refazer mode 2 e 3 e limpar main. mode 1 já está

# Main - Top level module, user interface to run sub-modules

# Allows to choose one mode of data gathering, process and export and repeat the operation

g1 = 0

while g1 != 1:
    
    g2 = 0
    
    f_ans = input("Choose one option:\n[1] Multiple sonics, multiple masts\n[2] All sonics, multiple masts\n[3] All masts, multiple sonic heights\nPlease choose the number of the desired mode:")
    f_ans = int(f_ans)

    if f_ans == 1:
        import mode_01_multiple_sonics_multiple_masts

    if f_ans == 2:
        import mode_02_all_sonics_multiple_masts
        
    if f_ans == 3:
        import mode_03_all_masts_multiple_sonics
    
    while g2 != 1:
        g_ans = input("End of data gathering?\n[yes/no]:")
        
        if g_ans == 'no':
            g2 = 1
            continue
        if g_ans == 'yes':
            g2 = 1
            g1 = 1
            continue
        else:
            print("Type correct answer.\n[yes/no]:")
            continue
    continue