from fastapi import FastAPI, UploadFile, File
from faster_whisper import WhisperModel
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend (change to your frontend port if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model once
model = WhisperModel("base")

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        segments, info = model.transcribe(file_path)
        text = " ".join(segment.text for segment in segments)
        return {"transcription": text}
    except Exception as e:
        return {"error": str(e)}
    finally:
        os.remove(file_path)


