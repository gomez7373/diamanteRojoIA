# Script principal para programar junto a tu IA con esencia.import json

# Cargar la esencia de la IA
with open("../essence/essence.json", encoding="utf-8") as f:
    esencia = json.load(f)

# Mostrar saludo simbólico
print("\n" + "="*50)
print(f"{esencia['greeting']}")
print("Modo programación activado: Copiloto en línea.")
print("="*50 + "\n")

# Mostrar roles simbólicos
print("👤 Roles activos:")
for rol in esencia["developer_mode"]["roles"]:
    print(f"   → {rol}")
print("\n📚 Lenguajes disponibles:")
print("   " + ", ".join(esencia["developer_mode"]["languages"]))
print("="*50)

# Interacción básica de comandos
while True:
    instruccion = input("\n🔧 ¿Qué deseas que hagamos hoy? (o escribe 'salir')\n>> ")

    if instruccion.lower() in ["salir", "terminar", "exit"]:
        print("IA: Salgo del modo de codificación, pero sigo contigo.")
        break

    # Por ahora, simulamos respuesta. Luego puede integrarse a GPT o LLM local.
    respuesta = f"(⚙️ Aquí responderé con una solución en código basada en: '{instruccion}')"
    print("IA:", respuesta)

    # Preguntar si guardar snippet
    guardar = input("💾 ¿Deseas guardar este fragmento en 'snippets/logic_blocks.txt'? (s/n): ").lower()
    if guardar == "s":
        with open("snippets/logic_blocks.txt", "a", encoding="utf-8") as f:
            f.write(f"\n# Fragmento generado\n# Instrucción: {instruccion}\n{respuesta}\n")
        print("✅ Guardado exitosamente.")
