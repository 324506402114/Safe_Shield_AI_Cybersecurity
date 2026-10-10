# 🛡️ SafeShield AI

### AI-Powered Digital Safety & Phishing Risk Analyzer

> **HackNowa Global Hackathon 2026**
> **Problem Statement:** Digital Safety & Cybersecurity

SafeShield AI is a defensive cybersecurity application that uses **Artificial Intelligence, Natural Language Processing, URL analysis, and explainable risk scoring** to help users identify potentially suspicious messages and phishing-style links.

The system analyzes message content and URL characteristics without opening or interacting with submitted URLs. It combines multiple security signals into an easy-to-understand **0–100 risk score**, explains the detected indicators, and provides practical safety recommendations.

---

## 🎯 Problem Statement

Digital communication has made phishing, scam messages, fraudulent notifications, and malicious links increasingly difficult for ordinary users to identify.

Many suspicious messages use:

* Urgent language
* Fake account warnings
* Reward or prize claims
* Requests for passwords or OTPs
* Suspicious login pages
* URL shorteners
* IP-address-based links
* Misleading domains
* Unusual URL structures

Users need a simple way to understand **why a message may be risky**, rather than relying only on a binary "safe/unsafe" decision.

---

## 💡 Solution

SafeShield AI provides a lightweight, explainable cybersecurity analysis system.

The application:

1. Accepts a suspicious message from the user.
2. Extracts URLs from the message.
3. Uses an NLP machine-learning model to analyze message language.
4. Performs lexical and structural analysis of detected URLs.
5. Detects common social-engineering indicators.
6. Combines the signals into a 0–100 risk score.
7. Classifies the result as:

   * 🟢 LOW RISK
   * 🟠 SUSPICIOUS
   * 🔴 HIGH RISK
8. Explains the detected risk indicators.
9. Provides recommended safety actions.

---

# 🚀 Key Features

## 🤖 AI-Based Message Detection

SafeShield AI uses:

* TF-IDF
* Logistic Regression
* NLP text classification

to estimate whether a message contains suspicious language patterns.

---

## 🔗 Safe URL Analysis

URLs are analyzed without visiting them.

The analyzer checks characteristics such as:

* HTTPS vs HTTP
* IP-address domains
* URL length
* Number of subdomains
* Suspicious keywords
* URL shorteners
* Unusual ports
* Encoded characters
* Suspicious file extensions
* Hostname patterns
* Suspicious TLD heuristics

### Security design

SafeShield AI does **not** make network requests to submitted URLs.

This prevents the analysis process from intentionally visiting potentially dangerous destinations.

---

## 🧠 Explainable Risk Scoring

Instead of returning only a classification, SafeShield AI explains the detected indicators.

Example:

```text
Risk Score: 82/100
Risk Level: HIGH RISK

Indicators:
• Urgent language detected
• Sensitive information request detected
• URL uses HTTP
• URL uses an IP address
• Suspicious login keyword detected
```

This makes the system easier for non-technical users to understand.

---

## 🛡️ Safety Recommendations

The system provides actionable recommendations based on the detected indicators.

Examples:

* Avoid opening suspicious links.
* Verify the sender independently.
* Do not share passwords or OTPs.
* Do not provide banking information through unsolicited messages.
* Verify important requests through official channels.

---

## 📊 Risk Classification

| Risk Score | Classification | Meaning                                  |
| ---------: | -------------- | ---------------------------------------- |
|       0–29 | 🟢 LOW RISK    | No strong risk indicators detected       |
|      30–59 | 🟠 SUSPICIOUS  | Several indicators require caution       |
|     60–100 | 🔴 HIGH RISK   | Multiple strong risk indicators detected |

The score is an analytical risk indicator and should not be interpreted as definitive proof that a message is malicious.

---

# 🏗️ System Architecture

```text
                   ┌──────────────────────┐
                   │      User Input      │
                   │  Suspicious Message  │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │   Message Cleaning   │
                   │     & URL Extraction │
                   └──────────┬───────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
       ┌──────────────────┐      ┌──────────────────┐
       │   NLP Detector   │      │  URL Analyzer    │
       │                  │      │                  │
       │ TF-IDF           │      │ URL Structure    │
       │ Logistic Reg.    │      │ URL Indicators   │
       └────────┬─────────┘      └────────┬─────────┘
                │                         │
                └────────────┬────────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │    Risk Engine       │
                  │                      │
                  │ ML Probability       │
                  │ URL Risk              │
                  │ Security Heuristics  │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Explainable Result   │
                  │                      │
                  │ Risk Score 0–100     │
                  │ Risk Level           │
                  │ Indicators           │
                  │ Recommendations      │
                  └──────────────────────┘
```

