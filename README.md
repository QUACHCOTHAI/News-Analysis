# 🧠 News Analyzer Chatbot

**A Human–Machine Interaction System for Analyzing Online News Content**

This project is a web-based chatbot that allows users to submit links to online news articles and receive AI-generated summaries and insights. The system uses a Large Language Model (LLM), integrated via the Gemini API, to analyze and respond conversationally.

---

## 🚀 Features

- 🔗 Input any online news URL
- 🤖 Summarize and analyze content using Gemini API
- 💬 Chat-style interface (like Messenger)
- 🖍️ Highlighted headers, clean markdown rendering
- 🌐 Built with Flask, HTML/CSS/JS

---

## 🧩 Technologies Used

- **Python 3.8+**
- **Flask** – backend server
- **Gemini API** – LLM integration
- **HTML/CSS/JavaScript** – frontend interface
- **Markdown formatting** for clean AI output

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/news-analyzer-chatbot.git
cd news-analyzer-chatbot
```

### 2. Set up Python virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate     # On Linux/macOS
venv\Scripts\activate      # On Windows
```

### 3. Install required dependencies

```bash
pip install -r requirements.txt
```

> ✅ `requirements.txt` includes:
> ```
> Flask
> requests
> beautifulsoup4
> python-dotenv
> google-generativeai
> ```

### 4. Set your Gemini API key

You can store your API key in a `.env` file in the root directory:

```
GEMINI_API_KEY=your_gemini_api_key_here
Model_Name=your_model_name 
```

Or directly inside `app.py` (not recommended for production).

---

## ▶️ Run the application

```bash
python app.py
```

Then open your browser at:  
**http://localhost:5000**

---

## 📁 Project Structure

```
news-analyzer-chatbot/
├── app.py
├── requirements.txt
├── .env
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

---

## 🖼️ Example Output

**User:** https://vnexpress.net/some-news  
**Bot:**
```
**1. Summary**: This article discusses...  
**2. Key Points**:  
- Point A  
- Point B  
**3. AI Opinion**: The article highlights...
```

---

## 📄 License

MIT License

