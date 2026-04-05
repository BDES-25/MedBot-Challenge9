# 🩺 Medbot: AI Medical Assistant
### Fine-tuned Medical AI Assistant
Challenge 9 - ZAKA AI Machine Learning Specialization

## Project Overview
This project was developed as part of the **ZAKA AI Certification (Challenge 9)**. It features a specialized Medical AI assistant (MedBot) fine-tuned on medical datasets using **LoRA (Low-Rank Adaptation)** and deployed as a containerized web application. It is designed to provide quick insights into medical symptoms through a user-friendly web interface.

## 📸 Preview


## Tech Stack
* **Model:** Fine-tuned GPT-NeoX (using PEFT/LoRA)
* **Backend:** Flask (Python)
* **Deployment:** Docker & Render
* **Frontend:** HTML5, CSS3, JavaScript

## Features
* **Domain Specificity:** Fine-tuned to provide informative responses to medical queries.
* **Scalability:** Containerized with Docker for consistent deployment across any cloud platform.
* **User Interface:** A minimalist and responsive chat interface for patient interaction.

## ZAKA Challenge Context
This repository demonstrates proficiency in the full AI lifecycle:
1.  **Fine-tuning:** Implementing Parameter-Efficient Fine-Tuning (PEFT).
2.  **Infrastructure:** Writing a custom `Dockerfile` and `requirements.txt`.
3.  **Deployment:** Serving a large language model through a production-ready API.

## Model Weights
Due to GitHub file size limitations, the fine-tuned LoRA adapters (adapter_model.safetensors) are hosted on Google Drive.
https://drive.google.com/drive/folders/1t_mutiWiPxMlJv_bdVPv_3j5h_mBrZqE?usp=sharing 

## 🛠️ Setup & Docker Instructions
1. Clone the Repo: git clone https://github.com/YourUser/Medbot.git
2. Download Weights: Download adapter_model.safetensors from [ https://drive.google.com/file/d/1JmnypQ4jXJ2-FO0VOJpCURp6LTIl8fVF/view?usp=drive_link  ] and place it in /outputs.
3. Build Docker Image:  docker build -t medbot 
4. Run Container:  docker run -p 5000:5000 medbot

## 💬 Usage
Type your symptoms into the chat box (e.g., "What should I do for a dry cough?") then model will generate a response based on its medical training data.

## ⚠️ Limitations
1. Hardware: Optimized for CPU; 
2. Accuracy: educational prototype and should not replace professional medical advice.
   

---
#AI #LLM #ZAKA #MedicalBot #Docker #Flask
