""" elasticFace.py
    Object that handels feature extraction and comparison it uses consine distance as default.
"""
from .backbones.iresnet import iresnet100
from .distanceMetrics import cosineDistance, euclideanDistance, realEuclideanDistance
import torch
import os
from services.FaceImage import FaceImage
from services.searchProgress import progress

class ElasticFace:

    def __init__(self):
        self.backbone = iresnet100(num_features=512)
        self.distanceMetric = 'L2' # default value

    def setWeights(self,wName):
        PATH = os.getcwd()
        self.backbone.load_state_dict(torch.load(os.path.join(PATH,'elasticFace/backbones/weights/', wName), map_location=torch.device('cpu')))
        self.backbone.eval()

    def setDistanceMetric(self,metric):
        self.distanceMetric = metric

    def extractFeatures(self,imgTensor):
        return self.backbone(imgTensor)[0]

    def verifyFaces(self,refFace: FaceImage, gF: FaceImage,threshold: float):
        with torch.no_grad():
            match = False
            d = realEuclideanDistance(refFace.features, gF.features)
            if d <= float(threshold):
                match = True
            return (d, gF,match)