class FaceImage:
    def __init__(self, img, originalName, folderName, box, features):
        self.img = img
        self.originalName = originalName
        self.folderName = folderName
        self.box = box
        self.features = features
