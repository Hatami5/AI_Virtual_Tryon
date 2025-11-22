from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from pathlib import Path
import uuid
from app.models.viton_hd.inference import run_tryon as run_viton_tryon
from app.models.tryon_diffusion.inference import load_model, run_tryon as run_diffusion_tryon
from app.utils import save_upload_file

app = FastAPI()

# Allow CORS
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

# -------------------------------
# Preload HF model at startup
# -------------------------------
@app.on_event("startup")
def startup_event():
    print("Loading Hugging Face TryOn-Diffusion model...")
    load_model(device="cuda" if torch.cuda.is_available() else "cpu")
    print("Model loaded successfully ")

# -------------------------------
# Try-On endpoint
# -------------------------------
@app.post("/tryon")
async def tryon(person: UploadFile = File(...),
                cloth: UploadFile = File(...),
                model: str = Form("viton_hd")):
    try:
        person_path = save_upload_file(person)
        cloth_path = save_upload_file(cloth)

        output_filename = f"{uuid.uuid4().hex}.png"
        output_path = RESULTS_DIR / output_filename

        if model.lower() == "viton_hd":
            run_viton_tryon(person_path, cloth_path, output_path)
        elif model.lower() == "tryon_diffusion":
            run_diffusion_tryon(person_path, cloth_path, output_path)
        else:
            return JSONResponse({"error": "Invalid model selected"}, status_code=400)

        return {"result_filename": output_filename}

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

@app.get("/result/{filename}")
async def get_result(filename: str):
    file_path = RESULTS_DIR / filename
    if file_path.exists():
        return FileResponse(file_path)
    return JSONResponse({"error": "File not found"}, status_code=404)
