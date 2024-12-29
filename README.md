# AI-Phishing-Email-Detector




AI-Powered Phishing Email Detector
An advanced Python-based tool for detecting phishing emails using both rule-based and machine learning approaches.

Features
Rule-Based Detection:

Detects phishing characteristics such as:
Suspicious links.
Urgent language patterns.
Mismatched sender information.
Machine Learning Detection:

Employs a Random Forest Classifier trained on email text data to flag phishing attempts.
Easily extendable with additional datasets for improved accuracy.
Dual Detection System:

Combines rule-based and AI-driven methods for comprehensive email analysis.
Requirements
Python 3.7+
Required libraries (install using pip):
scikit-learn
joblib
Setup Instructions
Clone the Repository:

bash
git clone https://github.com/yourusername/ai-phishing-email-detector.git
cd ai-phishing-email-detector
Install Dependencies:

bash
pip install -r requirements.txt
Run the Script:

bash
python ai_phishing_email_detector.py
How It Works
Rule-Based Analysis:

Scans the email text for specific patterns such as suspicious links and keywords.
Flags phishing emails based on the presence of multiple warning signals.
Machine Learning Detection:

Trained on a small sample dataset.
Predicts phishing likelihood using a Random Forest Classifier.
Result:

Outputs a combined evaluation of rule-based and ML-driven phishing detection.
Example Usage
python
email_input = "Subject: Urgent! Verify your account now by clicking this link: http://phishing-site.com"

# Rule-Based Detection
rule_based_detection, flags, suspicious_links, sender_mismatch = detect_phishing(email_input)
print(f"Rule-based Detection: {rule_based_detection}")

# Model-Based Detection
model_detection = predict_phishing(email_input)
print(f"Model-based Detection: {model_detection}")
Folder Structure
plaintext
Kopier kode
ai-phishing-email-detector/
├── ai_phishing_email_detector.py   # Main Script
├── phishing_detector_model.pkl     # Model File (Generated Post-Training)
├── requirements.txt                # Python Dependencies
To-Do
Extend the dataset for better ML model training.
Add support for parsing raw email headers.
Implement GUI for easier usage.
License
This project is licensed under the MIT License.

