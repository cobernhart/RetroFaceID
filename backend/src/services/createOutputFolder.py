from config import config
from PIL import Image
import os
import numpy as np
import matplotlib.patches as patches
from matplotlib import pyplot as plt
import shutil
import csv
import torchvision.transforms as T
import numpy as np
import matplotlib.pyplot as plt

def createOutputFolder(originalImage,refFace, matches):
    if os.path.exists(config.outputPath):
        config.errorMessage = "Output directory exists already -> please choose a new name"
        abort(422)
    os.mkdir(config.outputPath) #createOutputFolder
    #first save original referece image
    originalImage.save(os.path.join(config.outputPath,"reference-original-"+ originalImage.filename))
    #save face cropped image
    img = refFace.img.cpu().numpy()
    # convert image back to Height,Width,Channels
    img = np.transpose(img, (1, 2, 0))
    # show the image
    plt.imshow(img)
    plt.savefig(os.path.join(config.outputPath,"reference-cropped-face-"+ originalImage.filename))
    #create image matched folder
    MATCHED_FOLDER_PATH = os.path.join(config.outputPath,"image-matched-folder")
    os.mkdir(MATCHED_FOLDER_PATH)
    #create csv file
    header = ['fileName', 'similarityMeasure', 'parentFolderName','faceID']
    with open(os.path.join(config.outputPath,"matches-list.csv"), 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for match in matches:
            d, faceImg = match
            data = [faceImg.originalName, d, faceImg.folderName,faceImg.faceID]
            writer.writerow(data)
            #faceImg.img.save(os.path.)join(MATCHED_FOLDER_PATH,"m-"+ faceImg.originalName));
            # Created matched photo
            fig, ax = plt.subplots()
            ax.imshow(faceImg.img)
            ax.axis('off')
            box = faceImg.box
            sc = ax.add_patch(patches.Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1], edgecolor='red',facecolor='none', linewidth=2))
            fig.savefig(os.path.join(MATCHED_FOLDER_PATH,"m-"+"c-"+str(faceImg.faceID)+"-"+ faceImg.originalName), bbox_inches='tight')