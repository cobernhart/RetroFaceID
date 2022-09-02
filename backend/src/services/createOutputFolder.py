from config import config
from PIL import Image
import os
import numpy as np
import matplotlib.patches as patches
from matplotlib import pyplot as plt
import shutil
import csv

def createOutputFolder(originalImage,refFaceBox, matches):
    if os.path.exists(config.outputPath):
        config.errorMessage = "Output directory exists already -> please choose a new name"
        abort(422)
    os.mkdir(config.outputPath) #createOutputFolder
    #first save original referece image
    originalImage.save(os.path.join(config.outputPath,"reference-original-"+ originalImage.filename))
    #save face cropped image
    refCropped = originalImage.crop(refFaceBox)
    refCropped.save(os.path.join(config.outputPath,"reference-cropped-face-"+ originalImage.filename))
    #create image matched folder
    MATCHED_FOLDER_PATH = os.path.join(config.outputPath,"image-matched-folder")
    os.mkdir(MATCHED_FOLDER_PATH)
    #create csv file
    header = ['fileName', 'similarityMeasure', 'parentFolderName']
    with open(os.path.join(config.outputPath,"matches-list.csv"), 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for match in matches:
            d, faceImg = match
            data = [faceImg.originalName, d, faceImg.folderName]
            writer.writerow(data)
            #faceImg.img.save(os.path.)join(MATCHED_FOLDER_PATH,"m-"+ faceImg.originalName));
            # Created matched photo
            fig, ax = plt.subplots()
            ax.imshow(faceImg.img)
            ax.axis('off')
            box = faceImg.box
            sc = ax.add_patch(patches.Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1], edgecolor='red',facecolor='none', linewidth=2))
            fig.savefig(os.path.join(MATCHED_FOLDER_PATH,"m-"+ faceImg.originalName), bbox_inches='tight')