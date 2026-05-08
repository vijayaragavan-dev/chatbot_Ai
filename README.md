# 🤖 Offline AI Chatbot using Transformers

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
![Mode](https://img.shields.io/badge/Mode-Offline-success)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

A beginner-friendly yet professional offline AI chatbot built using **Python**, **PyTorch**, and **Hugging Face Transformers**.

This project demonstrates how transformer-based conversational AI systems work locally without relying on paid APIs like OpenAI or Gemini. The chatbot uses a pretrained conversational transformer model and runs fully on the local machine after the initial model download.

The project is designed for:

* AI/ML learning
* NLP fundamentals
* Transformer experimentation
* Internship portfolios
* Beginner-to-intermediate AI development

---

# 🚀 Features

* ✅ Fully offline chatbot after first model download
* ✅ Uses Hugging Face Transformer models
* ✅ Continuous multi-turn conversation
* ✅ Safe and clean terminal interface
* ✅ Proper tokenizer + transformer inference pipeline
* ✅ Conversation history management
* ✅ Token overflow protection
* ✅ Graceful exit handling (`exit`, `quit`, `Ctrl+C`)
* ✅ Error handling and runtime safety
* ✅ Beginner-friendly project structure
* ✅ Internship-ready documentation

---

# 🧠 Technologies Used

| Technology   | Purpose                                 |
| ------------ | --------------------------------------- |
| Python       | Main programming language               |
| Transformers | Transformer model loading and inference |
| PyTorch      | Tensor operations and model backend     |
| Hugging Face | Pretrained NLP models                   |
| Tokenizers   | Text tokenization                       |
| VS Code      | Development environment                 |

---

# 📂 Project Structure

```text
chatbot_ai/
│
├── chatbot.py          # Main chatbot application
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
├── info.txt            # Detailed technical explanation
└── screenshots/        # Project screenshots
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/vijayaragavan-dev/chatbot_Ai.git
```

---

## 2️⃣ Enter Project Folder

```bash
cd chatbot_Ai
```

---

## 3️⃣ Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv .venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows PowerShell

```powershell
.venv\Scripts\activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Chatbot

```bash
python chatbot.py
```

---

# 💬 Example Conversation

```text
You: Hello
Chatbot: Hello! How can I assist you today?

You: Give simple Java code for addition of two numbers.
Chatbot: Here is a simple Java program for adding two numbers...

You: What is machine learning?
Chatbot: Machine learning is a branch of AI where systems learn patterns from data.

You: exit
Chatbot: Goodbye! Thanks for chatting.
```

---

# 🔍 Internal Workflow

```text
User Input
    ↓
Tokenizer
    ↓
Transformer Model
    ↓
Response Generation
    ↓
Text Decoding
    ↓
Chatbot Response
```

---

# 🧠 AI Concepts Used

This project includes practical implementation of:

* Natural Language Processing (NLP)
* Tokenization
* Transformer Architecture
* Text Generation
* Conversational AI
* Attention Mechanism
* Inference Pipeline
* Conversation History Management

---

# 🛡️ Safety & Stability Features

* Input validation
* Exception handling
* Token overflow protection
* Clean shutdown handling
* Dependency validation
* Safe offline execution

---

# 📸 Screenshots

Add chatbot screenshots inside:

```text
screenshots/
```

Recommended screenshots:

* Startup screen
* Chat example
* Technical question response

---

# 🚀 Future Improvements

Planned enhancements:

* GUI interface (Tkinter / PyQt)
* Voice assistant support
* PDF question-answering
* Resume analyzer integration
* AI coding assistant
* Chat export functionality
* Better conversational memory
* Local vector database integration

---

# 🎯 Learning Outcomes

Through this project, I learned:

* Transformer-based NLP systems
* Hugging Face ecosystem
* PyTorch inference workflow
* Tokenization pipeline
* AI project structuring
* Local LLM execution
* Error handling in AI applications
* Professional GitHub project organization

---

# 💼 Internship / Portfolio Value

This project demonstrates:

* Practical AI development
* NLP fundamentals
* Transformer implementation
* Python backend skills
* Problem-solving ability
* Project structuring skills

Suitable for:

* AI/ML internship applications
* GenAI portfolio projects
* NLP learning showcase

---

# ⚠️ Important Notes

* First run requires internet connection for model download.
* After download, chatbot works offline.
* CPU inference may be slower on low-end systems.
* Responses depend on pretrained model quality.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Vijayaragavan**

Aspiring Generative AI Engineer
Passionate about AI, NLP, and software development.
