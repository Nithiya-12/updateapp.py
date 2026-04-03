import streamlit as st

st.title("📩 Spam Detection App")

msg = st.text_input("Enter your message")

if st.button("Check"):
    msg = msg.lower()
    spam_words = ["offer", "win", "free", "money", "click"]

    if any(word in msg for word in spam_words):
        st.error("🚨 Spam Message")
    else:
        st.success("✅ Not Spam")
