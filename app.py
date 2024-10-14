import os

import vertexai
from vertexai.generative_models import GenerativeModel

# TODO: Rename ".env.template" to ".env" and add your project ID to it.
from dotenv import load_dotenv
load_dotenv()

vertexai.init(project=os.environ.get('PROJECT_ID'), location="us-central1")

model = GenerativeModel("gemini-1.5-flash-002")

response = model.generate_content(
    "What's a good name for a flower shop that specializes in selling bouquets of dried flowers?"
)

print(response.text)