from flask import Flask, json, jsonify, request, abort
from config import config
from main import frPipeline
from flask_cors import CORS
from services.createDetectFaceBoxes import findBoundingBoxes
import logging
api = Flask(__name__)
cors = CORS(api)

logging.basicConfig(level=logging.INFO, format = f'%(asctime)s %(levelname)s %(name)s : %(message)s')

@api.route('/face/detect', methods=['POST'])
def post_detectFaces():
    imageFile = request.files['image']
    boxes = findBoundingBoxes(imageFile)
    if boxes is None:
        abort(422, "No Faces detected in this image, try another one")
        return jsonify([])
    boxesList = boxes.tolist() #prepare for json method
    return json.dumps(boxesList)

@api.route('/face/select', methods=['POST'])
def post_selectFace():
    config.faceId = int(request.args.get('id'))
    return jsonify(config.faceId)

@api.route('/search/start', methods=['GET'])
def get_startSearch():
    frPipeline(config.faces,config.faceId)
    api.logger.info(f'FaceRecognitionPipeline Started')
    return "success"

@api.route('/gallery/path', methods=['POST'])
def post_setGallery():
    config.galleryPath = request.data.decode().replace('"','')
    api.logger.info(f'GalleryPath Set : {config.galleryPath}')
    return config.galleryPath

@api.route('/start', methods=['POST'])
def post_startPipeline():
    api.logger.info(f'Pipeline started')
    frPipeline()
    return 'Pipeline started'

if __name__ == '__main__':
    api.run()
