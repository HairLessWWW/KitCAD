from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class CADRequest(BaseModel):
    description: str

@app.post("/generate/")
def generate_model(req: CADRequest):
    with open("input.txt", "w", encoding="utf-8") as f:
        f.write(req.description)
    result = subprocess.run(
        ["FreeCADCmd", "cad/generate_model.py"],
        capture_output=True,
        text=True,
        shell=True
    )
    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "message": "Генерация завершена"
    }
