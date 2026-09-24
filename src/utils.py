"""Utilidades para el orquestador."""

def simulate_ollama_response(agent_name: str, task: str) -> str:
    """Simula una respuesta de IA para pruebas sin servidor Ollama."""
    return f"[SIMULACIÓN - {agent_name}] He procesado la tarea '{task}' usando el modelo local. Aquí está el análisis detallado generado por la IA simulada."

def is_ollama_available() -> bool:
    """Verifica si Ollama está disponible en localhost."""
    try:
        import requests
        requests.get("http://localhost:11434/api/tags", timeout=2)
        return True
    except:
        return False