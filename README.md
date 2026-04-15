# 🎥 YouTube → Insightful Article & PDF Generator

Convert any YouTube video into a **structured article** and **downloadable PDF** using AI.

This project extracts transcripts from YouTube videos and uses an LLM to generate readable, insightful content.

---

## 🚀 Features

* 🎬 Extract video metadata (title, channel)
* 📝 Fetch transcript using YouTube Transcript API
* ✍️ Generate structured article using Gemini AI
* 📄 Convert article into downloadable PDF
* 🌐 Simple and interactive Streamlit UI

---

## 🧠 How It Works

```
YouTube URL
   ↓
Transcript API
   ↓
LLM (Article Generation)
   ↓
PDF Generator
   ↓
User Download
```

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM:** Google Gemini (`google-generativeai`)
* **Transcript API:** youtube-transcript-api
* **PDF Generation:** FPDF
* **Deployment:** AWS EC2

---

## 📂 Project Structure

```
youtube-insight-generator/
│
├── app.py
├── requirements.txt
├── .env
│
├── services/
│   ├── llm_service.py
│   ├── pdf_service.py
|   ├── transcript.py
│
└── outputs/
    └── article.pdf
```

---

## ⚙️ Setup Instructions

###  Clone Repository

```
git clone https://github.com/your-username/youtube-article_generator.git
cd youtube-article-generator
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt


###  Add API Key
Create a `.env` file:
GOOGLE_API_KEY=your_api_key_here


###  Run Application
streamlit run app.py

---

## ⚠️ Limitations

* Some YouTube videos do not have transcripts
* YouTube may block requests from cloud providers (AWS EC2)
* Depends on availability of captions

---

## 📈 Future Improvements

* 🎧 Add audio-based transcription (Whisper)
* 💬 Chat with video (RAG)
* 📝 Generate LinkedIn posts / notes
* 🌍 Multi-language support




⭐ If you found this project useful, consider giving it a star!
