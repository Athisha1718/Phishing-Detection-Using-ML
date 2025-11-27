import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

def train_model():
    # Load dataset
    df = pd.read_csv("dataset.csv")

    # Features and label
    X = df.drop(columns=["label"])
    y = df["label"]

    # Split data into train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create model
    model = LogisticRegression()

    # Train model
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Accuracy
    acc = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {acc * 100:.2f}%")

    # Save model
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model saved as model.pkl")

if __name__ == "__main__":
    train_model()
