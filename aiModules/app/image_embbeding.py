import cv2
import numpy as np
import torch
from .models_manager import models_manager
from .log import log

def preprocess_image_byte(file_bytes):
    nparr = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    h, w, _ = img.shape
    scale = 256 / min(h, w)
    new_h, new_w = int(h * scale), int(w * scale)
    img_resized = cv2.resize(img, (new_w, new_h))

    startx = max(new_w // 2 - 112, 0)
    starty = max(new_h // 2 - 112, 0)
    img_cropped = img_resized[starty:starty+224, startx:startx+224]

    img_norm = img_cropped / 255.0
    mean = np.array([0.485, 0.456, 0.406]).reshape(1,1,3)
    std = np.array([0.229, 0.224, 0.225]).reshape(1,1,3)
    img_norm = (img_norm - mean) / std

    img_chw = np.transpose(img_norm, (2,0,1)).astype(np.float32)
    img_batch = np.expand_dims(img_chw, axis=0)

    tensor = torch.from_numpy(img_batch).to(models_manager.deviceName)
    return tensor

def image_embedding(file_bytes):
    log("Start EMBEDDING image prediction")
    tensor = preprocess_image_byte(file_bytes)
    
    with torch.no_grad():
        features = models_manager.embedding_model(tensor)
        embedding = torch.mean(features, dim=[2,3])  # shape [1, 1280]

    embedding_np = embedding.cpu().numpy()
    return embedding_np.tolist()[0]
