from fastapi import FastAPI
import pickle
import uvicorn
from feature import extract_features

app = FastAPI()

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "Phishing Detection API is running!"}

@app.get("/predict")
def predict(url: str):
    # Extract features from the URL
    features = extract_features(url)
    
    # Convert to 2D list for prediction
    prediction = model.predict([features])[0]

    if prediction == 1:
        result = "Phishing"
    else:
        result = "Legitimate"

    return {
        "url": url,
        "prediction": result
    }

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
