import streamlit as st
from utils import generate_blog_post, humanize_text

st.set_page_config(page_title="AI Writing Assistant", layout="centered")

st.title("✍️ AI Writing Assistant")
st.write("Enter a topic and get a blog post + humanized rewrite!")

topic = st.text_input("Enter a blog topic", placeholder="e.g., The Benefits of Meditation")

if st.button("Generate"):
    if topic.strip() != "":
        with st.spinner("Generating..."):
            blog = generate_blog_post(topic)
            humanized = humanize_text(blog)

        st.subheader("📝 AI-Generated Blog Post")
        st.write(blog)

        st.subheader("💬 Humanized Rewrite")
        st.write(humanized)
    else:
        st.warning("Please enter a topic to proceed.")
