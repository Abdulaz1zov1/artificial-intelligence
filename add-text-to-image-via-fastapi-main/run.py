from fastapi import FastAPI, UploadFile
from PIL import ImageDraw, Image
from fastapi.responses import FileResponse


app = FastAPI()


def add_text(image_path, title):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), title, (255,255,255))
    output_name = f'{image_path.split(".")[0]}-out.jpg'
    img.save(output_name)
    return output_name


@app.post("/add-text/")
def read_item(file: UploadFile, title: str):

    with open(f"{file.filename}", "wb") as f:
        f.write(file.file.read())

    name = add_text(file.filename, title)

    return FileResponse(name)
