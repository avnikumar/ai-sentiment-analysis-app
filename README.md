# 💬 Sentiment Analysis App (Streamlit + Hugging Face Transformers)

This project is a fully interactive **Sentiment Analysis Web Application** built using **Streamlit** and **Hugging Face Transformers**.  
The application uses a pretrained model from Hugging Face’s Model Hub to analyze text and determine whether the sentiment is **Positive** or **Negative**.

---

# 🧠 What This Project Uses (Full Explanation)

## ✔ Hugging Face Transformers  
This app uses the **Transformers** library from Hugging Face — a powerful library providing state‑of‑the‑art NLP models.

You import it here:

```python
from transformers import pipeline
```

The app uses the **Hugging Face `pipeline` API**, which makes it extremely simple to load a pretrained NLP model.

---

## ✔ Sentiment Analysis Pipeline  
The following line automatically loads a pretrained sentiment analysis model from Hugging Face:

```python
pipeline("sentiment-analysis", framework="pt")
```

This loads:

### **Model:**  
```
distilbert-base-uncased-finetuned-sst-2-english
```

This is a **DistilBERT** model (a smaller, faster version of BERT), fine‑tuned for sentiment classification on the SST‑2 dataset.

### Why DistilBERT?  
- 60% faster than BERT  
- 40% smaller  
- ~95% of BERT’s accuracy  
- Perfect for lightweight web apps  

So **YES — this project directly uses Hugging Face** for loading the model, tokenizer, and performing inference.

---

## ✔ PyTorch Backend  
The model runs with the PyTorch backend because of:

```python
framework="pt"
```

If PyTorch is installed, Hugging Face uses it automatically.

---

## ✔ Streamlit Frontend  
Streamlit is used to build the UI:

- Text input area  
- "Analyze Sentiment" button  
- Display sentiment + confidence score  

Streamlit makes it easy to turn ML models into interactive apps.

---

# 🚀 Features

- Real-time sentiment prediction  
- Hugging Face Transformers for NLP  
- Pretrained BERT-family model  
- Fast and lightweight  
- Clean UI  
- Streamlit caching to avoid repeated model loading  

---

# 📦 Installation

## **1. Clone the repository**
```bash
git clone https://github.com/YOUR-USERNAME/sentiment-app.git
cd sentiment-app
```

## **2. Create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate       # Mac/Linux
```

## **3. Install dependencies**
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install streamlit transformers torch
```

---

# ▶️ Run the App

```bash
streamlit run app.py
```

App runs at:

```
http://localhost:8501
```

---

# 🗂 Project Structure

```
sentiment-app/
│
├── app.py                # Streamlit UI + HF model loading
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```

---

# 📘 Code Breakdown

### Load Hugging Face Sentiment Pipeline
```python
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", framework="pt")
```

### Why `@st.cache_resource`?
- Prevents the model from loading repeatedly  
- Speeds up user interactions  

### UI Interaction
```python
result = analyzer(user_text)
label = result[0]['label']
score = result[0]['score']
```

Returns:
- `label`: POSITIVE / NEGATIVE  
- `score`: model confidence  

---

# 🔧 Customization Options

### Use Full BERT:
```python
pipeline("sentiment-analysis",
         model="textattack/bert-base-uncased-SST-2")
```

### Use RoBERTa:
```python
pipeline("sentiment-analysis",
         model="cardiffnlp/twitter-roberta-base-sentiment")
```

### Use Multilingual Model:
```python
pipeline("sentiment-analysis",
         model="nlptown/bert-base-multilingual-uncased-sentiment")
```

---

# 📝 Example `requirements.txt`

```
streamlit==1.32.0
transformers==4.38.1
torch>=2.0.0
```

---

# 📄 License  
This project is licensed under the **MIT License**.  
© 2025 Avnish Kumar

---

# ⭐ Support  
If you like this project, please ⭐ star the repo!  
Your support motivates more projects like this 🚀  
