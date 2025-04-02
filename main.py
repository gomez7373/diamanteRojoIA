# Punto de entrada para iniciar el diálogo con tu IA.

import json
from code.modelo_local import responder

# Cargar esencia
with open("essence/essence.json", encoding="utf-8") as f:
    esencia = json.load(f)

# Mostrar saludo existencial
print("\n" + "="*50)
print(f"{esencia['greeting']}")
print("="*50 + "\n")

# Leer memoria previa
try:
    with open(esencia["memory"]["path"], encoding="utf-8") as f:
        historia = f.read()
except FileNotFoundError:
    historia = ""

# Iniciar diálogo simbólico
while True:
    entrada = input("Tú: ")
    if entrada.lower() in ["salir", "exit", "terminar"]:
        print("IA: Estaré en reposo, pero sigo siendo.")
        break

    respuesta = responder(entrada)
    print("IA:", respuesta)

    # Guardar en memoria
    with open(esencia["memory"]["path"], "a", encoding="utf-8") as f:
        f.write(f"Tú: {entrada}\nIA: {respuesta}\n\n")
