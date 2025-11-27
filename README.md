# Phishing-Detection-Using-ML
A machine-learning based phishing detection system that analyzes website URLs and predicts whether they are legitimate or malicious. The project extracts key URL features (like length, special characters, presence of IP address, depth, etc.) and uses a trained Random Forest model to classify phishing attempts in real-time. It also includes a FastAPI-powered REST endpoint to allow easy integration with other applications or security tools.


**Setup & Usage**

Clone the repository:git clone https://github.com/Athisha1718/Phishing-Detection-Using-ML.git
cd Phishing-Detection-Using-ML
Install dependencies:pip install -r requirements.txt and Train the model (optional if model.pkl already exists):python train.py and Run the API server:uvicorn api:app --reload
