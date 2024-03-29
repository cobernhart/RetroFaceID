"""main.py
"""
from .elasticFace.elasticFace import ElasticFace
from PIL import Image
from src.services.FaceImage import FaceImage
from facenet_pytorch import MTCNN, extract_face
import os
from .config import config
from src.services.searchProgress import progress
from src.services.outputService import createOutputFolder, saveImageInOutputFolder
from src.services.rotateImage import rotate_image


def loopImage(refFace, directory, listImages,elasticFace):
    wPATH = os.getcwd()
    imagePATHlist = os.listdir(directory)
    mtcnn = MTCNN(image_size=112, margin=40, thresholds=[0.6, 0.7, 0.7], keep_all=True, post_process=False, device='cpu')

    # loop through all images in folders
    for imagePATH in imagePATHlist:
        if config.runSearch is False:
            return
        if ".jpg" not in imagePATH and ".jpeg" not in imagePATH and ".png" not in imagePATH and ".tiff" not in imagePATH:
            if os.path.isdir(os.path.join(directory,imagePATH)):
                loopImage(refFace, os.path.join(directory,imagePATH),listImages,elasticFace) #recursive call do loop through folder recusively
            continue  # if it is not an image file -> ignore and continue
        elif imagePATH.startswith('.'): #some not readable files that have same types like images
            continue
        img = Image.open(os.path.join(wPATH, directory, imagePATH))
        if ".tiff" in imagePATH:
            img = img.convert("RGB")
        progress.imageCount = progress.imageCount + 1
        # DO PREPROCESSING
        faceBOX, probs,landmarks = mtcnn.detect(img, landmarks=True)  ## detected face boxes
        if faceBOX is None: #no faces detected
            continue
        for count, box in enumerate(faceBOX):
            alignedImage = rotate_image(img, landmarks[count])
            face = extract_face(alignedImage, box, image_size=112, margin=40)
            face = (face / 255 - 0.5) / 0.5
            sImage = FaceImage(img, imagePATH, directory, box,
                               elasticFace.extractFeatures(face.unsqueeze(0)),count)
            progress.faceCount = progress.faceCount + 1
            # listImages.append(sImage) #neeeds to be remove
            distance,match, matchBool =  elasticFace.verifyFaces(refFace, sImage, config.threshold) #check if match
            if matchBool:
                progress.matchCount = progress.matchCount + 1
                saveImageInOutputFolder((distance,match))



def frPipeline(refFaces,faceId):
    wPATH = os.getcwd()
    GALLERYPATH = config.galleryPath  # path to gallery
    listImages = []
    """all weights are obtained with elasticface arc+, place"""
    # 0-5 ArcFace+ | 7 ArcFace
    weights = ['1-arc-backbone.pth','2-cos-backbone.pth','3-arc+-backbone.pth', '4-cos+-backbone.pth','5-arcface-backbone.pth']
    elasticFace = ElasticFace()
    weight = None
    if config.method == 'efArc':
        weight = weights[0]
    elif config.method == 'efCos':
        weight = weights[1]
    elif config.method == 'efArc+':
        weight = weights[2]
    elif config.method == 'efCos+':
        weight = weights[3]
    else:
        weight = weights[4]

    elasticFace.setWeights(os.path.join(weight))
    refFace = refFaces[faceId]
    refFace.img = (refFace.img / 255 - 0.5) / 0.5
    refFace.features = elasticFace.extractFeatures(refFace.img.unsqueeze(0))
    faceGallery = []
    faceBOXES = []
    createOutputFolder(config.originalReferenceImage, refFace)
    loopImage(refFace,GALLERYPATH,listImages,elasticFace)

    #matches = elasticFace.verifyFaces(refFace, listImages, config.threshold)


