FROM python:3.6-slim

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    tk-dev \
    tcl-dev \
    libtk8.6 \
    libtcl8.6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /aiModules

RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Based on modfied ultralitycs lib for python3.6
COPY ultralytics-8.0.208.tar.gz .
RUN pip install --no-deps ultralytics-8.0.208.tar.gz

COPY run.py .
COPY app ./app
CMD [ "python", "run.py" ]
