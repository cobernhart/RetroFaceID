"""main.py
"""
from faceRecognition.elasticFace import ElasticFace
from PIL import Image
from FaceImage import FaceImage
from torchvision import transforms
from facenet_pytorch import MTCNN, extract_face
import os
from config import config
from services.createOutputFolder import createOutputFolder




def frPipeline(refFaces,faceId):
    wPATH = os.getcwd()
    GALLERYPATH = config.galleryPath  # path to gallery

    """all weights are obtained with elasticface arc+, place"""
    # 0-5 ArcFace+ | 7 ArcFace
    weights = ['1-arc-backbone.pth','2-cos-backbone.pth','3-arc+-backbone.pth', '4-cos+-backbone.pth']
    listImages = []
    elasticFace = ElasticFace()
    elasticFace.setWeights(os.path.join(weights[3]))
    mtcnn = MTCNN(image_size=112, margin=40, thresholds=[0.6, 0.7, 0.7], keep_all=True, post_process=False, device='cpu')

    refFace = refFaces[faceId]
    refFace.img = (refFace.img / 255 - 0.5) / 0.5
    refFace.features = elasticFace.extractFeatures(refFace.img.unsqueeze(0))
    faceGallery = []
    faceBOXES = []
    imagePATHlist = os.listdir(GALLERYPATH)
    #loop through all images in folders
    for imagePATH in imagePATHlist:
        if ".jpg" not in imagePATH and ".jpeg" not in imagePATH and ".png" not in imagePATH:
            continue  # if it is not an image file -> ignore and continue
        img = Image.open(os.path.join(wPATH, GALLERYPATH, imagePATH))
        # DO PREPROCESSING
        faceBOX, probs = mtcnn.detect(img, landmarks=False) ## detected face boxes
        for count, box in enumerate(faceBOX):
            face = extract_face(img, box, image_size=112, margin=40)
            face = (face / 255 - 0.5) / 0.5
            sImage = FaceImage(img, imagePATH, box,
                               elasticFace.extractFeatures(face.unsqueeze(0)))
            listImages.append(sImage)
    distances = elasticFace.verifyFaces(refFace, listImages, config.threshold)
    createOutputFolder(config.originalReferenceImage,refFace.box, distances)

