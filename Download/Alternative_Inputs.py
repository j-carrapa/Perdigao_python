# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 23:36:41 2022

@author: Joao
"""

# Alternative input code


# Mode_3 - tower loop

a1 = 0
a2 = 0
a3 = 0
a4 = 0

while a3 != 1:
    while a1 != 1:
        j = 0
        x = input("Tower name code:")
        for a in t_name:
            
            if x == a:
                
                if a2 == 1:
                    x_arr = np.append(x_arr, x)
                    j_arr = np.append(j_arr, j)
                    
                if a2 == 0:
                    x_arr = np.array(x)
                    j_arr = np.array(j)
                    a2 = 1
                
                a4 = 0   
                a1 = 1
                break
            j = j + 1
        if a1 != 1:
            print("Code name incorrect")
            
        continue
    
    while a4 != 1:
        
        t_ans = input("Get other tower?\n[yes/no]:")
        
        if t_ans == 'yes':
            a4 = 1
            a1 = 0
            break
            
        if t_ans == 'no':
            a4 = 1
            a3 = 1
            break
        
        if a4 == 0:
            print("Type correct answer")
            
        
    continue

if x_arr.size > 1:
    i = 0
    for x in x_arr:
        
        
        print(x)
        #print(j_arr[i])
        
        j = j_arr.item(i)
        print(j)
        i += 1
else:
    x = x0
    j = j0
    
'''-------------------------------'''