---

# 🧠 AI & Technical Implementation

## 1. Text Classification

The message detector uses a scikit-learn pipeline:

```text
Raw Message
     ↓
TF-IDF Vectorization
     ↓
Logistic Regression
     ↓
Legitimate / Suspicious
```

### TF-IDF

TF-IDF converts text into numerical features based on word and n-gram importance.

The implementation supports:

* Unigrams
* Bigrams
* English stop-word filtering
* Sublinear TF scaling
* Feature limits

### Logistic Regression

Logistic Regression estimates the probability that a message belongs to the suspicious class.

The resulting probability becomes one of the inputs to the SafeShield risk engine.

---

# 🔍 URL Security Analysis

SafeShield performs **static lexical analysis** of URLs.

For example:

```text
http://192.168.1.50/login
```

may produce indicators such as:

```text
HTTP instead of HTTPS
IP-address hostname
Suspicious login keyword
```

The system does not attempt to connect to:

```text
192.168.1.50
```

or any other submitted destination.

---

# ⚙️ Risk Engine

The risk engine combines multiple independent signals.

Conceptually:

```text
                    NLP Risk
                       │
                       ▼
                  ┌─────────┐
                  │         │
URL Risk ────────►│  Risk   │◄──── Security Heuristics
                  │ Engine  │
                  │         │
                  └────┬────┘
                       │
                       ▼
                Final Risk Score
                    0 – 100
```

The current implementation considers:

* NLP suspicious probability
* URL risk
* Urgency indicators
* Sensitive-information requests
* Multiple URLs
* High-risk URL characteristics

The final score is then mapped to a human-readable risk category.

---

# 🗂️ Project Structure

```text
SafeShield-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│
├── models/
│   └── text_detector.joblib
│
├── src/
│   ├── text_detector.py
│   ├── url_analyzer.py
│   ├── risk_engine.py
│   └── utils.py
│
├── screenshots/
│
├── demo/
│
└── SafeShield_AI_Cybersecurity_Hackathon.ipynb
```

---

# 🛠️ Technology Stack

| Technology          | Purpose                        |
| ------------------- | ------------------------------ |
| Python              | Core programming language      |
| Streamlit           | Interactive web application    |
| Scikit-learn        | Machine learning               |
| TF-IDF              | Text feature extraction        |
| Logistic Regression | Message classification         |
| Pandas              | Data processing                |
| NumPy               | Numerical operations           |
| Joblib              | Model persistence              |
| Matplotlib          | Evaluation/visualization       |
| Regular Expressions | URL and text pattern detection |

---

# 📦 Installation

## 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd SafeShield-AI
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

Usually the local application is available at:

```text
http://localhost:8501
```

---

# 🧪 Running Individual Components

## Test the utility module

```bash
python -c "from src.utils import extract_urls; print(extract_urls('Visit https://example.com'))"
```

## Train and test the NLP detector

```bash
python src/text_detector.py
```

## Test URL analysis

```bash
python src/url_analyzer.py
```

## Test the complete risk engine

```bash
python src/risk_engine.py
```

---

# 🧪 Example Analysis

### Example input

```text
FINAL WARNING! Your account will be blocked today.
Verify your OTP and password immediately at
http://192.168.1.50/login
```

### Possible SafeShield analysis

```text
Risk Score: HIGH

Detected signals:

✓ Urgent language
✓ Sensitive-information request
✓ HTTP URL
✓ IP-address hostname
✓ Login-related URL keyword
✓ Suspicious message language

Recommended action:

Do not open the link or provide sensitive information.
Verify the request through an official channel.
```

---

# 📸 Screenshots

Add screenshots of your working application inside:

```text
screenshots/
```

Recommended screenshots:

### 1. Main Dashboard

```text
screenshots/dashboard.png
```

### 2. Low-Risk Analysis

```text
screenshots/low-risk.png
```

### 3. Suspicious Analysis

```text
screenshots/suspicious-risk.png
```

### 4. High-Risk Analysis

```text
screenshots/high-risk.png
```

### 5. Technical Analysis

```text
screenshots/technical-analysis.png
```

After uploading the images, you can display them here using:

