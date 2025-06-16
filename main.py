from fastapi import FastAPI, Request
from gtts import gTTS
from io import BytesIO
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.post("/tts")
async def tts_endpoint(request: Request):
    data = await request.json()
    text = data.get("text", "")
    lang = data.get("lang", "ar")
    tts = gTTS(text=text, lang=lang)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return StreamingResponse(mp3_fp, media_type="audio/mpeg")
