# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 00:15:27 2019

@author: Andrew
"""



def merge_sort(X, inversion_count=0):
    
    if(len(X)==1):
        return(X, inversion_count)
        
    if(len(X)==2):
        if(X[0]>X[1]):
            X[0], X[1] = X[1], X[0]
            inversion_count = inversion_count + 1
        return(X, inversion_count)
    
    if(len(X)>2):
        Left, inversion_count = merge_sort(X[0:len(X)//2])
        Right, inversion_count = merge_sort(X[len(X)//2:len(X)])
        X_sorted = len(X)*[None]
        
        L_count=0
        R_count=0
        for i in range(0, len(X_sorted)):
            if(L_count==len(Left)):
                X_sorted[i:len(X_sorted)] = Right[R_count:len(Right)]
                break
                #R_count = R_count+1
            else:
                if(R_count==len(Right)):
                    X_sorted[i:len(X_sorted)] = Left[L_count:len(Left)]
                    break
                    #L_count = L_count+1
                else:
                    if(Left[L_count] < Right[R_count]):
                        X_sorted[i] = Left[L_count]
                        L_count = L_count+1
                    else:
                        X_sorted[i] = Right[R_count]
                        inversion_count = inversion_count + len(Left[L_count:len(Left)])
                        R_count = R_count+1
        
        return(X_sorted, inversion_count)


######################
######################
X_test_1 = [2, 5, 3, 0, -1, 5, 2.4, -65, -2.5, 0, 10]
merge_sort(X_test_1)

X_test_2 = list(range(5,-10,-1))
merge_sort(X_test_2)

X_test_3 = [1, 3, 5, 2, 4, 6]
merge_sort(X_test_3)
                    
            
            
            
            
            
            
        
        

