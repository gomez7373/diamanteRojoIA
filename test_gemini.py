import os
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar API Key desde .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Usar el modelo correcto
model = genai.GenerativeModel(model_name="gemini-pro")

# Enviar prompt
response = model.generate_content("¿Quién eres?")
print(response.text.strip())
