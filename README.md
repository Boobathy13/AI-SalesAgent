
# 🤖 AI Sales Agent – Intelligent Conversational Product Assistant

**FutureStack GenAI Hackathon 2025**
Sponsors: **Meta | Cerebras | Docker**
License: MIT

---

## 📌 Overview

AI Sales Agent is a **GenAI-powered conversational backend** that enables businesses to provide **real-time, AI-driven sales assistance**.

Built for the **FutureStack GenAI Hackathon**, this project showcases how cutting-edge **speech-to-text (STT)**, **natural language processing (NLP)**, and **text-to-speech (TTS)** technologies can power a seamless customer engagement experience.

The current version focuses on the **backend service**, while **frontend, multi-agent orchestration, and containerized cloud deployment (Docker)** are planned as future milestones.

---

## ✨ Features (Current)

✅ Conversational backend with **FastAPI**
✅ **Product Q&A** powered by static JSON / `.env`
✅ **LiveKit + Cartesia** for real-time speech processing
✅ Context-aware **AI-driven responses**
✅ Ready-to-integrate with frontend or call systems

---

## 🧰 Tech Stack

| Layer       | Technology                         |
| ----------- | ---------------------------------- |
| Backend     | Python 3.10, FastAPI               |
| STT/TTS     | LiveKit Agents, Cartesia           |
| NLP Engine  | OpenAI / Hugging Face Models       |
| Data Source | `.env` / JSON (no DB required)     |
| Deployment  | Localhost (Future: Docker + Cloud) |

---

## 🔧 Prerequisites

* Python 3.10+
* FastAPI & pip for dependencies
* LiveKit & Cartesia API keys
* (Optional) Docker for future deployment

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-sales-agent.git
cd ai-sales-agent
```

### 2️⃣ Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Configure Environment

`.env` file example:

```env
LIVEKIT_API_KEY=your_livekit_key
LIVEKIT_API_SECRET=your_livekit_secret
CARTESIA_API_KEY=your_cartesia_key
PRODUCTS_FILE=products.json
```

### 4️⃣ Run Backend

```bash
uvicorn app:app --reload
```

Backend available at: `http://localhost:8000`

---

## 🌐 API Endpoints

📤 **Ask Question**

```http
POST /ask
{
  "query": "Tell me about Product A"
}
```

📊 **Get Products**

```http
GET /products
```

---

## 🧭 Project Structure

```
AI-Sales-Agent/
├── app.py                # FastAPI backend entry
├── agents/               # Agent logic
├── config/               # env & product configs
├── products.json         # Product data
├── requirements.txt      # Dependencies
└── README.md             # You’re reading it!
```

---

## 🚀 Future Roadmap

🖥️ **Frontend Integration** – React UI with real-time chat & voice
🤖 **Multi-Agent System** – Sales, Support, Recommendations working together
🐳 **Dockerized Deployment** – Containerized for scale (aligning with sponsor Docker 🚀)
⚡ **Cerebras Acceleration** – Faster inference for GenAI workloads
🌐 **Cloud & Meta APIs** – Expanding reach with Meta AI ecosystem
📊 **Analytics Dashboard** – Insights into customer queries & trends

---

## 📝 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

* Boobathy R

---

