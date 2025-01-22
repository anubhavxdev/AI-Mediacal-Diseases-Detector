import os
import base64
from groq import Groq

api_key = os.environ.get('GROQ_API_KEY')

if not api_key:
    raise ValueError("Error: Dhasu is not happy.")

image_path = 'acne.png'
with open(image_path, 'rb') as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

client = Groq(api_key=api_key)

query = 'what happened on my face?'
model = "llama-3.2-90b-vision-preview"

message = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": query
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}"
                }
            }
        ]
    }
]

chat_completion = client.chat.completions.create(
    model=model,
    messages=message,
)

print(chat_completion.choices[0].message.content)
