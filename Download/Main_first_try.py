# -*- coding: utf-8 -*-
"""
Created on Fri May 20 16:15:06 2022

@author: Joao
"""

# Main first try

g1 = 0

while g1 != 1:
    
    g2 = 0
    
    f_ans = input("Choose one option:\n[1] Manual sonic selection\n[2] All sonics in one mast\n[3]All sonics in choosen masts\n[4] All sonics for specified height\n[5] Sonics for specified height, in choosen masts\nPlease choose the number of the desired mode:")
    f_ans = int(f_ans)

    if f_ans == 1:
        import Mode_01_one_sonic_one_mast

    if f_ans == 2:
        import Mode_02_all_sonics_one_mast
        
    
        
    
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












'''

g1 = 0

while g1 != 1:
    
    #all the code for 1 sonic
    
    g2 = 0
    
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

        
'''
    
    