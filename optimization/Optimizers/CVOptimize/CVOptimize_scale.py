import torch
import Tracker
import torch.optim as optim
import math

import numpy as np
import matplotlib.pyplot as plt


import sys
sys.path.append("../../Data/Scenarios")
sys.path.append("../../Data/Train")

import trainData 

dataPacks = trainData.trainDataPacks


dtype_torch = torch.float64
torch.autograd.set_detect_anomaly(True)

#helper functions

def calculateLoss(groundTruth, predictionMeasured):
    
    diff = groundTruth - predictionMeasured
    
    return torch.mm(diff.T, diff)



#to optimize

#########################################

scale = torch.tensor([
    0.192
], dtype= dtype_torch, requires_grad=True)


def getProcessNoiseCov():

    return    torch.tensor([
       [0.12958419304911287,0,0,0,0],
       [0,0.20416385918814656,0,0,0],
       [0,0,0.035931863724135523,0,0],
       [0,0,0,2.887976563803366,0],
       [0,0,0,0,0] 
     
    ], dtype=dtype_torch) * scale



#########################################
    


learningRate = 0.5

sequenceLength = 100


optimizer = optim.Adam([scale], lr = learningRate )

scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min', patience = 10, factor=0.5, verbose=True)

Tracker.ProcessNoiseCov = getProcessNoiseCov()
    



dt = 0.1

minimumSliceCount = float("inf")
batchSize = 25
initialThreshold = math.ceil(50 / sequenceLength)

losses_ = []

for dataPack in dataPacks:
    sliceCount = int(len(dataPack[0]) / sequenceLength)
    if(minimumSliceCount > sliceCount):
        minimumSliceCount = sliceCount
        
        

for epoch in range(100):
    
    losses = []
    trackers = []
    
    for _ in dataPacks:
        trackers.append(Tracker.Tracker_SingleTarget_SingleModel_CV_allMe())
    
    for s in range(minimumSliceCount):
        
        totalLoss = 0
        
        batches = []
        
        for b in range(math.ceil(len(dataPacks)/batchSize)):
            
            if((b+1)*batchSize > batchSize):
                batches.append(dataPacks[b*batchSize : ])
            else:
                batches.append(dataPacks[b*batchSize : (b+1)*batchSize])
                
        for b, batch in enumerate(batches):       
            
            loss = 0
        
            for l, dataPack in enumerate(batch):
                
                tracker = trackers[b*batchSize + l]
                
                measurementPacks = dataPack[0][s*sequenceLength: (s+1) * sequenceLength]
                groundTruthPacks = dataPack[1][s*sequenceLength: (s+1) * sequenceLength]
                
                for i, (measurementPack, groundTruthPack) in enumerate(zip(measurementPacks, groundTruthPacks)):
                    
                    z = tracker.feedMeasurement(torch.from_numpy(measurementPack[0]), dt)
                    if(z is not None and s >= initialThreshold):
                        loss += calculateLoss(torch.from_numpy(groundTruthPack[0]), z) / len(dataPacks) / sequenceLength
            
            if(loss != 0):
                loss.backward()
                totalLoss += loss.item()
                
                optimizer.step()
                optimizer.zero_grad()
            
            for l, _ in enumerate(batch):                
                tracker = trackers[b*batchSize + l]                
                tracker.detachTrack()
                
            Tracker.ProcessNoiseCov = getProcessNoiseCov()
        if(s == initialThreshold):
            print(totalLoss)
            print(scale)
            scheduler.step(totalLoss)
        losses.append(totalLoss)

    
    losses_.append(losses)

               
            
    