```markdown
## 📸 Application Screenshots

### Dashboard

![SafeShield AI Dashboard](screenshots/dashboard.png)

### High-Risk Detection

![High Risk Detection](screenshots/high-risk.png)
```

---

# 🎥 Hackathon Demo

The recommended demo flow is:

### 1. Introduce the problem

Explain that phishing and scam messages often rely on urgency, impersonation, suspicious links, and requests for sensitive information.

### 2. Introduce SafeShield AI

Show the dashboard and explain that the system combines AI-based text analysis with URL and security heuristics.

### 3. Demonstrate a normal message

Example:

```text
Your package has been delivered successfully.
```

Show the resulting low-risk analysis.

### 4. Demonstrate suspicious language

Example:

```text
Congratulations! You won a reward.
Claim it immediately.
```

Show the suspicious indicators.

### 5. Demonstrate a high-risk message

Use a completely fictional example containing:

* Urgency
* Sensitive-information request
* Suspicious URL
* IP-address hostname

### 6. Explain the result

Show:

```text
Risk Score
     ↓
NLP Analysis
     ↓
URL Analysis
     ↓
Security Signals
     ↓
Recommendations
```

### 7. Explain the safety design

Emphasize:

> SafeShield analyzes URL strings without opening the URLs.

---

# 🔐 Responsible Cybersecurity Design

SafeShield AI is intentionally designed as a **defensive cybersecurity tool**.

It does not:

* Open suspicious URLs
* Execute downloaded files
* Exploit websites
* Attempt unauthorized access
* Collect passwords
* Collect OTPs
* Collect payment credentials
* Perform credential harvesting
* Scan external systems
* Attack infrastructure

The application is intended for **education, awareness, and defensive risk assessment**.

---

# ⚠️ Limitations

SafeShield AI is a risk-assessment prototype and has several limitations.

### 1. Synthetic training data

The initial NLP model uses a small synthetic dataset designed for demonstration and reproducibility.

A production system would require a much larger, diverse, and carefully validated dataset.

### 2. False positives

A legitimate message may contain words such as:

```text
verify
account
payment
security
urgent
```

and therefore receive elevated risk indicators.

### 3. False negatives

Sophisticated phishing messages may avoid obvious suspicious language and therefore evade simple lexical or ML detection.

### 4. URL heuristics

URL structure alone cannot prove that a website is malicious.

A legitimate site can have unusual URL characteristics, while a malicious site can appear technically normal.

### 5. No live threat intelligence

The current system does not query external threat-intelligence databases or reputation services.

---

# 🔮 Future Improvements

Potential future versions could include:

* Larger real-world cybersecurity datasets
* Transformer-based NLP models
* BERT-style message classification
* Domain reputation APIs
* Threat-intelligence integration
* WHOIS/domain-age analysis
* Homograph/IDN detection
* Brand impersonation detection
* QR-code URL analysis
* Email header analysis
* Browser extension integration
* Multilingual phishing detection
* Mobile application
* Continuous model evaluation
* Human-in-the-loop feedback
* Explainable AI dashboards
* Federated/privacy-preserving learning

---

# 🎯 Hackathon Alignment

SafeShield AI addresses the **Digital Safety & Cybersecurity** problem statement by combining:

### Innovation

A unified system combining message analysis, URL analysis, security heuristics, explainability, and user guidance.

### AI Implementation

TF-IDF and Logistic Regression provide machine-learning-based suspicious-message detection.

### Problem Relevance

The project targets phishing, scam messages, social engineering, and suspicious links.

### Functionality

Users can submit messages and immediately receive a structured risk assessment.

### Presentation

The Streamlit interface provides:

* Risk score
* Risk classification
* Security indicators
* URL analysis
* AI probabilities
* Safety recommendations

---

# 👨‍💻 Author

**Singipurapu Dinesh**

Computer Science Student | Python Developer | AI & Data Science Enthusiast

---

# 🏆 Hackathon

**HackNowa Global Hackathon 2026**

Problem Statement:

**Digital Safety & Cybersecurity**

Project:

**SafeShield AI**

---

# 📜 Disclaimer

SafeShield AI is an educational and defensive cybersecurity prototype.

A SafeShield result should not be treated as definitive proof that a message or URL is safe or malicious.

Users should independently verify important communications through trusted official channels.

Never provide passwords, OTPs, banking credentials, API keys, or other sensitive information to an unsolicited message or website.

---

## ⭐ Project Goal

> **Help users understand digital threats before they act on them.**

**Analyze. Understand. Verify. Stay Safe.** 🛡️
