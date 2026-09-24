# 🤖 Local Agent Orchestrator

> **Orquestación descentralizada de agentes de IA locales.** Ejecuta múltiples agentes especializados colaborando sin depender de la nube. Privacidad total, costos cero.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Local First](https://img.shields.io/badge/Local--First-Yes-green.svg)](https://localfirstweb.dev/)

## ✨ Características Principales

- **🔒 Privacidad Garantizada:** Todo corre localmente. Tus datos nunca salen de tu máquina.
- **🧩 Arquitectura Modular:** Agrega nuevos agentes especializados fácilmente (Web, Código, Redacción).
- **💰 Costo Cero:** Usa modelos locales gratuitos (Llama 3, Mistral vía Ollama) en lugar de APIs costosas.
- **⚡ Orquestación Inteligente:** Un "Manager" asigna tareas dinámicamente a los mejores agentes disponibles.
- **🐳 Listo para Docker:** Despliegue sencillo y reproducible.

## 🚀 Quick Start

### Prerrequisitos
- Python 3.10 o superior
- [Ollama](https://ollama.ai) instalado y corriendo localmente
- Docker (opcional, para contenedores)

### Instalación Rápida

```bash
# Clonar el repositorio
git clone https://github.com/netmarti/local-agent-orchestrator.git
cd local-agent-orchestrator

# Instalar dependencias
pip install -r requirements.txt

# Configurar tu modelo local (ejemplo con Llama 3)
ollama pull llama3

# Ejecutar el orquestador
python src/main.py
local-agent-orchestrator/
├── src/
│   ├── main.py              # Punto de entrada
│   ├── orchestrator/        # Lógica del orquestador principal
│   └── agents/              # Agentes especializados (Web, Code, Writer)
├── config/
│   └── config.yaml          # Configuración de modelos y agentes
├── docs/                    # Documentación detallada
└── tests/                   # Pruebas unitarias
🛠️ Cómo Funciona
El Orquestador recibe una tarea compleja (ej: "Analiza este PDF y resume los puntos clave").
Desglosa la tarea en subtareas manejables.
Asigna cada subtarea al agente especializado más adecuado (ej: Agente "Lector" para el PDF, Agente "Resumidor" para el texto).
Comparte resultados entre agentes y entrega el resultado final.
🌟 Contribuir
¡Las contribuciones son bienvenidas! Si tienes ideas para nuevos agentes o mejoras en la arquitectura, abre un Issue o envía un Pull Request.

📄 Licencia
Este proyecto está bajo la licencia MIT. Ver LICENSE para más detalles.

Hecho con ❤️ por Daniel (netmarti) para la comunidad de IA Local.