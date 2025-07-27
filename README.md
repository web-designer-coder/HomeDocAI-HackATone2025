# 🏥 HomeDoc AI – Voice-First Health Companion

**HomeDoc AI** is a multilingual, voice-first healthcare assistant designed to help users understand their symptoms, scan medical reports, and receive home remedies and guidance — especially for rural, elderly, and low-literacy users. Built for Hack-a-Tone 2025 (Problem Statement 2: *Unlocking Access*), it uses conversational AI to break down health barriers, one voice at a time.

🌐 **Live Site:** [https://homedoc-ai-webapp.vercel.app](https://homedoc-ai-webapp.vercel.app)

---

## 🎯 Hackathon Problem Statement

> “Unlocking Access – The Digital Companion for Social Welfare”  
HomeDoc AI solves Priya’s challenge: accessing health guidance without complex apps, in local languages, through natural, voice-first interaction.

---

## 🧩 Key Features

- 🗣️ **Voice-Based Chatbot** with multilingual STT & TTS (supports Indian languages like Hindi, Tamil, Marathi, Gujarati, etc.)
- 🤖 **AI Disease Predictor** based on selected symptoms (KNN ML model)
- 🧾 **Medical Report Analyzer**: OCR + Gemini summarization for blood/urine test PDFs
- 💬 **Friendly Health Advice & Home Remedies** in simple language
- 🔐 **Secure Login** via Firebase Authentication
- 📩 **Contact Form** via EmailJS
- 📱 **Mobile-Friendly UI**, dark mode, Three.js animations

---

## 🧑‍🤝‍🧑 Who is HomeDoc AI For?

| Group                         | How HomeDoc AI Helps                                                                                       |
|------------------------------|-------------------------------------------------------------------------------------------------------------|
| 🧓 **Elderly Users**          | No typing or app downloads — just speak and listen. Simple voice interaction makes it easy to access help. |
| 👩🏽‍🌾 **Rural Citizens**       | Speak in regional languages, get advice instantly — no travel, no paperwork, no confusing forms.          |
| 📖 **Low-Literacy Individuals** | No reading required. The assistant talks to you in your language, with simple words and instructions.       |
| 🌍 **Non-English Speakers**   | Chatbot supports major Indian languages via speech-to-text and text-to-speech.                             |
| 👨‍👩‍👧‍👦 **Families & Caregivers** | Can use chatbot to get help for family members, scan their reports, and explain results clearly.          |
| 🧑‍💼 **Social Workers/Volunteers** | Can use HomeDoc AI to guide beneficiaries in applying digital solutions for better healthcare access.     |

---

## 📋 Feature Checklist (Hack-a-Tone Judging Alignment)

| #    | Feature                                | Description                                                                                                                                                       | Judging Alignment                                                           |
| ---- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| ✅ 1  | **Talk-to-Chatbot in Your Language**   | Speak in your own language—like Tamil, Marathi, or Gujarati—and get a spoken reply in the same. | 🗣️ Voice Accessibility<br>🎤 Conversational Understanding<br>🎯 Innovation |
| ✅ 2  | **Know Your Illness from Symptoms**    | Select symptoms (e.g., cough, headache) and get illness predictions via KNN model.                                           | 💻 Core Functionality<br>🧠 Technical Implementation                        |
| ✅ 3  | **Scan Your Health Report & Get Help** | Upload PDFs/images; OCR + Gemini explain your report and offer care suggestions.                                             | 📄 Document Assistance<br>🎯 AI Integration                                 |
| ✅ 4  | **Simple & Clean Chat UI**             | Minimal UI with dark mode, large buttons, and easy flow for any age group.                                                   | 🎨 UI/UX & Accessibility                                                    |
| ✅ 5  | **Friendly Health Tips & Remedies**    | Chatbot shares simple home remedies and advice—like talking to a friend.                                                     | ❤️ Cultural Sensitivity<br>🗣️ Voice-First Design                           |
| ✅ 6  | **Safe Login & Privacy First**         | Firebase Authentication for secure login, session handling, and data protection.                                             | 🔐 Security<br>🌐 Scalability                                               |
| ✅ 7  | **Get in Touch Easily**                | Contact form in footer via EmailJS to reach the dev team anytime.                                                            | 💌 Completeness & Support                                                   |
| ✅ 8  | **Fun Animations & 3D Effects**        | Three.js adds subtle animations for visual engagement.                                                                      | 🎨 UI Polish<br>🎯 Innovation                                               |
| ✅ 9  | **Works Great on Phones Too**          | Mobile-optimized, responsive design—runs well on low-end Android phones.                                                     | 📱 Mobile Accessibility<br>🌐 Scalability                                   |
| ✅ 10 | **Smart AI Behind the Scenes**         | Gemini LLM powers both chatbot and report summaries—intelligent, multilingual responses.                                     | 🧠 AI Use<br>🗣️ Multilingual Interaction                                   |

---

## 🛠️ Tech Stack

### 🎨 Frontend
- React.js (with HTML, CSS)
- Firebase Authentication
- Three.js (for animations)
- EmailJS (contact form)

### ⚙️ Backend
- FastAPI (Python)
- ML: Scikit-learn (KNN, LabelEncoder)
- OCR: PyTesseract + Pillow + PyMuPDF
- Gemini API (chatbot + report summarization)

### 🚀 Deployment
- Frontend: [Vercel](https://vercel.com)
- Backend: [Render](https://render.com)

---

## 🧪 Dataset

- [Kaggle – Disease & Symptoms Dataset](https://www.kaggle.com/datasets/dhivyeshrk/diseases-and-symptoms-dataset)

---

## 👥 Team

| Member             | Role                                                                                     |
|--------------------|------------------------------------------------------------------------------------------|
| **Nidhi Devare**   | Frontend Dev (React, Three.js), chatbot UI, Firebase, multilingual voice support (Web Speech API), deployment |
| **Aryan Wankhade** | Backend Dev (FastAPI), OCR integration, ML model (KNN), Gemini integration, deployment    |

---

## 💡 Business Use-Cases

- 🏥 **Hospitals & Clinics** (AI triage assistant)
- 📱 **Health Apps** (B2C chatbot integrations)
- 🌐 **Rural Access** (multilingual, app-free access)
- 👩‍⚕️ **Telemedicine Partners** (report summarization, symptom screening)
- 💼 **SaaS Platform** (freemium model)

---

## 🔮 Future Scope

- 📲 Native mobile app version (React Native / Flutter)
- 📊 Report history dashboard
- 👨‍⚕️ Doctor escalation feature
- 🔍 Explainable ML (LIME/SHAP)

---

## 🧪 Run the Project Locally

### 🔹 Prerequisites

- Node.js (v16+)
- Python (v3.8+)
- `pip`, `git`

---

### 📁 Clone Repo

```bash
git clone https://github.com/yourusername/homedoc-ai-webapp.git
cd homedoc-ai-webapp
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
