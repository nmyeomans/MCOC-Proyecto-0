# -*- coding: utf-8 -*-
"""
Created on Thu Aug 01 23:44:02 2019

@author: nico7
"""
import decimal
import scipy as sp
from matplotlib import pyplot
import sys
from numpy import*
import numpy as np


def valores_errores(valor_1):
    x=[]
    y=[]
    valor_16=float(array((valor_1),dtype=np.float16))
    valor_32=float(array((valor_1),dtype=np.float32))
    valor_64=float(array((valor_1),dtype=np.float64))
    print "Para el valor aleatorio: " , valor_1," se encuentran los siguientes errores:\n"
    
    error_16=(abs(valor_16-valor_1)/valor_1)*100
    error_32=(abs(valor_32-valor_1)/valor_1)*100
    error_64=(abs(valor_64-valor_1)/valor_1)*100
    print "Error dtype=np.float16 es :" , error_16, "%"
    print "Error dtype=np.float32 es :" , error_32, "%"
    print "Error dtype=np.float64 es :" , error_64,"%\n"
    #se crea una lista con las coordenada x correspondiente a los valores
    x.append(valor_16)
    x.append(valor_32)
    x.append(valor_64)
    #se crea una lista con las coordenadas y correspondientes al error    
    y.append(error_16)
    y.append(error_32)
    y.append(error_64)
    pyplot.plot(x,y,"o")
    pyplot.show()
    return " "
def valores_raiz_errores(valor_1):
    x=[]
    y=[]
    valor=valor_1**0.5
    valor_16=float(array((valor_1),dtype=np.float16))**0.5
    valor_32=float(array((valor_1),dtype=np.float32))**0.5
    valor_64=float(array((valor_1),dtype=np.float64))**0.5
    print "Para el valor aleatorio: ", valor," con raiz cuadrada :",valor," se encuentran los siguientes errores:\n"
    
    error_16=(abs(valor_16-valor)/valor)*100
    error_32=(abs(valor_32-valor)/valor)*100
    error_64=(abs(valor_64-valor)/valor)*100
    print "Error dtype=np.float16 es :" , error_16, "%"
    print "Error dtype=np.float32 es :" , error_32, "%"
    print "Error dtype=np.float64 es :" , error_64,"%\n"
    #se crea una lista con las coordenada x correspondiente a los valores
    x.append(valor_16)
    x.append(valor_32)
    x.append(valor_64)
    #se crea una lista con las coordenadas y correspondientes al error  
    y.append(error_16)
    y.append(error_32)
    y.append(error_64)
    pyplot.plot(x,y,"o")
    pyplot.show()
    return " "
print "\n"
print "Para el calculo del error se considera la siguiente formula :"
print " Error (%) = [|Valor flotante como array - Valor aleatorio|]/[ Valor aleatorio ] \n"
for i in range(3):
    valor_1=random.random()
    print valores_errores(valor_1)
    print valores_raiz_errores(valor_1)
    
    

    
        

      
