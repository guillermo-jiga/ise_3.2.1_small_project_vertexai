import os
import vertexai
from vertexai.generative_models import GenerativeModel
import streamlit as st

# TODO: Rename ".env.template" to ".env" and add your project ID to it.
from dotenv import load_dotenv

load_dotenv()

vertexai.init(project=os.environ.get("PROJECT_ID"), location="us-central1")

model = GenerativeModel("gemini-1.5-flash-002")

st.title("Find your neighboring states")
st.write("The neighboring states are:")

users_state = st.text_input("Enter your state")

if users_state:  # Ensure input is not empty before calling API
    response = model.generate_content(
        f"What are all of the neighboring states: {users_state}",
        generation_config={
            "temperature": 0.1,
            "max_output_tokens": 100,
        }
    )

    # Display response in Streamlit
    st.write("The neighboring states are:")
    st.write(response.text)  # Correct way to display the response

# print(response.text)
