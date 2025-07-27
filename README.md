# 🏥 HomeDoc AI – Voice-First Health Companion

**HomeDoc AI** is a multilingual, voice-first healthcare assistant designed to help users understand their symptoms, scan medical reports, and receive home remedies and guidance — especially for rural, elderly, and low-literacy users. Built for Hack-a-Tone 2025 (Problem Statement 2: *Unlocking Access*), it uses conversational AI to break down health barriers, one voice at a time.

🌐 **Live Site:** [https://homedoc-ai-webapp.vercel.app](https://homedoc-ai-webapp.vercel.app)

---

## 🎯 Hackathon Problem Statement

> “Unlocking Access – The Digital Companion for Social Welfare”
> HomeDoc AI solves Priya’s challenge: accessing health guidance without complex apps, in local languages, through natural, voice-first interaction.

---

## 🧩 Key Features

* 🗣️ **Voice-Based Chatbot** with multilingual STT & TTS (supports Indian languages like Hindi, Tamil, Marathi, Gujarati, etc.)
* 🤖 **AI Disease Predictor** based on selected symptoms (KNN ML model)
* 🧾 **Medical Report Analyzer**: OCR + Gemini summarization for blood/urine test PDFs
* 💬 **Friendly Health Advice & Home Remedies** in simple language
* 🔐 **Secure Login** via Firebase Authentication
* 📩 **Contact Form** via EmailJS
* 📱 **Mobile-Friendly UI**, dark mode, Three.js animations

---

## 🧑‍🤝‍🧑 Who is HomeDoc AI For?

| Group                                 | How HomeDoc AI Helps                                                                                       |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 🧓 **Elderly Users**                  | No typing or app downloads — just speak and listen. Simple voice interaction makes it easy to access help. |
| 👩🏽‍🌾 **Rural Citizens**            | Speak in regional languages, get advice instantly — no travel, no paperwork, no confusing forms.           |
| 📖 **Low-Literacy Individuals**       | No reading required. The assistant talks to you in your language, with simple words and instructions.      |
| 🌍 **Non-English Speakers**           | Chatbot supports major Indian languages via speech-to-text and text-to-speech.                             |
| 👨‍👩‍👧‍👦 **Families & Caregivers** | Can use chatbot to get help for family members, scan their reports, and explain results clearly.           |
| 🧑‍💼 **Social Workers/Volunteers**   | Can use HomeDoc AI to guide beneficiaries in applying digital solutions for better healthcare access.      |

---

## 📋 Feature Checklist (Hack-a-Tone Judging Alignment)

| #    | Feature                                    | Description                                                                                                                                      | Judging Alignment                                                          |
| ---- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| ✅ 1  | **Voice-First Chatbot (Multilingual)**     | Users speak in their local language (Tamil, Hindi, Marathi, Gujarati, etc.) via mic. Chatbot uses STT and responds via TTS in the same language. | Conversational Understanding<br>Voice Accessibility<br>Innovation & AI Use |
| ✅ 2  | **Symptom-Based Disease Predictor**        | Users select symptoms and get illness predictions using a trained KNN ML model. Aimed at non-technical and low-literacy users.                   | Core Functionality<br>Technical Implementation                             |
| ✅ 3  | **Medical Report Scanner (OCR + Gemini)**  | Upload reports (PDF/image). OCR extracts text and Gemini LLM simplifies and explains the content, with care tips.                                | Document Assistance<br>Innovation & AI Use                                 |
| ✅ 4  | **User-Friendly Chat UI**                  | Clean, simple UI with dark mode, large clickable elements, and minimal menus. Easy for elderly or first-time users.                              | UI/UX & Accessibility                                                      |
| ✅ 5  | **Personalized Voice-Based Health Advice** | Chatbot gives home remedies and recovery tips in a conversational format—easy to understand, no jargon.                                          | Cultural Sensitivity<br>Voice-First Accessibility                          |
| ✅ 6  | **Secure Login & Session Handling**        | Firebase used for sign in/up, profile creation, and secure session tracking.                                                                     | Scalability & Security                                                     |
| ✅ 7  | **Contact Developer Option (EmailJS)**     | Contact form in the footer lets users reach out to the developer team easily.                                                                    | Completeness & Polish                                                      |
| ✅ 8  | **Interactive Visuals (Three.js)**         | Smooth animations and 3D visuals improve engagement, especially for youth or new users.                                                          | UI Polish<br>Innovation                                                    |
| ✅ 9  | **Mobile-First, App-Free Design**          | Entire platform is responsive, works well on low-end phones and browsers—no app downloads needed.                                                | Accessibility<br>Scalability                                               |
| ✅ 10 | **Gemini LLM Integration**                 | Gemini is used for multilingual chatbot replies and for analyzing reports, offering rich contextual understanding.                               | AI Use<br>🇮🇳 Multilingual Interaction                                    |

---

## 🛠️ Tech Stack

### 🎨 Frontend

* React.js (with HTML, CSS)
* Firebase Authentication
* Three.js (for animations)
* EmailJS (contact form)

### ⚙️ Backend

* FastAPI (Python)
* ML: Scikit-learn (KNN, LabelEncoder)
* OCR: PyTesseract + Pillow + PyMuPDF
* Gemini API (chatbot + report summarization)

### 🚀 Deployment

* Frontend: [Vercel](https://vercel.com)
* Backend: [Render](https://render.com)

---

## 🧪 Dataset

* [Kaggle – Disease & Symptoms Dataset](https://www.kaggle.com/datasets/dhivyeshrk/diseases-and-symptoms-dataset)

---

## 👥 Team

| Member             | Role                                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------------------- |
| **Nidhi Devare**   | Frontend Dev (React, Three.js), chatbot UI, Firebase, multilingual voice support (Web Speech API), deployment |
| **Aryan Wankhade** | Backend Dev (FastAPI), OCR integration, ML model (KNN), Gemini integration, deployment                        |

---

## 💡 Business Use-Cases

* 🏥 **Hospitals & Clinics** (AI triage assistant)
* 📱 **Health Apps** (B2C chatbot integrations)
* 🌐 **Rural Access** (multilingual, app-free access)
* 👩‍⚕️ **Telemedicine Partners** (report summarization, symptom screening)
* 💼 **SaaS Platform** (freemium model)

---

## 🔮 Future Scope

* 📲 Native mobile app version (React Native / Flutter)
* 📊 Report history dashboard
* 👨‍⚕️ Doctor escalation feature
* 🔍 Explainable ML (LIME/SHAP)

---

## 🧪 Run the Project Locally

### 🔹 Prerequisites

* Node.js (v16+)
* Python (v3.8+)
* `pip`, `git`

---

### 📁 Clone Repo

```bash
git clone https://github.com/yourusername/homedoc-ai-webapp.git
cd homedoc-ai-webapp
```

---

### 🎨 Frontend Setup

```bash
cd Frontend
npm install
npm start
```

---

### ⚙️ Backend Setup

```bash
cd Backend
pip install -r requirements.txt
uvicorn main:app --reload
```

---

### 🔐 Create `.env` File

Create a `.env` file inside the `Backend/` folder and add the following:

```env
GEMINI_API_KEY=your_gemini_api_key
FIREBASE_API_KEY=your_firebase_web_api_key
```

---

> 🗣️ *HomeDoc AI is built to talk like a human, guide like a doctor, and care like a friend — all in your language.*
