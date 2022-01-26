#Solution to Mean-Var-Std Calculator
#Created in Visual Studio Code
#By Michael Green

import numpy as np

'''*****************************************************************************
Name: calculate
*
Description: take a list of numbers, reshapes into 3x3 array, and calculate mean, variance, std, max, min, and sum from both axes and flat array.
*
Input: list_parameters- list of nine numbers.
*
Output: calculations- dictionary where keys= stat name and values = list of results [axis1, axis2, flat]
*****************************************************************************'''
def calculate(list_parameter):

    flattened_array = np.array(list_parameter)
    try:
        shaped_matrix = flattened_array.reshape(3,3)    #check for list of 9

    except:
        raise ValueError("List must contain nine numbers.")

    calculations = {'mean':[list(np.mean(shaped_matrix, axis=0)), 
                           list(np.mean(shaped_matrix, axis=1)), 
                            np.mean(flattened_array)], 
                    'variance':[list(np.var(shaped_matrix, axis=0)), 
                                list(np.var(shaped_matrix, axis=1)), 
                                np.var(flattened_array)], 
                    'standard deviation':[list(np.std(shaped_matrix, axis=0)), 
                                        list(np.std(shaped_matrix, axis=1)), 
                                        np.std(flattened_array)],
                    'max':[list(np.ma.max(shaped_matrix, axis=0)), 
                            list(np.ma.max(shaped_matrix, axis=1)), 
                            np.ma.max(flattened_array)], 
                    'min':[list(np.ma.min(shaped_matrix, axis=0)), 
                            list(np.ma.min(shaped_matrix, axis=1)), 
                            np.ma.min(flattened_array)], 
                    'sum':[list(np.sum(shaped_matrix, axis=0)), 
                            list(np.sum(shaped_matrix, axis=1)), 
                            np.sum(flattened_array)]}

    return calculations