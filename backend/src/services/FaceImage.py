class FaceImage:
    def __init__(self, img, originalName, folderName, box, features, faceID):
        self.img = img
        self.originalName = originalName
        self.folderName = folderName
        self.box = box
        self.features = features
        self.faceID = faceID
