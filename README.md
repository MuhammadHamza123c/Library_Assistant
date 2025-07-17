📚 Library_Assistant
“They needed it, but they didn’t build it — so I did.” 💡
An AI-powered assistant to make libraries smarter, faster, and more student-friendly.

🚀 Project Overview
Students often struggle in traditional libraries — from finding books to understanding rules. Library_Assistant solves this by creating an AI chatbot that:

Finds books using natural language

Provides quick answers about library timings and rules

Reads book images via OCR

Supports conversations over WhatsApp

🧠 Features
📘 Subject-wise Book Recommendations

🔍 Smart Search with Embeddings (ChromaDB + GTE-Large)

🕒 Instant Responses about library rules, timings, issue policies

🖼️ Image OCR to extract book names from images

💬 Chatbot Support via WhatsApp using n8n + FastAPI

🛠️ Tech Stack
Component	Tech
LLM	LLaMA 3 (8B) via Groq API
Embeddings	thenlper/gte-large (HuggingFace)
Vector Store	Chroma DB
Backend API	FastAPI
OCR Engine	Tesseract + Pillow
Automation	n8n
Messaging	WhatsApp (via n8n + ngrok)

🧩 How It Works

flowchart TD
    A[User Message (WhatsApp/API)] --> B[FastAPI Endpoint]
    B --> C[Vector Search (Chroma DB)]
    C --> D[Prompt Creation (LangChain)]
    D --> E[LLaMA 3 API via Groq]
    E --> F[Reply Sent to User via WhatsApp (n8n)]
    B --> G[OCR Module (if Image Sent)]


📦 Installation & Setup
✅ Prerequisites
Python 3.10+

Node.js (for n8n)

Ngrok account

Tesseract OCR installed


 Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/Library_Assistant.git
cd Library_Assistant
