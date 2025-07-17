# 📚 Library_Assistant

> “They needed it, but they didn’t build it — so I did.” 💡  
> An AI-powered assistant to make libraries smarter, faster, and student-friendly.

---

## 🚀 Project Overview

In many libraries, students struggle to find the right books, understand borrowing rules, or get quick help. This project solves that problem by creating an **AI Library Assistant** that:

- Helps students **find relevant books** using smart semantic search
- Provides **library rules, timings, and issue policies**
- Extracts text from **uploaded book images** using OCR
- Works through **WhatsApp chatbot integration**

---

## 🧠 Features

- 📘 Book suggestions based on subject or topic
- 🔍 Smart search using vector embeddings for accurate book discovery
- ⏱️ Instant replies about library rules, timings, and issue/return limits
- 🖼️ OCR support to extract text from uploaded book cover images
- 💬 Integrated WhatsApp chatbot (via n8n) for direct student communication

---

## 🛠️ Tech Stack

| Component       | Technology                        |
|----------------|------------------------------------|
| Language Model  | LLaMA 3 (8B) via Groq API         |
| Embeddings      | HuggingFace `thenlper/gte-large`  |
| Vector Store    | ChromaDB                          |
| Backend         | FastAPI                           |
| OCR             | Tesseract + Pillow                |
| Workflow Engine | n8n                               |
| WhatsApp Bot    | n8n + ngrok tunnel                |

---

## 🧩 How It Works

1. **User Message** → Sent via FastAPI endpoint or WhatsApp
2. **OCR (optional)** → If image is uploaded, text is extracted using Tesseract
3. **Vector Search** → ChromaDB finds relevant book data using GTE-Large embeddings
4. **Prompt Construction** → LangChain builds prompt with memory + context
5. **AI Response** → LLaMA 3 generates intelligent answers using Groq API
6. **Memory Handling** → Tracks conversation history for contextual answers
7. **n8n Workflow** → Routes WhatsApp messages to FastAPI and sends back replies

---

## 📦 Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Library_Assistant.git
cd Library_Assistant
