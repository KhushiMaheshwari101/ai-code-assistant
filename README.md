# 💻 AI Code Assistant

> A real-time AI-powered coding assistant that helps you write better code — instantly!

 **Live Demo:** [Click here to try it!]
(https://ai-code-assistant-ynkycvexwue7sn5hnjt2sp.streamlit.app/)

---

##  Overview

AI Code Assistant is a web-based tool that acts as your personal coding companion. Just write your code and let the AI suggest improvements, find bugs, complete incomplete code, and answer your coding questions — all in real time.
 **Hinglish Support** — The AI responds in **Hinglish (Hindi + English mix)** to make the interaction feel more natural, friendly, and comfortable — especially for Indian developers. No more robotic responses, just a helpful coding buddy that talks like a friend! 
 


##  Features

-  **Smart Suggestions** — Get instant AI-powered code improvement recommendations
-  **Error Detection** — Identifies bugs, warnings, and logical mistakes with line numbers
-  **Code Completion** — Automatically completes your incomplete code
-  **AI Chat** — Ask anything about your code and get clear explanations
-  **Multi-language Support** — Works with Python, JavaScript, Java, C++, TypeScript, and more
-  **Hinglish Responses** — AI explains in Hindi + English mix for a friendly, relatable experience


---



##  Tech Stack

| Technology | Purpose |
|-----------|---------|
| [Streamlit](https://streamlit.io) | Web Application Framework |
| [Groq API](https://groq.com) | Ultra-fast LLM Inference |
| [LLaMA 3.3 70B](https://groq.com) | Underlying AI Model |
| Python | Core Language |

---

##  Project Structure

```
ai-code-assistant/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (not tracked)
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- A free [Groq API Key](https://console.groq.com)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/KhushiMaheshwari101/ai-code-assistant.git
cd ai-code-assistant
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up environment variables**

Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```

**4. Run the application**
```bash
streamlit run app.py
```

Open your browser and go to `http://localhost:8501` 🎉

---

##  Deployment

This project is deployed on **Streamlit Cloud** (free tier).

To deploy your own instance:
1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repository and set `app.py` as the main file
5. Add your `GROQ_API_KEY` in the Secrets section
6. Click **Deploy!**

---

##  Demoshots


> <img width="1880" height="1036" alt="image" src="https://github.com/user-attachments/assets/2c7041cd-0792-4d22-9a46-e19ab63584c5" />
<img width="1791" height="984" alt="image" src="https://github.com/user-attachments/assets/e93e227c-e12b-4f30-8818-a273fbbb0226" />



---

##  Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a [GitHub Issue](https://github.com/KhushiMaheshwari101/ai-code-assistant/issues).

---

##  License

This project is open source and available under the [MIT License](LICENSE).

---

##  Author

**Khushi Maheshwari**

[![GitHub](https://img.shields.io/badge/GitHub-KhushiMaheshwari101-black?style=flat&logo=github)](https://github.com/KhushiMaheshwari101)

---

⭐ If you found this project helpful, please consider giving it a **star**!
