from flask import Blueprint, request, jsonify
from .log import log
from .nsfw_detector import predict
from .image_embbeding import image_embedding
import cv2

main = Blueprint("main", __name__)

def get_image(request):
    if "image" not in request.files:
        raise Exception("No file found in request")
    file = request.files["image"]
    return file.read()

@main.route("/nsfw", methods=["POST"])
def check_nsfw():
    log("Event: NSFW start")
    
    try:
        image_bytes = get_image(request)
        result = predict(image_bytes)
    except Exception as e:
        log(f", {str(e)}")
        return jsonify({"error": str(e)}), 500
    
    log("Event: NSFW end")
    return jsonify(result)

@main.route("/embbed", methods=["POST"])
def embbed():
    log("Event: embed start")

    try:
        image_bytes = get_image(request)
        result = image_embedding(image_bytes)
    except Exception as e:
        log(f", {str(e)}")
        return jsonify({"error": str(e)}), 500

    log("Event: embed end")
    return jsonify({"res": result})
