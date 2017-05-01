# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 22:33:40 2016

@author: Zhian Wang
GWID: G33419803

This program is used to call the fileinput, regression and plot function.
Besides the default output, user can choose other different outputs through '-b','-v','-p' and '-o'
"""

import A02Module_G33419803

import argparse as ap


def Main():
    myP = ap.ArgumentParser()
    
    myGroup = myP.add_mutually_exclusive_group()
    myGroup.add_argument("-b","--brief", action = "store_true")
    myGroup.add_argument("-v","--verbose", action = "store_true")
    myGroup.add_argument("-p","--plot", action = "store_true")
    
    myP.add_argument("myFile", help="The name of csv txt file to caculate")
    myP.add_argument("-o", "--output", dest='outfile', help="output file")
    
    myArgs = myP.parse_args()
    
    myData = A02Module_G33419803.fileInput(myArgs.myFile)
    b, r2 = A02Module_G33419803.regress(myData)

#This is the brief output    
    if myArgs.brief:
        print ("b0 = %.2f" % (b[0]))
        print ("b1 = %.2f" % (b[1]))
        print ("b2 = %.2f" % (b[2]))

#This is the verbose output
    elif myArgs.verbose:
        print ("The equation is: \ny = %.2f + %.2fx1 + %.2fx2" % (b[0],b[1],b[2]))
        print ("The R-square value is: %.2f" % (r2))
        #print the actual data values
        print ("The formatted input data is shown below:")
        # print header   
        s = '{:>3}'.format('y')
        s = s + '{:>8}'.format('x1')
        s = s + '{:>8}'.format('x2')
        print (s)
        #print line
        print ("="*3*7) 
        #print table
        for y,x1,x2 in myData:
               print ("{:.2f}\t{:.2f}\t{:.2f}".format(y,x1,x2))
        
#This is the default output        
    else:
        print ("b0 = %.2f" % (b[0]))
        print ("b1 = %.2f" % (b[1]))
        print ("b2 = %.2f" % (b[2]))
        print ('R-Square = %.2f' % (r2))


#This is the output with plot        
    if myArgs.plot:
        A02Module_G33419803.myPlot(myData, b)
        
#This is the output file        
    if myArgs.outfile:
        #creating a list containing all outputs
        text = list()
        text.append("The equation is: \ny = %.2f + %.2fx1 + %.2fx2" % (b[0],b[1],b[2]))
        text.append("\nThe R-square value is: %.2f" % (r2))
        text.append("\nThe formatted input data is shown below:")
        text.append("\n")
        s = '{:>3}'.format('y')
        s = s + '{:>8}'.format('x1')
        s = s + '{:>8}'.format('x2')
        text.append(s)
        text.append("\n")
        text.append("="*3*7)
        for y,x1,x2 in myData:
            text.append("\n")
            text.append("{:.2f}\t{:.2f}\t{:.2f}".format(y,x1,x2))
        
        with open(myArgs.outfile, 'a') as f:
            for i in text:
                f.write(i)
            print ("Output being sent to " + str(myArgs.outfile))



# Main Function

if __name__ == "__main__":
    Main()