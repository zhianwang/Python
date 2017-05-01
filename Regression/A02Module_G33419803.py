# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 16:53:56 2016

@author: Zhian Wang
GWID: G33419803

This program is define 3 function to to compute the regression coefficients 
for the data in an input csv file and plot the regression.


"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import argparse as ap
from mpl_toolkits.mplot3d import *




# Part1 Read data
def fileInput(filename):
    """
    Input = name of csv text file with comma separated numbers
    Output = nunmpy array
    """
    myData = np.loadtxt(filename, delimiter = ',', dtype = float)
    return(myData)

# Part 2 Compute the regression coefficients    
def regress(myData):
    """
    Input = numpy array with three columns
    Column 1 is the dependent variable
    Column 2 and 3 are the independent variables
    Returns = a colum vector with the b coefficients and 
    """
    # In order to do multiple regression we need to add a column of 1s for x
    Data = np.array([np.concatenate((xi,[1])) for xi in myData])
    x = Data[:,1:4]
    y = myData[:,0]

    # Create linear regression object
    linreg = linear_model.LinearRegression()
    # Train the model using the training sets
    linreg.fit(x,y)
    
    # We can view the regression coefficients    
    B = np.concatenate(([linreg.intercept_], linreg.coef_), axis=0)
    b = B[0:3].reshape(3,1)
        
    from sklearn.metrics import r2_score
    pred = linreg.predict(x)
    r2 = r2_score(y,pred)
    
    return(b,r2)


# Part 3 Plot the regression        
def myPlot(myData,b):
    """
    Input = numpy array with three columns
    Column 1 is the dependent variable
    Column 2 and 3 are the independent variables
    and
    a cloumn vector with the b coefficients
    Reurns = Nothing
    Output = 3D plot of the actual data and
    the surface plot of the linear model
    """
    
    
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib import cm
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')               # to work in 3d
    plt.hold(True)
        
    x_max = max(myData[:,1])    
    y_max = max(myData[:,2])   
        
    b0 = float(b[0])
    b1 = float(b[1])
    b2 = float(b[2])   
        
    x_surf=np.linspace(0, x_max, 100)                # generate a mesh
    y_surf=np.linspace(0, y_max, 100)
    x_surf, y_surf = np.meshgrid(x_surf, y_surf)
    z_surf = b0 + b1*x_surf +b2*y_surf         # ex. function, which depends on x and y
    ax.plot_surface(x_surf, y_surf, z_surf, cmap=cm.hot, alpha=0.2);    # plot a 3d surface plot
        
    x=myData[:,1]
    y=myData[:,2]
    z=myData[:,0]
    ax.scatter(x, y, z);                        # plot a 3d scatter plot
        
    ax.set_xlabel('x1')
    ax.set_ylabel('y2')
    ax.set_zlabel('y')
    
    plt.show()
        
    
