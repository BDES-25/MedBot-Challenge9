
import os
import torch
from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

app = Flask(__name__)

# CONFIGURATION
# Using Pythia-70m for high stability on Render/Colab Free Tier
BASE_MODEL_NAME = "EleutherAI/pythia-70m"
ADAPTER_PATH = "outputs"  # Your Challenge 8 training output folder

# Device detection
device = "cuda" if torch.cuda.is_available() else "cpu"

# MODEL LOADING
print(f" Starting Medbot on {device.upper()}... please wait.")

try:
    full_path = os.path.abspath(ADAPTER_PATH)
    
    # 1. Load Tokenizer (Matches your training tokenizer.json)
    tokenizer = AutoTokenizer.from_pretrained(full_path)
    
    # 2. Load Base Model (Using float32 for maximum CPU compatibility on Render)
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL_NAME, 
        torch_dtype=torch.float32,
        device_map=None
    )

    # 3. Merge LoRA Adapters
    # We use is_local_path=True to ensure it looks at your folder
    model = PeftModel.from_pretrained(base_model, full_path)
    model.to(device)
    model.eval()

    print(" Medbot loaded successfully!")

except Exception as e:
    print(f" Error loading model: {e}")

# ROUTES
@app.route('/')
def index():
    # Ensure you have a 'templates/index.html' file!
    try:
        return render_template('index.html')
    except:
        return "<h1>Medbot is Online</h1><p>Please use the /predict API endpoint.</p>"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    user_message = data.get("message", "")

    # Matches the training format: Patient -> Doctor
    prompt = f"Patient: {user_message}\nDoctor:"

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        output_tokens = model.generate(
            **inputs, 
            max_new_tokens=100,
            temperature=0.7,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

    response = tokenizer.decode(output_tokens[0], skip_special_tokens=True)
    
    # Extract only the Doctor's response
    clean_response = response.split("Doctor:")[-1].strip()

    return jsonify({"response": clean_response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
