from facenet_pytorch import MTCNN, extract_face
from PIL import Image
from config import config
from services.rotateImage import rotate_image
from FaceImage import FaceImage

def findBoundingBoxes(imageFile):
    img = Image.open(imageFile)
    config.originalReferenceImage = img #set original image
    config.originalReferenceImage.filename = imageFile.filename
    rgb_img = img.convert('RGB')
    mtcnn = MTCNN(keep_all=True, device='cpu')

    faceDetected = mtcnn.detect(rgb_img, landmarks=True)#detect Faces and find boxes
    boxes, probs, landmarks = faceDetected
    #saveFaces as images
    faces = []
    for count, box in enumerate(boxes):
        alignedImage = rotate_image(rgb_img, landmarks[count])
        faces.append(FaceImage(extract_face(alignedImage, box, image_size=112, margin=40),imageFile.filename,'refFaceImage',box,None,count))
    config.faces = faces
    return boxes
    #img.save('/Users/costa/Desktop/test.png')
