FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . .