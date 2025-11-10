<!DOCTYPE html>
<html lang="en">

<body>
 <center> <h1>👗 FashionFit-AI: Virtual Try-On System</h1></center>

  <!-- Demo Images -->


  <div class="section">
    <h2>🌟 Overview</h2>
    <p>FashionFit-AI is an <b>AI-powered Virtual Try-On system</b> allowing users to try clothes virtually without physically wearing them.</p>
    <ul>
      <li>Upload your own photos or use preloaded demo images.</li>
      <li>Choose between <b>VITON-HD</b> or <b>TryOn-Diffusion</b> (Hugging Face pretrained).</li>
      <li>Download the generated try-on image instantly.</li>
      <li>Local-first system: no cloud storage needed during development.</li>
      <li>Interactive Streamlit frontend with instant demo.</li>
    </ul>
  </div>

  <div class="section">
    <h2>🗂 Project Structure</h2>
    <pre>
fashionfit-ai/
│
├── app/
│   ├── main.py                  # FastAPI backend
│   ├── models/
│   │   ├── viton_hd/
│   │   │   ├── inference.py
│   │   │   └── checkpoints/viton_hd.pth
│   │   └── tryon_diffusion/
│   │       ├── inference.py
│   │       └── checkpoints/
│   └── utils.py
│
├── frontend/
│   ├── streamlit_app.py         # Streamlit frontend
│   └── static/images/           # Demo images
├── results/                     # Generated try-on results
├── requirements.txt
├── run_demo.py                  # End-to-end demo launcher
└── FashionFit-AI.html           # This file
    </pre>
  </div>

  <div class="section">
    <h2>⚡ Installation & Run</h2>
    <pre>
git clone https://github.com/hatami5/AI_Virtual_Tryon.git
cd fashionfit-ai

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
    </pre>
    <p>Place pretrained checkpoints:</p>
    <pre>
app/models/viton_hd/checkpoints/viton_hd.pth
app/models/tryon_diffusion/checkpoints/tryon_diffusion.ckpt
    </pre>
    <pre>Run demo:
python run_demo.py
    </pre>
  </div>

  <div class="section">
    <h2>🖥 Frontend Features</h2>
    <div class="gallery">
      <div>
        <img src="frontend/static/images/demo_user.jpg" width="200"/>
        <p>User Photo</p>
      </div>
      <div>
        <img src="frontend/static/images/demo_cloth.jpg" width="200"/>
        <p>Clothing Image</p>
      </div>
      <div>
        <img src="results/output.png" width="200"/>
        <p>Generated Try-On</p>
      </div>
    </div>
    <ul>
      <li>Dropdown to select preloaded images.</li>
      <li>Upload your own photos.</li>
      <li>Download generated try-on images.</li>
      <li>Model selection: VITON-HD or TryOn-Diffusion (Hugging Face pretrained).</li>
    </ul>
  </div>

  <div class="section">
    <h2>🔧 Hugging Face Integration</h2>
    <pre>
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe.to("cuda")  # GPU acceleration

prompt = "A person wearing a red t-shirt, photo-realistic"
image = pipe(prompt).images[0]
image.save("results/output.png")
    </pre>
    <p>No training required. Works with GPU or CPU. High-quality virtual try-on.</p>
  </div>

  <div class="section">
    <h2>📈 Workflow</h2>
    <pre>
User Upload / Select Image --> Streamlit Frontend --> FastAPI Backend
    --> Model Selection: VITON-HD or TryOn-Diffusion
    --> Run Inference --> Save Result --> Display + Download
    </pre>
  </div>

  <div class="section">
    <h2>🔗 References</h2>
    <ul>
      <li><a href="https://github.com/shadow2496/VITON-HD">VITON-HD GitHub</a></li>
      <li><a href="https://huggingface.co/docs/diffusers/index">Diffusers (Hugging Face)</a></li>
      <li><a href="https://huggingface.co/runwayml/stable-diffusion-v1-5">Stable Diffusion pretrained model</a></li>
    </ul>
  </div>

  <footer>
    <p align="center"><b>Created by Hassan Hatami — AI Developer & Engineer</b></p>
  </footer>

</body>
</html>
