# Install dependencies if not already
# pip install streamlit google-genai pillow

import streamlit as st
from google import genai
from PIL import Image
import time
import io
# Install dependencies if not already
# pip install streamlit google-genai pillow

import streamlit as st
from google import genai
from PIL import Image
import time
import io

# --------------------------
# Gemini Client
# --------------------------
client = genai.Client(api_key="AIzaSyARlr9KGNtlVrmMPmjhfJPfb1e-nox1Lrw")  # Replace with your key
model = "gemini-2.5-flash"

# --------------------------
# Streamlit Page Config
# --------------------------
st.set_page_config(page_title="Venkat GPT Multi-modal", page_icon="🤖", layout="wide")
st.title("Venkat GPT Multi-modal LLM")
st.write("Ask questions, upload images, and get AI responses powered by Google Gemini LLM.")

# --------------------------
# Session State for Chat
# --------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------
# User Input
# --------------------------
user_input = st.text_area("Enter your query here:", height=120)
uploaded_file = st.file_uploader("Upload an image (optional)", type=["png", "jpg", "jpeg"])

if st.button("Send"):
    if user_input.strip() == "" and uploaded_file is None:
        st.warning("Please enter a query or upload an image!")
    else:
        # Append user message
        st.session_state.messages.append(f"You: {user_input}")

        # If image uploaded, show it and prepare description
        image_desc = ""
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            # For now, just mention an image exists
            image_desc = "\nThe user uploaded an image. Describe it if relevant.\n"

        # Combine text and image info into prompt
        prompt = "You are an expert AI assistant helping answer queries.\n"
        prompt += "\n".join(st.session_state.messages)
        prompt += image_desc

        # Show spinner while AI generates response
        with st.spinner("AI is thinking... 🤖"):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )
                ai_content = response.text

                # Streaming simulation
                placeholder = st.empty()
                message = ""
                for char in ai_content:
                    message += char
                    placeholder.markdown(f"**AI:** {message}")
                    time.sleep(0.01)

                # Append AI response to chat history
                st.session_state.messages.append(f"AI: {ai_content}")

            except Exception as e:
                st.error(f"Error: {e}")

# --------------------------
# Display Chat History
# --------------------------
st.markdown("---")
st.subheader("💬 Conversation History")
for msg in st.session_state.messages:
    if msg.startswith("You:"):
        st.markdown(f"**You:** {msg[5:]}")
    else:
        st.markdown(f"**AI:** {msg[4:]}")

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit & Google Gemini API")

# --------------------------
# Gemini Client
# --------------------------
client = genai.Client(api_key="AIzaSyARlr9KGNtlVrmMPmjhfJPfb1e-nox1Lrw")  # Replace with your key
model = "gemini-2.5-flash"

# --------------------------
# Streamlit Page Config
# --------------------------
st.set_page_config(page_title="Venkat GPT Multi-modal", page_icon="🤖", layout="wide")
st.title("Venkat GPT Multi-modal LLM")
st.write("Ask questions, upload images, and get AI responses powered by Google Gemini LLM.")

# --------------------------
# Session State for Chat
# --------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------
# User Input
# --------------------------
user_input = st.text_area("Enter your query here:", height=120)
uploaded_file = st.file_uploader("Upload an image (optional)", type=["png", "jpg", "jpeg"])

if st.button("Send"):
    if user_input.strip() == "" and uploaded_file is None:
        st.warning("Please enter a query or upload an image!")
    else:
        # Append user message
        st.session_state.messages.append(f"You: {user_input}")

        # If image uploaded, show it and prepare description
        image_desc = ""
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            # For now, just mention an image exists
            image_desc = "\nThe user uploaded an image. Describe it if relevant.\n"

        # Combine text and image info into prompt
        prompt = "You are an expert AI assistant helping answer queries.\n"
        prompt += "\n".join(st.session_state.messages)
        prompt += image_desc

        # Show spinner while AI generates response
        with st.spinner("AI is thinking... 🤖"):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )
                ai_content = response.text

                # Streaming simulation
                placeholder = st.empty()
                message = ""
                for char in ai_content:
                    message += char
                    placeholder.markdown(f"**AI:** {message}")
                    time.sleep(0.01)

                # Append AI response to chat history
                st.session_state.messages.append(f"AI: {ai_content}")

            except Exception as e:
                st.error(f"Error: {e}")

# --------------------------
# Display Chat History
# --------------------------
st.markdown("---")
st.subheader("💬 Conversation History")
for msg in st.session_state.messages:
    if msg.startswith("You:"):
        st.markdown(f"**You:** {msg[5:]}")
    else:
        st.markdown(f"**AI:** {msg[4:]}")

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit & Google Gemini API")
