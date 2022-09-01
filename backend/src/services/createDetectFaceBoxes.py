from facenet_pytorch import MTCNN, extract_face
from PIL import Image
from config import config
from FaceImage import FaceImage

def findBoundingBoxes(imageFile):
    img = Image.open(imageFile)
    config.originalReferenceImage = img #set original image
    config.originalReferenceImage.filename = imageFile.filename
    rgb_img = img.convert('RGB')
    mtcnn = MTCNN(keep_all=True, device='cpu')
    boxes, probs, landmarks = mtcnn.detect(rgb_img, landmarks=True) #detect Faces and find boxes
    #saveFaces as images
    faces = []
    for box in boxes:
        faces.append(FaceImage(extract_face(rgb_img, box, image_size=112, margin=40),imageFile.filename,'refFaceImage',box,None))
    config.faces = faces
    return boxes
    #img.save('/Users/costa/Desktop/test.png')
