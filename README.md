# 💬 Sentiment Analysis App (Streamlit + Transformers)

A lightweight AI-powered Sentiment Analyzer built with Streamlit, Hugging Face Transformers, and PyTorch.
This simple web app performs real-time sentiment analysis — type any text and instantly see whether it’s Positive or Negative!

## 🚀 Features

- 🧠 Uses pre-trained Transformer model (`distilbert-base-uncased-finetuned-sst-2-english`)
- 💬 Real-time web app with Streamlit
- ⚡ Fast & lightweight — runs locally or on Streamlit Cloud
- 🧩 Uses **PyTorch** backend

---

## 🛠️ Installation

```bash
git clone https://github.com/avnikumar/ai-sentiment-analysis-app.git
cd sentiment-analyzer
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
