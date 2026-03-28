# NSFW Image Detection & Embedding Project

## Project Description

This repository contains a **subset of the full AdventurePlus project** ([https://adventureplusapp.web.app/](https://adventureplusapp.web.app/)), focused on:

* **NSFW image detection** using **YOLO / NudeNet**
* **Image embedding generation** using **MobileNetV2**

> ⚠️ Note: This project **does not include the full AdventurePlus project**. Only NSFW detection and embeddings are included for **legal and licensing reasons**.
> I am **not the original creator of YOLO, Ultralytics, NudeNet, or MobileNetV2 models**.

The code in this repository, including Docker setup and wrappers around these models, is **distributed under AGPL-3.0**. This is because it incorporates or modifies components from the original AGPL-3.0 licensed projects. The code you see here is a **separate, independent work**.

This project leverages these technologies to **detect potentially harmful or unsafe images for end-users**. It is currently **not developed for commercial purposes**, and inclusion of these components **does not imply any future commercial release**.

---

## ⚠️ Warning / Content Notice

This project **processes images containing adult / 18+ content**. Some labels in the dataset correspond to explicit:


---

## Model Sources & Licenses

* **YOLO / Ultralytics** – original code and model are **not owned by this project** and are licensed under **AGPL-3.0**. Any modifications included here are also under **AGPL-3.0**.
* **NudeNet** – original code and model are **not owned by this project** and licensed under **AGPL-3.0**. Any modifications included here are also under **AGPL-3.0**.
* **MobileNetV2** – original model is **not owned by this project** and licensed under **Apache 2.0**.

### Links

* YOLO: [https://github.com/ultralytics/ultralytics/releases/tag/v8.0.208](https://github.com/ultralytics/ultralytics/releases/tag/v8.0.208)
* NudeNet: [https://github.com/notAI-tech/NudeNet/releases/download/v3.4-weights/320n.pt](https://github.com/notAI-tech/NudeNet/releases/download/v3.4-weights/320n.pt)

> ⚠️ Make sure to download models from official sources and respect their licenses.

---

## Requirements

* Docker ≥ 20.0
* Python 3.6 (inside the Docker image)

---

## Running with Docker

1. Build the Docker image:

```bash
cd aiModules
docker build -t nsfw-yolo .
```

2. Run the container (serves on port 5000):

```bash
docker run -p 5000:5000 --name nsfw-yolo-run nsfw-yolo
```

> The code, Dockerfile, and wrappers are **AGPL-3.0 licensed**. Users can execute the models, but the original model code is **not included** in this repository.

---

## License

This repository and all included modifications / wrappers are licensed under **AGPL-3.0**. Original models (YOLO, NudeNet, MobileNetV2) retain their own licenses as described above.
