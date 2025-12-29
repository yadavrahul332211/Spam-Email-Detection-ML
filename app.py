import streamlit as st
import pickle

# load model & vectorizer
model = pickle.load(open("model.pkl", "rb"))
cv = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📧 Spam Email Detection App")
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

