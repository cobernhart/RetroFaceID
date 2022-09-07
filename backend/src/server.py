from flask import Flask, json, jsonify, request, abort
from config import config
from searchProgress import progress, resetprogress
from main import frPipeline
from flask_cors import CORS
from services.createDetectFaceBoxes import findBoundingBoxes
import logging
import os
import time
api = Flask(__name__)
cors = CORS(api)

logging.basicConfig(level=logging.INFO, format = f'%(asctime)s %(levelname)s %(name)s : %(message)s')

@api.route('/face/detect', methods=['POST'])
def post_detectFaces():
    imageFile = request.files['image']
    boxes = findBoundingBoxes(imageFile)
    if boxes is None:
        response.status = 422
        response = jsonify({
            'message': 'No Faces detected in this image, try another one',
            'boxes': boxes
        })
        return response
    #prepare for json method
    response = jsonify({
        'message': f'{str(len(boxes)) + " faces detected"}',
        'boxes': json.dumps(boxes.tolist())
    })
    return response

@api.route('/face/select', methods=['POST'])
def post_selectFace():
    config.faceId = int(request.args.get('id'))
    api.logger.info(f'Face #{config.faceId}')
    response = jsonify({
        'message': f'Face #{config.faceId} selected',
        'id': f'{config.faceId}'
    })
    return response

@api.route('/search/start', methods=['GET'])
def get_startSearch():
    if config.faceId is None or config.galleryPath is None or config.outputPath is None:
        api.logger.info(f'Search not started configs missing')
        message = "Please provide following configurations "
        stringList = []
        if config.faceId is None:
            stringList.append("a valid face")
        if config.galleryPath is None:
            stringList.append(" a gallery path")
        if config.outputPath is None:
            stringList.append(" a output path")
        if os.path.exists(config.outputPath):
            response = jsonify({
                'message': f'Search not started because output directory exists already. Please choose a new name'
            })
            response.status = 422
            return response
        message += ','.join(stringList)
        response = jsonify({
            'message': message
        })
        response.status = 422
        return response
    resetprogress()
    config.runSearch = True
    start = time.time()
    frPipeline(config.faces,config.faceId)
    end = time.time()
    api.logger.info(f'Search finished in {int((end - start) / 60)} min')
    api.logger.info(f'FaceRecognitionPipeline Started')
    response = jsonify({
        'message': f'Search finished in {int((end - start) / 60)} min'
    })
    return response

@api.route('/search/stop', methods=['GET'])
def get_stopSearch():
    config.runSearch = False
    response = jsonify({
        'message': 'Search is stopping and output generated'
    })
    return response

@api.route('/search/progress', methods=['GET'])
def post_getProgress():
    api.logger.info(f'Searchprogress')
    response = jsonify({
        'message': f'Searchprogress queried',
        'imageCount': progress.imageCount,
        'faceCount' : progress.faceCount,
        'matchCount' : progress.matchCount
    })
    return response

@api.route('/gallery/path', methods=['POST'])
def post_setGallery():
    config.galleryPath = request.data.decode().replace('"', '')
    api.logger.info(f'GalleryPath Set : {config.galleryPath}')
    response = jsonify({
        'message': f'GalleryPath set to {config.galleryPath}'
    })
    return response

@api.route('/output/path', methods=['POST'])
def post_setOutput():
    config.outputPath = request.data.decode().replace('"', '')
    if os.path.exists(config.outputPath):
        response = jsonify({
            'message': f'Output directory exists already. Please choose a new name'
            })
        response.status = 422
        return response

    api.logger.info(f'OutputPath Set : {config.outputPath}')
    response = jsonify({
        'message': f'OutputPath set to {config.outputPath}'
    })
    return response

@api.route('/settings', methods=['POST'])
def post_setSettings():
    data = request.get_json()
    config.method = data['method']
    config.threshold = data['threshold']
    response = {
        'message': f'Updated settings method {config.method} with threshold {config.threshold} is used'
    }
    return response

if __name__ == '__main__':
    api.run()
