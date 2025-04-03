import openai
import os
from dotenv import load_dotenv

# Cargar la clave desde .env
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Enviar la solicitud al modelo GPT-3.5 con el nuevo cliente
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres Charlie, un asistente lógico, amable y enfocado en el aprendizaje."},
        {"role": "user", "content": "¿Quién eres?"}
    ]
)

print(response.choices[0].message.content.strip())
