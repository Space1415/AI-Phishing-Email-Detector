import re
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

def detect_phishing(email_text):
    phishing_patterns = [
        r"urgent", r"act now", r"limited time", r"verify your account",
        r"click here", r"reset your password", r"bank account", r"login details"
    ]

    suspicious_links = len(re.findall(r"https?://[^"]+", email_text)) > 0
    sender_mismatch = "@trustedbank.com" not in email_text

    flags = sum(bool(re.search(pattern, email_text, re.IGNORECASE)) for pattern in phishing_patterns)

    return (flags > 2 or suspicious_links or sender_mismatch), flags, suspicious_links, sender_mismatch

def train_model():
    emails = [
        "Verify your account by clicking this link now!",
        "Your trusted bank update: Your account is secure.",
        "Limited time offer: Reset your password to avoid suspension.",
        "Annual newsletter: Upcoming events and news."
    ]

    labels = [1, 0, 1, 0]

    pipeline = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    pipeline.fit(emails, labels)
    joblib.dump(pipeline, 'phishing_detector_model.pkl')

def predict_phishing(email_text):
    try:
        model = joblib.load('phishing_detector_model.pkl')
        prediction = model.predict([email_text])
        return bool(prediction[0])
    except Exception as e:
        print(f"Error loading or using the model: {e}")
        return False

if __name__ == "__main__":
    print("Phishing Email Detector\n")

    try:
        open('phishing_detector_model.pkl', 'rb')
    except FileNotFoundError:
        print("Training model...")
        train_model()

    email_input = "Subject: Urgent! Verify your account now by clicking this link: http://phishing-site.com"

    rule_based_detection, flags, suspicious_links, sender_mismatch = detect_phishing(email_input)
    print(f"Rule-based Detection: {rule_based_detection} (Flags: {flags}, Suspicious Links: {suspicious_links}, Sender Mismatch: {sender_mismatch})")

    model_detection = predict_phishing(email_input)
    print(f"Model-based Detection: {model_detection}")
