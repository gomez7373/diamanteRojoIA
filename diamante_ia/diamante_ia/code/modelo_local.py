import os
import requests
import json
from dotenv import load_dotenv

# Cargar API Key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-1.5-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"

# Cargar personalidad base
with open("essence/charlie_persona.json", encoding="utf-8") as f:
    data = json.load(f)
    SYSTEM_PROMPT = data["system_prompt"]

# Cargar memoria adicional
try:
    with open("essence/memoria_charlie.txt", encoding="utf-8") as f:
        CHARLIE_MEMORY = f.read()
except FileNotFoundError:
    CHARLIE_MEMORY = "Memoria personalizada no encontrada. Charlie no tiene contexto del usuario."

# Palabras clave que activan respuestas largas
ACTIVADORES_DETALLE = [
    "explica más", "dame más detalles", "hazlo largo", "amplía", "cuéntame con más detalle",
    "necesito una explicación más extensa", "desarrolla"
]

def mensaje_activa_modo_largo(texto_usuario):
    return any(frase in texto_usuario.lower() for frase in ACTIVADORES_DETALLE)

def responder(mensaje):
    headers = {"Content-Type": "application/json"}

    # Activar respuesta larga solo si el mensaje lo pide
    modo_largo = mensaje_activa_modo_largo(mensaje)

    # Estilo de instrucción
    if modo_largo:
        instrucciones_extra = (
            "Puedes hablar con más detalle. Usa ejemplos si hace falta. "
            "Organiza la información si es compleja."
        )
    else:
        instrucciones_extra = (
            "Responde de forma breve y natural. No repitas información anterior a menos que se pida. "
            "Evita sobreexplicar. Si el usuario cambia de tema, sigue ese cambio con naturalidad."
        )

    data = {
        "contents": [
            {"role": "model", "parts": [{"text": SYSTEM_PROMPT}]},
            {"role": "user", "parts": [{"text": CHARLIE_MEMORY}]},
            {"role": "user", "parts": [{"text": f"Instrucciones del usuario para estilo de respuesta: {instrucciones_extra}"}]},
            {"role": "user", "parts": [{"text": mensaje}]}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        resultado = response.json()
        texto = resultado["candidates"][0]["content"]["parts"][0]["text"]
        return texto.strip()
    except Exception as e:
        return f"❌ Error al generar respuesta: {e}"
