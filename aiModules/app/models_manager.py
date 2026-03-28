import torch
import os
from .log import log
from torchvision import models
import gc
import torch.nn as nn
from ultralytics import YOLO

class ModelsManager:

    def __init__(self):
        self.is_cuda = torch.cuda.is_available() 
        self.deviceName = "cuda" if self.is_cuda else "cpu"
        log(f"Detect device: {self.deviceName}")
        self.nsfw_model = None
        self.embedding_model = None

    def load_models(self):
        base_path = os.path.join(os.path.dirname(__file__), "models")
        self.load_nsfw_model(base_path)
        self.load_embbeding_model(base_path)

    def load_nsfw_model(self, path):
        model_path = f"{path}/nsfw_model.pt"
        self.nsfw_model = YOLO(model_path).to(self.deviceName)
        log(f'NSFW model device {next(self.nsfw_model.parameters()).device}')

    def load_embbeding_model(self, path):
        model = models.mobilenet_v2(pretrained=False)
        state_dict = torch.load(f"{path}/mobile_v2.pth", map_location="cpu")
        model.load_state_dict(state_dict)
        model.to(self.deviceName).eval()
        embedding_model = nn.Sequential(*list(model.children())[:-1])
        embedding_model.to(self.deviceName)
        embedding_model.eval()

        del model, state_dict
        gc.collect()

        self.embedding_model = embedding_model
        log(f'Embbeding model device {next(self.embedding_model.parameters()).device}')


    def cleanup(self):
        if self.is_cuda:
           torch.cuda.empty_cache()
        log("Models cleanup done")

models_manager = ModelsManager()
