# 🩺 Medbot: AI Medical Assistant
### Fine-tuned Medical AI Assistant
Challenge 9 - ZAKA AI Machine Learning Specialization

## Project Overview
This project was developed as part of the **ZAKA AI Certification (Challenge 9)**. It features a specialized Medical AI assistant (MedBot) fine-tuned on medical datasets using **LoRA (Low-Rank Adaptation)** and deployed as a containerized web application. It is designed to provide quick insights into medical symptoms through a user-friendly web interface.

To ensure high-performance inference despite the large memory footprint of LLMs, this application is deployed via a Flask-Ngrok Hybrid Architecture, bridging a high-RAM environment with a public web interface.

## 📸 Preview
<img width="729" height="302" alt="image" src="https://github.com/user-attachments/assets/6f15ea7d-1cb0-4f56-afc2-4645ab4a02bd" />


## Tech Stack
* **Model:** Fine-tuned Pythia-70m (using PEFT/LoRA)
* **Deployment:** Docker & Render
* **Tunneling:** Ngrok (Secure Public Tunnel)
* **Environment:** Google Colab (T4 GPU Accelerated)
* **Frontend:** HTML5, CSS3, JavaScript
* **Backend:** Flask (Python)

## Features
* **Domain Specificity:** Fine-tuned to provide informative responses to medical queries.
* **Scalability:** Containerized with Docker for consistent deployment across any cloud platform.
* **UI:**  Minimalist and User friendly chat interface for patient interaction.

## Engineering Design: The Deployment Strategy
During the Challenge, I explored multiple deployment pathways (Render, PythonAnywhere, and Docker). Due to the 1.2GB+ RAM requirement for loading torch and transformers alongside the model weights, standard free-tier hosting (512MB RAM) proved insufficient for production-level inference.

**My Solution:**
I implemented a High-Performance Tunneling Strategy. By hosting the Flask server in a high-resource environment (Google Colab) and exposing the port via Ngrok, the Medbot maintains access to GPU acceleration and 12GB+ of RAM, ensuring instantaneous responses for the end-user.

## ZAKA Challenge Context
This repository demonstrates proficiency in the full AI lifecycle:
1.  **Fine-tuning:** Implementing Parameter-Efficient Fine-Tuning (PEFT).
2.  **Infrastructure:** Writing a custom `Dockerfile` and `requirements.txt`.
3.  **Deployment:** Serving a large language model through a production-ready API.
   

## Model Weights
Due to GitHub file size limitations, the fine-tuned LoRA adapters (adapter_model.safetensors) are hosted on Google Drive.
https://drive.google.com/drive/folders/1t_mutiWiPxMlJv_bdVPv_3j5h_mBrZqE?usp=sharing 

## 🛠️ Setup & Docker Instructions
1. Clone the Repo: git clone https://github.com/BDES-25/MedBot-Challenge9.git 

**Option 1: Docker**
Use this method for containerized deployment:
1. Clone the Repo: git clone https://github.com/BDES/Medbot.git
2. Download Weights: Download adapter_model.safetensors from [ https://drive.google.com/file/d/1JmnypQ4jXJ2-FO0VOJpCURp6LTIl8fVF/view?usp=sharing ] and Place adapter_model.safetensors in the /outputs directory.
3. Build Image: docker build -t medbot .
4. Run Container: docker run -p 5000:5000 medbot

**Option 2: Manual Run with Ngrok (For Live Demo)**
Use this method to bypass RAM limitations on cloud hosts:
1. Install Dependencies: ```bash
pip install -r requirements.txt
2. Authentication: Sign in to Ngrok and set your authtoken:
Bash
ngrok config add-authtoken YOUR_AUTH_TOKEN_HERE
3. Run Application:
Bash
python app.py
4. Access: Open the public URL generated in your terminal or Colab cell.


## 💬 Usage
Type your symptoms into the chat box (e.g., "What should I do for a dry cough?") then model will generate a response based on its medical training data.

## ⚠️ Limitations
1. Hardware: Optimized for CPU; 
2. Accuracy: educational prototype and should not replace professional medical advice.
   

---
#AI #LLM #ZAKA #MedicalBot #Docker #Flask #Ngrok
