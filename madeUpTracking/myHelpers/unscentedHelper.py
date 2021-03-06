from scipy.linalg import cholesky
import numpy as np


"""
    References: 
        [WR00] The Unscented Kalman Filter for Nonlinear Estimation, Eric A. Wan and Rudolph van der Merwe
"""

def generateUnscentedWeights(L, alpha, beta, kappa): #checkCount : 1
    """
        Description:
            [WR00 Equation 15]
        Input:
            L: float
            alpha: float
            beta: float
            kappa: float
    """

    lambda_ = (alpha ** 2) * (L + kappa) - L


    Ws0 = lambda_ / (L + lambda_)
    Wc0 = lambda_ / (L + lambda_) + (1 - alpha**2 + beta)

    Wsi = 0.5 / (L + lambda_)
    Wci = 0.5 / (L + lambda_)

    return ([Ws0, Wsi],[Wc0, Wci], lambda_)

def generateSigmaPoints(stateMean, stateCovariance, lambda_): #checkCount : 1

    """
        Description:
            [WR00 Equation 15]
        Input:
            stateMean: np.array(shape = (dimX,1))
            stateCovariance: np.array(shape = (dimX, dimX))
            lambda_: float
        
        Output:
            sigmaPoints : np.array(shape = (dimX*2 + 1, dimX, 1))

    """

    L = stateMean.shape[0]

    sigmaPoints = [stateMean]

    sqrtMatrix = cholesky((L + lambda_) * stateCovariance)

    for i in range(L):
        sigmaPoints.append( stateMean + np.expand_dims(sqrtMatrix[i],axis=1) )
        sigmaPoints.append( stateMean - np.expand_dims(sqrtMatrix[i],axis=1) )
        

    return np.array(sigmaPoints, dtype="float")

def predictNextState(forwardFunc, dt, sigmaPoints, Ws, Wc, processNoise):

    """
        Description:
            Predicts the next state
        
        Input:
            forwardFunc : function
            dt: float
            sigmaPoints : np.array(shape = (2*dimX +1, dimX, 1))
            Ws : [Ws0, Wsi] -> only 2 elements
            Wc : [Wc0, Wci] -> only 2 elements
            processNoise : np.array(shape = (dimX, dimX))
        
        Output:
            predictedStateMean : np.array(shape = (dimX, 1))
            predictedStateCovariance : np.array(shape = (dimX, dimX))
    """
    
    sigmaStarPoints_state = []
    
    for sigmaPoint in sigmaPoints:
        sigmaStarPoints_state.append(forwardFunc(sigmaPoint,dt))

    
    sigmaStarPoints_state = np.array(sigmaStarPoints_state)
    
    predictedStateMean = Ws[0] * sigmaStarPoints_state[0] + Ws[1] * np.sum(sigmaStarPoints_state[1:], axis = 0)


    predictedStateCovariance = None 

    for i,sigmaStarPoint_state in enumerate(sigmaStarPoints_state):
        
        if(predictedStateCovariance is None):
            predictedStateCovariance = Wc[0] * np.dot((sigmaStarPoint_state - predictedStateMean), (sigmaStarPoint_state-predictedStateMean).T)
        else:
            predictedStateCovariance += Wc[1] * np.dot((sigmaStarPoint_state - predictedStateMean), (sigmaStarPoint_state-predictedStateMean).T)
    
    
    predictedStateCovariance += processNoise  

    return (predictedStateMean, predictedStateCovariance)  

    

def calculateUpdateParameters(predictedStateMean, predictedStateCovariance, measureFunc, sigmaPoints, Ws, Wc, measurementNoise): #checkCount : 1

    """
    
        Description : 
            Calculates the predicted state
            [WR00 Algorithm 3.1]
    
        Input:

            predictedStateMean : np.array(shape = (dimX, 1))
            predictedStateCovariance : np.array(shape = (dimX, dimX))
            measureFunc : function
            sigmaPoints : np.array(shape = (2*dimX + 1, dimX, 1))
            Ws : [Ws0, Wsi] -> only 2 elements
            Wc : [Wc0, Wci] -> only 2 elements
            measurementNoise : np.array(shape = (dimZ, dimZ))
        
        Output:
            S : np.array(shape = (dimZ, dimZ))
            kalmanGain : np.array(shape = (dimX, dimZ))
            predictedMeasureMean : np.array(shape = (dimZ,1))

            
    """
    sigmaStarPoints_measure = []
    
    for sigmaPoint in sigmaPoints:
        
        sigmaStarPoint_measure = measureFunc(sigmaPoint)

        sigmaStarPoints_measure.append(sigmaStarPoint_measure)
    
    sigmaStarPoints_measure = np.array(sigmaStarPoints_measure)

    predictedMeasureMean = Ws[0] * sigmaStarPoints_measure[0] + Ws[1] * np.sum(sigmaStarPoints_measure[1:], axis = 0)
    

    Pzz = None
    Pxz = None

    for i, sigmaPoint in enumerate(sigmaPoints):

        sigmaStarPoint_measure = sigmaStarPoints_measure[i]

        if(Pzz is None):
            Pzz = Wc[0] * np.dot((sigmaStarPoint_measure - predictedMeasureMean), (sigmaStarPoint_measure - predictedMeasureMean).T)
            Pxz = Wc[0] * np.dot((sigmaPoint - predictedStateMean), (sigmaStarPoint_measure - predictedMeasureMean).T)
        else:
            Pzz += Wc[1] * np.dot((sigmaStarPoint_measure - predictedMeasureMean), (sigmaStarPoint_measure - predictedMeasureMean).T)
            Pxz += Wc[1] * np.dot((sigmaPoint - predictedStateMean), (sigmaStarPoint_measure - predictedMeasureMean).T)               
    
    
    S = Pzz + measurementNoise
    
    kalmanGain = np.dot(Pxz, np.linalg.inv(S))

    return (S, kalmanGain, predictedMeasureMean)



