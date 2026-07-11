# 🎥 QuackVision AI

<div align="center">

# 🚀 QuackVision AI

### Multimodal AI Video Understanding & Intelligent Caption Generation

Built for **AMD Developer Hackathon – ACT II**

**Team:** QUACKSHIELD X

<img src="https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react" />
<img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi" />
<img src="https://img.shields.io/badge/Gemma%204-AI-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Whisper-Speech-success?style=for-the-badge" />
<img src="https://img.shields.io/badge/EasyOCR-OCR-orange?style=for-the-badge" />

</div>

---

# 📌 Overview

QuackVision AI is a multimodal AI platform that understands videos by combining **speech recognition**, **computer vision**, and **OCR** into one intelligent reasoning pipeline.

Unlike traditional caption generators that rely on a single modality, QuackVision AI fuses multiple AI models to understand the complete story before generating high-quality captions suitable for LinkedIn, Instagram, YouTube Shorts, and other social platforms.

---

# 🚨 Problem Statement

Content creators spend significant time creating captions that accurately represent the story of a video.

Most existing AI tools:

- rely only on speech
- ignore visual context
- miss on-screen text
- generate generic captions
- fail to understand the complete story

---

# 💡 Our Solution

QuackVision AI analyzes a video using three AI pipelines simultaneously:

🎙 Speech Recognition

📸 Visual Understanding

📝 OCR

The extracted information is fused using **Gemma 4** to generate intelligent captions with richer context and improved quality.

---

# ✨ Features

## 🎥 Video Understanding

- Video Upload
- Intelligent Frame Extraction
- Scene Progression Analysis

## 🧠 AI

- Gemma 4 Vision
- AI Reasoning Engine
- Multimodal Context Fusion

## 🎙 Speech

- Whisper Speech Recognition
- Automatic Language Detection

## 📝 OCR

- EasyOCR
- Subtitle Detection
- Sign & Text Recognition

## 📱 Caption Studio

- Professional Caption
- Sarcastic Caption
- Tech Humor Caption
- Meme Caption
- AI Summary
- Smart Hashtags
- SEO Keywords

---

# 🏗 System Architecture

```
                 Video Upload
                      │
                      ▼
             Frame Extraction
                      │
                      ▼
             Scene Detection
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼

 Speech-to-Text     OCR Engine    Keyframes
   (Whisper)       (EasyOCR)         │

      └───────────────┼───────────────┘
                      ▼

            Gemma 4 Vision Analysis

                      ▼

            AI Reasoning Engine

                      ▼

          Intelligent Caption Studio
```

---

# ⚙ AI Pipeline

1. Upload Video
2. Extract Frames
3. Detect Key Frames
4. Speech Recognition
5. OCR Extraction
6. Visual Understanding
7. AI Reasoning
8. Caption Generation

---

# 📊 Output

QuackVision AI generates:

✅ Professional Caption

✅ Sarcastic Caption

✅ Tech Humor Caption

✅ Meme Caption

✅ AI Summary

✅ SEO Keywords

✅ Smart Hashtags

✅ Language Detection

✅ Confidence Score

---

# 🛠 Tech Stack

## Frontend

- React
- Vite
- Axios

## Backend

- FastAPI
- Python

## AI Models

- Gemma 4
- Whisper
- EasyOCR

## Computer Vision

- OpenCV

## Deployment

- Docker
- Vercel

---

# 📂 Project Structure

```
QuackVision-AI

│

├── frontend

│ ├── src

│ ├── public

│ └── package.json

│

├── backend

│ ├── app

│ │ ├── agents

│ │ ├── api

│ │ ├── pipeline

│ │ ├── uploads

│ │ └── main.py

│ │

│ ├── Dockerfile

│ ├── docker-compose.yml

│ └── requirements.txt

│

└── README.md
```

---

# 🚀 Local Installation

## Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend

```
http://localhost:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend

```
http://localhost:5173
```

---

# 🐳 Docker

```bash
docker compose build

docker compose up
```

---

# 📸 Application Preview

## 🏠 Landing Page

The modern landing page introduces QuackVision AI and highlights its multimodal AI capabilities.

![Landing Page](screenshots/Hero.png)

---

## 📤 Video Upload

Upload videos through a clean drag-and-drop interface supporting multiple formats.

![Upload Video](screenshots/Generator.png)

---

## ⚡ Intelligent AI Processing

The AI pipeline visualizes every processing stage in real time, including:

- Frame Extraction
- Scene Detection
- Speech Recognition
- OCR
- Visual Understanding
- Story Reasoning
- Caption Generation

### Processing Started

![Processing 1](screenshots/loadingScreen.png)

### Audio Extraction

![Processing 2](screenshots/loadingscreen_02.png)

### Story Understanding

![Processing 3](screenshots/loadingscreen_03.png)

---

## 🎬 Video Understanding

The uploaded video is analyzed together with AI-generated insights such as confidence score, language detection, mood analysis, and video category.

![Video Analysis](screenshots/video_preview.png)

---

## ✍️ AI Caption Studio

QuackVision AI automatically generates multiple caption styles suitable for different audiences.

- 🎓 Professional Caption
- 😏 Sarcastic Caption
- 🤖 Tech Humor Caption
- 😂 Meme Caption

![Caption Studio](screenshots/caption_01.png)

---

## 📈 AI Insights

Along with captions, the platform generates:

- AI Summary
- Smart Hashtags
- SEO Keywords

![AI Insights](screenshots/caption_02.png)

---

## 📄 Export AI Report

Export generated content as:

- 📋 Copy All
- 📄 TXT
- 📦 JSON
- 📑 PDF

![Export](screenshots/downloadable_1.png)



---

# 🌐 Live Demo

Frontend

**https://quack-vision-5blsmbad2-vaibhavpandey78ks-projects.vercel.app/**

---

# 🎥 Demo Video

**YOUTUBE_OR_GOOGLE_DRIVE_LINK**

---

# 💻 GitHub Repository

**https://github.com/vaibhavpandey78k/QuackVision-AI**

---

# 🎯 Future Scope

- Viral Caption Scoring
- AI Thumbnail Generation
- Multi-language Caption Generation
- Batch Video Processing
- Team Collaboration
- Social Media Publishing
- Brand Style Personalization

---

# 👤 Team

## QUACKSHIELD X

### Team Member

**Vaibhav Pandey**

---

# 🏆 Built For

AMD Developer Hackathon – ACT II

---

# 📄 License

This project is developed exclusively for the AMD Developer Hackathon – ACT II.
