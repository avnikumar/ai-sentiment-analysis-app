import streamlit as st
from transformers import pipeline

# Page setup
st.set_page_config(page_title="Sentiment Analyzer", page_icon="💬")

st.title("💬 Sentiment Analysis App")
st.write("Type a sentence and find out whether it's Positive or Negative!")

# Cache the model so it doesn't reload every time
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", framework="pt")  # use PyTorch backend

analyzer = load_model()

# User input
user_text = st.text_area("Enter text here:", "How is your day? This was bad.")

# When user clicks the button
if st.button("Analyze Sentiment"):
    if user_text.strip():
        result = analyzer(user_text)
        label = result[0]['label']
        score = result[0]['score']
        
        # Display result
        st.subheader("Result:")
        st.write(f"**Sentiment:** {label}")
        st.write(f"**Confidence:** {score:.2%}")
    else:
        st.warning("Please enter some text to analyze.")
