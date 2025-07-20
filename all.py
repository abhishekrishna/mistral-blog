import os
import streamlit as st
from mistralai import Mistral

# Setup Mistral API
api_key = "77vgQir3lUzP1Lj45pzjpy5PYbVBXgD3"
model = "mistral-large-latest"
client = Mistral(api_key=api_key)

# Streamlit UI
st.set_page_config(page_title="📝 Mistral Blog Generator", layout="centered")
st.title("📝 Blog Post Generator with Mistral")

with st.form("blog_form"):
    topic = st.text_input("Blog Topic", value="The Future of AI in Education")
    tone = st.selectbox("Tone", ["Professional", "Casual", "Humorous", "Inspirational"], index=0)
    audience = st.text_input("Target Audience", value="Teachers and EdTech Startups")
    word_count = st.slider("Word Count", 300, 2000, 800)
    submitted = st.form_submit_button("Generate Blog")

if submitted:
    with st.spinner("Generating blog post..."):
        # One-line prompt template
        prompt = f"""Write a detailed blog post on "{topic}" in a {tone} tone for "{audience}", targeting around {word_count} words. Include an introduction, 2–4 informative sections, and a conclusion. Use markdown formatting with headings and bullet points."""

        chat_response = client.chat.complete(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        blog_content = chat_response.choices[0].message.content

    st.markdown(blog_content)