import streamlit as st
import pickle
from PIL import Image

# Show logo
logo = Image.open("logo.png")
st.image(logo, width=180)

st.title("📧 Email Scam Detection App")

# Load model & vectorizer
model = pickle.load(open("model.pkl", "rb"))
cv = pickle.load(open("vectorizer.pkl", "rb"))

st.write("Enter a message to check whether it is Spam or Ham")

user_input = st.text_area("Enter your message here")

if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please enter a message")
    else:
        data = cv.transform([user_input])
        prediction = model.predict(data)

        if prediction[0] == 1:
            st.error("🚫 This message is SPAM")
        else:
            st.success("✅ This message is HAM (Not Spam)")


