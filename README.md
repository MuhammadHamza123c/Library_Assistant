# 📚 Library_Assistant

> “They needed it, but they didn’t build it — so I did.” 💡  
> An AI-powered assistant to make libraries smarter, faster, and student-friendly.

---

## 🚀 Project Overview

In many libraries, students struggle to find the right books, understand borrowing rules, or get quick help. This project solves that problem by creating an **AI Library Assistant** that:

- Helps students **find relevant books** using smart search
- Provides **library rules, timings, and issue policies**
- Extracts text from **uploaded book images** using OCR
- Works through **WhatsApp chatbot integration**

---

## 🧠 Features

- 📘 Book suggestions based on subject
- 🔍 Book finding using vector embeddings
- 🕒 Replies about rules, timings, and book limits
- 🖼️ OCR support to read book titles from images
- 💬 Chatbot replies through WhatsApp (via n8n)

---

## 🛠️ Tech Stack

| Component | Tech |
|----------|------|
| Language Model | LLaMA 3 (8B) via Groq API |
| Embeddings | HuggingFace `thenlper/gte-large` |
| Vector Store | Chroma DB |
| Backend | FastAPI |
| OCR | Tesseract + Pillow |
| Automation | n8n |
| WhatsApp Bot | n8n + ngrok tunnel |

---

## 🧩 How It Works

1. **User Query** → Sent via API or WhatsApp
2. **Vector Search** → Chroma returns relevant book content using `gte-large` embeddings
3. **Prompt Building** → LangChain builds prompt with memory + context
4. **Response** → LLaMA 3 (via Groq) generates the final reply
5. **Memory** → Previous messages are tracked and used for better responses
6. **Image OCR** → Text is extracted from uploaded book images
7. **n8n WhatsApp Bot** → Sends user messages to FastAPI and replies back with AI responses

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Library_Assistant.git
cd Library_Assistant
