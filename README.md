# chatbot_ai - Offline AI Chatbot

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Mode](https://img.shields.io/badge/Mode-Offline-orange)

`chatbot_ai` is a beginner-friendly, internship-ready Python project that runs a fully local conversational chatbot in the terminal using Hugging Face DialoGPT. After the first model download, the chatbot works offline and does not require any paid API service. The codebase focuses on readability, robust error handling, and practical NLP engineering patterns like token-based conversation history control.

## Features

- Fully offline chat after first-time model download
- Uses `microsoft/DialoGPT-medium` with automatic fallback to `DialoGPT-small`
- Clean CLI interface with startup banner and usage instructions
- Continuous multi-turn conversation loop
- Safe exit handling for `exit`, `quit`, and `Ctrl+C`
- Rolling context memory with token limit to prevent overflow
- Defensive exception handling around generation and runtime errors
- Beginner-friendly code structure with constants, docstrings, and clear functions
- Dependency versions pinned for reproducible setup
- Portfolio-friendly documentation for interviews and academic submission

## Technologies Used

| Library | Version | Purpose |
|---|---:|---|
| Python | 3.9+ | Primary programming language |
| transformers | 4.40.0 | Loads tokenizer/model and runs text generation |
| torch | 2.2.2 | Tensor operations and inference backend |
| tokenizers | 0.19.1 | Fast tokenizer implementation support |
| huggingface-hub | 0.23.0 | Model download and local cache management |
| safetensors | 0.4.3 | Safe model weight format support |
| tqdm | 4.66.4 | Progress indicators for downloads |
| numpy | 1.26.4 | Numeric compatibility dependency |
| packaging | 24.0 | Version handling utilities |
| filelock | 3.14.0 | Cache file locking for safe operations |
| regex | 2024.4.16 | Regex utilities used by NLP stack |

## Project Structure

```text
chatbot_ai/
├── chatbot.py         # Main chatbot logic and terminal loop
├── requirements.txt   # Pinned dependencies
├── README.md          # Project documentation
├── info.txt           # Detailed technical explanation
└── screenshots/       # Empty folder for demo screenshots
```

## Prerequisites

- Python 3.9 or newer
- `pip` available in terminal
- At least 1 GB free disk space for model and cache
- Internet required only for first run to download model files

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chatbot_ai.git
   ```
2. Enter the project folder:
   ```bash
   cd chatbot_ai
   ```
3. (Recommended) Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
4. Activate the virtual environment:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

```bash
python chatbot.py
```

Expected startup output:

```text
==================================================================
chatbot_ai - Offline AI Chatbot (DialoGPT)
==================================================================
Type your message and press Enter.
Type 'exit' or 'quit' to stop.
Press Ctrl+C to exit safely at any time.
------------------------------------------------------------------
Loading model: microsoft/DialoGPT-medium (first run may take time)...
Model loaded successfully: microsoft/DialoGPT-medium
Using model: microsoft/DialoGPT-medium
You:
```

## Example Interaction

```text
You: Hello chatbot.
Chatbot: Hi! Nice to meet you. How can I help you today?

You: I am preparing for an internship interview.
Chatbot: Great goal. I can help you practice technical and behavioral questions.

You: Ask me one Python question.
Chatbot: Sure. What is the difference between a list and a tuple in Python?

You: A list is mutable and a tuple is immutable.
Chatbot: Correct. Lists can change after creation, while tuples cannot.

You: Give me one ML study tip.
Chatbot: Focus on fundamentals first: preprocessing, model evaluation, and overfitting.

You: exit
Chatbot: Goodbye! Thanks for chatting.
```

## Troubleshooting

1. **Model download fails**
   - Cause: unstable internet on first run.
   - Fix: reconnect and rerun `python chatbot.py`.

2. **Out of memory error**
   - Cause: limited RAM with medium model.
   - Fix: close background apps; fallback to small model occurs automatically.

3. **Very slow responses**
   - Cause: CPU-only inference and long context.
   - Fix: reduce conversation length and keep prompts concise.

4. **Tokenizer or import errors**
   - Cause: broken/mismatched package installs.
   - Fix: recreate venv and reinstall from `requirements.txt`.

5. **Unexpected app close with Ctrl+C**
   - Cause: manual interrupt.
   - Fix: expected behavior; script exits safely by design.

## Future Improvements

- Add GUI version (Tkinter/PyQt)
- Add optional voice input/output
- Add chat transcript export to text or Markdown
- Add persona modes (mentor, interviewer, tutor)
- Add local safety filter for offensive responses
- Add model selection via command-line flag
- Add local retrieval from user notes for grounded responses
- Add simple evaluation logs (latency and token stats)

## License

This project is licensed under the MIT License.
