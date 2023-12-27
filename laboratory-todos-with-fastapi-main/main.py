from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse, FileResponse
from typing import Annotated


app = FastAPI()
app.mount("/images", StaticFiles(directory="images"), name="images")
CUSTOM_FILE = "images/stefan-rodriguez-2AovfzYV3rc-unsplash.jpeg"

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/items")
def read_item(item_id: int, items_id: str):
    return {"item_id": f"{item_id, items_id}"}


@app.post("/files/")
async def create_file(file: Annotated[UploadFile, File()]):
    print(dir(file))
    
    file_name = "images/"+file.filename
                 
    with open(file_name, "wb") as f:
        data = await file.read()
        f.write(data)

    return {"filename": file_name}


@app.post("/get-file-as-streaming-response")
def read_item():
    def iterfile():
        with open(CUSTOM_FILE, mode="rb") as f:
            yield from f

    return StreamingResponse(iterfile(), media_type="image/jpeg")


@app.post("/get-file-as-file-response")
def read_item():
    return FileResponse(CUSTOM_FILE, media_type="image/jpeg")