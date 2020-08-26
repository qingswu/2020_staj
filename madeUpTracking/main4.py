# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import Scenarios.scenario as scn
import copy

from Trackers.MultipleTarget.allMe.track_multipleTarget_multipleModel import Tracker_MultipleTarget_MultipleModel_allMe

from myHelpers.visualizeHelper import showPerimeter
from myHelpers.visualizeHelper import showRadius
from myHelpers.visualizeHelper import visualizeTrackingResults

#%matplotlib qt
#scn.scenario_2.plotScenario()

def extractMeasurementsFromScenario(scenario):
    measurementPacks = []
    i = 0
    exhausteds = np.zeros((len(scenario.objects)))
    done = False

    while(not done):
        measurementPack = []
        for k,object_ in enumerate(scenario.objects):

            if(len(object_.xPath) > i):
                if(object_.xNoisyPath[i] is not None):
                    measurementPack.append(np.expand_dims(np.array([object_.xNoisyPath[i], object_.yNoisyPath[i]]), axis=1))
            else:
                exhausteds[k] = 1
        if(np.sum(exhausteds) > len(scenario.objects)-1):
            done = True
            
        if(not done):
            measurementPacks.append(measurementPack)
        i += 1
    
    return measurementPacks

def extractGroundTruthFromScenario(scenario):
    groundTruthPacks = []
    
    for k, object_ in enumerate(scenario.objects):
        
        groundTruthX = object_.xPath
        groundTruthY = object_.yPath
        
        groundTruthPacks.append((groundTruthX, groundTruthY))
    
    return groundTruthPacks



measurementPacks = extractMeasurementsFromScenario(scn.scenario_3)
groundTruthPacks = extractGroundTruthFromScenario(scn.scenario_3)

scn.scenario_3.plotScenario()



gateThreshold = 10
distanceThreshold = 5
spatialDensity = 0.0008
detThreshold = 400
PD = 0.99

dt = 0.1


multipleTargetTracker = Tracker_MultipleTarget_MultipleModel_allMe(gateThreshold, distanceThreshold, detThreshold, spatialDensity, PD)


for i, measurementPack in enumerate(measurementPacks):

    measurements = np.array(measurementPack)
    multipleTargetTracker.feedMeasurements(measurements, dt, i)
    


        
print("validationMatrix.shape = ", multipleTargetTracker.validationMatrix.shape)
print("associationEvents.shape = ", multipleTargetTracker.associationEvents.shape)


ani = visualizeTrackingResults(multipleTargetTracker.matureTrackerHistory, measurementPacks, groundTruthPacks, True, gateThreshold)
    
ani = visualizeTrackingResults(multipleTargetTracker.matureTrackerHistory, measurementPacks, groundTruthPacks, False, gateThreshold)
        
        
# targetTrack = multipleTargetTracker.matureTrackerHistory[0].models[0].trackHistory[-1][0]
# targetMixedStateHistory = multipleTargetTracker.matureTrackerHistory[0].models[0].mixedStateHistory[-1]

# print("targetTrack_xPredict :", targetTrack.x_predict)
# print("targetTrack_pPredict :", targetTrack.P_predict)

# print("targetMixedStateHistory_xMixed : ", targetMixedStateHistory[2])
# print("targetMixedStateHistory_xMixed : ", targetMixedStateHistory[3])

