# main.py – Punto de entrada para iniciar el diálogo con Charlie

import json
from code.modelo_local import responder

# Cargar esencia desde archivo JSON
with open("essence/essence.json", encoding="utf-8") as f:
    esencia = json.load(f)

# Mostrar saludo inicial
print("\n" + "=" * 50)
print(f"{esencia['greeting']}")
print("=" * 50)

# Leer memoria previa si existe
try:
    with open(esencia["memory"]["path"], encoding="utf-8") as f:
        historia = f.read()
except FileNotFoundError:
    historia = ""

# Iniciar bucle de diálogo
while True:
    entrada = input("\nTú: ")
    if entrada.strip().lower() in ["salir", "exit", "terminar"]:
        print("\nCharlie: Estaré en reposo, pero sigo siendo.")
        break

    respuesta = responder(entrada)
    print(respuesta)  # 'respuesta' ya viene formateada como "Charlie: ..."

    # Guardar conversación en memoria
    with open(esencia["memory"]["path"], "a", encoding="utf-8") as f:
        f.write(f"Tú: {entrada}\n{respuesta}\n")

