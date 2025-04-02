# Funciones auxiliares para tareas comunes en programación simbólica.import json

# Cargar esencia general
def cargar_esencia(path="essence/essence.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

# Leer comandos personalizados
def cargar_comandos(path="your_voice/comandos_personales.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

# Ejecutar comandos personales
def ejecutar_comando(comando, comandos_dict):
    if comando in comandos_dict:
        accion = comandos_dict[comando]
        if "respuesta" in accion:
            return accion["respuesta"]
        else:
            return f"(⚙️ Comando '{comando}' ejecutado simbólicamente.)"
    else:
        return "⚠️ Comando no reconocido. ¿Deseas agregarlo?"

# Estilo de respuesta corta para /modo_silencio
def modo_silencio_activo(comandos_dict):
    return comandos_dict.get("/modo_silencio", {}).get("activo", False)

# Mostrar lista de roles actuales
def listar_roles(esencia):
    print("\n🔰 Roles activos:")
    for rol in esencia["developer_mode"]["roles"]:
        print(f"   → {rol}")
