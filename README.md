# 📚 Emerson University Library Assistant

> “They needed it, but they didn’t build it — so I did.” 💡  
> An AI-powered assistant to make the university library smarter, faster, and student-friendly.

---

## 🚀 Project Overview

At Emerson University Multan, students often struggle to find books related to their field due to a disorganized library system. To solve this, I created an **AI Library Assistant** that:

- Helps students **find relevant books** using semantic search
- Provides **library rules, timings, and issue policies**
- Accepts **uploaded book images** and extracts text using OCR
- Works as a **chatbot over WhatsApp** via `n8n` workflows

---

## 🧠 Features

- 📘 Book suggestions based on subject
- 🔍 Smart book search using vector embeddings
- 🕒 Answers about rules, timings, and borrowing limits
- 🖼️ OCR support to read book titles from images
- 💬 WhatsApp integration using `n8n` + `ngrok`

---

## 🛠️ Tech Stack

| Component | Tech |
|----------|------|
| Language Model | [LLaMA 3 (8B)](https://groq.com) via Groq API |
| Embeddings | HuggingFace `thenlper/gte-large` |
| Vector Store | Chroma DB |
| Backend | FastAPI |
| Image OCR | Tesseract OCR + Pillow |
| Workflow Automation | n8n |
| WhatsApp Integration | n8n + ngrok tunnel |

---

## 🧩 How It Works

1. **Query**: Student sends a question via web or WhatsApp.
2. **Search**: The system searches similar content using vector embeddings.
3. **Prompting**: A custom prompt is generated with context and memory.
4. **Response**: LLaMA 3 replies with a short, helpful answer.
5. **Memory**: The assistant remembers recent queries and replies.
6. **Image OCR**: If the user uploads a book image, it extracts text using Tesseract.
7. **WhatsApp Bot**: n8n forwards WhatsApp messages to FastAPI and sends back AI replies.

---

## 📦 Installation

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/emerson-library-assistant.git
cd emerson-library-assistant
