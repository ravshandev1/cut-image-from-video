from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import cv2
import os

app = FastAPI()


class Video(BaseModel):
    video: str


@app.post('/cut-image')
async def index(data: Video):
    video = data.video.split('/')[-1]
    name = video.split('.')[0]
    cap = cv2.VideoCapture(f'{data.video}')
    ret, frame = cap.read()
    if frame is not None:
        cv2.imwrite(f'images/{name}.jpg', frame)    
    cap.release()
    return FileResponse(f'images/{name}.jpg')

@app.get("/remove/{image}")
async def remove_image(image: str):
    os.remove(f"images/{image}")
    return {'success': True}
