# import cv2
# import numpy as np
# from .log import log

# cv2_cuda_use = cv2.cuda.getCudaEnabledDeviceCount() > 0
# log(f"cv2 cuda status {cv2_cuda_use}")

# def upload_img(image_bytes):
#     nparr = np.frombuffer(image_bytes, np.uint8)
#     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

#     gpu_img = cv2.cuda_GpuMat()
#     gpu_img.upload(img)
#     return gpu_img

