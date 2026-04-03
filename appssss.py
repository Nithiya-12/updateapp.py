import streamlit as st

st.title("📩 Spam Detection App")

msg = st.text_input("Enter your message")

if st.button("Check"):
    if msg.strip() == "":
        st.warning("⚠️ Please enter a message")
    else:
        msg = msg.lower()
        spam_words = ["offer", "win", "free", "money", "click"]

        if any(word in msg for word in spam_words):
            st.error("🚨 Spam Message")

            # Play spam sound
            audio_file = open("spam.mp3", "rb")
            st.audio(audio_file.read(), format="audio/mp3")

        else:
            st.success("✅ Not Spam")

            # Play success sound
            audio_file = open("notspam.mp3", "rb")
            st.audio(audio_file.read(), format="audio/mp3")
