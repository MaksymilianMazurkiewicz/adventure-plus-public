import numpy as np
import cv2
from .models_manager import models_manager
from .log import log

treshhold = 0.5

__labels = [
    2,# "BUTTOCKS_EXPOSED",
    3,# "FEMALE_BREAST_EXPOSED",
    4,# "FEMALE_GENITALIA_EXPOSED",
    5,# "MALE_BREAST_EXPOSED",
    6,# "ANUS_EXPOSED",
    7,# "FEET_EXPOSED",
    13,# "BELLY_EXPOSED",
    14,# "MALE_GENITALIA_EXPOSED"
]

def preprocess_image(image_bytes, target_size=320):
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_resized = cv2.resize(img, (target_size, target_size))
    log("END img preprocess")
    return img_resized

def predict(image_bytes):
    log("Sart NSFW image prediction")
    tensor = preprocess_image(image_bytes, 320)
    results = models_manager.nsfw_model(tensor, classes=__labels)
    for r in results:
        for box in r.boxes:
            conf = float(box.conf[0])
            if conf > treshhold:
                return True

    return False

    

