import os

import groq


groq.

API_KEY = os.getenv("API_KEY")

groq_client = groq.client(
    api_key=API_KEY
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)