
import os
import torch
from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

app = Flask(__name__)

# CONFIGURATION
# "EleutherAI/gpt-neox-20b" >> the right one but session crashed after using all available RAM
BASE_MODEL_NAME = "EleutherAI/pythia-70m"
ADAPTER_PATH = "outputs"

# Device detection (CPU for Colab Free/Render Free)
device = "cuda" if torch.cuda.is_available() else "cpu"

# MODEL LOADING
print(f"Starting Medbot on {device.upper()}... please wait.")

try:
     # Get full absolute path to fix the 'Repo ID' error
    full_path = os.path.abspath(ADAPTER_PATH)
    print(f"Loading from: {full_path}")

    # Load Tokenizer locally
    tokenizer = AutoTokenizer.from_pretrained(full_path, local_files_only=True)

    # Load Base Model (float32 is safest for CPU)
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL_NAME, 
        torch_dtype=torch.float32,
        device_map=None
    )

    #Load LoRA Adapters from the local path
    model = PeftModel.from_pretrained(base_model, full_path)
    model.to(device)
    model.eval()

    print("Medbot loaded successfully!")

except Exception as e:
    print(f"Error loading model: {e}")


# ROUTES
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    user_message = data.get("message", "")

    # Prompt engineering for the Medical Assistant
    prompt = f"Patient: {user_message}\nMedbot:"

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        output_tokens = model.generate(**inputs, max_new_tokens=100,temperature=0.7,do_sample=True)

    response = tokenizer.decode(output_tokens[0], skip_special_tokens=True)
    # Extract only the Medbot's response
    clean_response = response.split("Medbot:")[-1].strip()

    return jsonify({"response": clean_response})

# RUN
if __name__ == '__main__':
    # PORT 5000 for Colab/LocalTunnel, dynamic port for Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
