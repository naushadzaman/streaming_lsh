'''
Created on Jul 5, 2011

@author: kykamath
'''
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def getLatexForString(str): return '$'+str.replace(' ', '\\ ')+'$'

class CurveFit():
    '''
    Exponential funcion: a.x^-b
    '''
    exponentialFunction = lambda p, x: p[0]*pow(x, -1*p[1])
    
    def __init__(self, functionToFit, initialParameters, dataX, dataY): 
        self.functionToFit, self.initialParameters, self.dataX, self.dataY = functionToFit, initialParameters, dataX, dataY
        if self.functionToFit != None: self.error = lambda p, x, y: self.functionToFit(p, x) - y
    def estimate(self, polyFit=None): 
        if polyFit == None: self.actualParameters, self.success = scipy.optimize.leastsq(self.error, self.initialParameters, args=(self.dataX, self.dataY))
        else: self.actualParameters = np.polyfit(self.dataX, self.dataY, polyFit)
    def errorVal(self):
        xfit=np.polyval(self.actualParameters, self.dataX)
        return scipy.sqrt(sum((self.dataX-xfit)**2)/len(xfit))
    def plot(self, xlabel='', ylabel='', title='', color = 'r'):
        plt.plot(self.dataX, self.dataY, 'o')
        plt.plot(self.dataX, self.functionToFit(self.actualParameters, self.dataX), 'o', color=color)
        plt.xlabel(xlabel), plt.ylabel(ylabel), plt.title(title)
        plt.show()
    def getModeledYValues(self): return self.functionToFit(self.actualParameters, self.dataX)
    @staticmethod
    def getParamsAfterFittingData(x, y, functionToFit, initialParameters):
        cf = CurveFit(functionToFit, initialParameters, x, y)
        cf.estimate()
        return cf.actualParameters
    @staticmethod
    def iterator(functionToFit, params, x): 
        for i in x: yield functionToFit(params, i)
    @staticmethod
    def getParamsForExponentialFitting(x,y): return CurveFit.getParamsAfterFittingData(x, y, CurveFit.exponentialFunction, [1., 1.])
    @staticmethod
    def exponentialIterator(params,x): CurveFit.iterator(CurveFit.exponentialFunction, params, x)
        
    