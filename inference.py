import torch
from diffusers import StableDiffusionInpaintPipeline
from PIL import Image
import os

# Load pre-trained model from Hugging Face
# You can replace this with your own fine-tuned model later
MODEL_ID = "runwayml/stable-diffusion-inpainting"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Loading model on {DEVICE}...")

# Load model
pipe = StableDiffusionInpaintPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32
).to(DEVICE)

def generate_tryon_result(person_path: str, cloth_path: str, result_path: str):
    """
    Use a diffusion model to generate a try-on result
    """

    # Open input images
    person_img = Image.open(person_path).convert("RGB").resize((512, 512))
    cloth_img = Image.open(cloth_path).convert("RGB").resize((512, 512))

    # Create a composite prompt — later you can make this dynamic
    prompt = "A person wearing the uploaded clothing item, realistic lighting and proportions"

    # Generate result using the diffusion model
    result = pipe(
        prompt=prompt,
        image=person_img,
        mask_image=cloth_img,
        guidance_scale=7.5,
        num_inference_steps=30
    ).images[0]

    # Save and return
    os.makedirs(os.path.dirname(result_path), exist_ok=True)
    result.save(result_path)

    return result_path
