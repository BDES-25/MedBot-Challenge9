# Use a lightweight Python base image
FROM python:3.12-slim

#Set the working directory inside the container
WORKDIR /app

#Copy all files from your computer/Colab into the container
COPY . .

#Install libraries from your requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the app when the container opens
CMD ["python", "app.py"]
