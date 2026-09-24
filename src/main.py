#!/usr/bin/env python3
"""
Local Agent Orchestrator
Orquesta múltiples agentes de IA locales para colaborar en tareas complejas.
"""

import yaml
import logging
from pathlib import Path
from typing import Dict, Any, Optional

# Configuración básica de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/orchestrator.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AgentOrchestrator:
    """Clase principal que gestiona la colaboración entre agentes."""
    
    def __init__(self, config_path: str = "config/config.yaml"):
        self.config = self._load_config(config_path)
        self.agents = {}
        self.logger = logger
        
        logger.info("🚀 Inicializando Local Agent Orchestrator...")
        self._initialize_agents()
        
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Carga la configuración desde el archivo YAML."""
        try:
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            logger.info(f"✅ Configuración cargada desde {config_path}")
            return config
        except Exception as e:
            logger.error(f"❌ Error al cargar configuración: {e}")
            raise
            
    def _initialize_agents(self):
        """Inicializa los agentes configurados."""
        agents_config = self.config.get('agents', {})
        
        for agent_name, agent_settings in agents_config.items():
            if agent_settings.get('enabled', False):
                logger.info(f"🤖 Iniciando agente: {agent_name}")
                # Aquí se inicializaría el agente real (simulado por ahora)
                self.agents[agent_name] = {
                    'description': agent_settings['description'],
                    'specialties': agent_settings.get('specialties', []),
                    'status': 'active'
                }
                
        logger.info(f"✨ {len(self.agents)} agentes activos listos para trabajar.")
        
    def assign_task(self, task: str, required_specialty: Optional[str] = None) -> str:
        """
        Asigna una tarea al agente más adecuado.
        
        Args:
            task: Descripción de la tarea a realizar.
            required_specialty: Especialidad requerida (opcional).
            
        Returns:
            Respuesta simulada del agente asignado.
        """
        logger.info(f"📋 Tarea recibida: '{task}'")
        
        if not self.agents:
            return "❌ No hay agentes disponibles."
            
        # Selección simple de agente (en producción sería más inteligente)
        selected_agent = None
        if required_specialty:
            for name, settings in self.agents.items():
                if required_specialty in settings.get('specialties', []):
                    selected_agent = name
                    break
                    
        if not selected_agent:
            # Usar el primer agente disponible
            selected_agent = list(self.agents.keys())[0]
            
        logger.info(f"🎯 Tarea asignada a: {selected_agent}")
        
        # Simulación de respuesta del agente
        return f"✅ El agente '{selected_agent}' ({self.agents[selected_agent]['description']}) " \
               f"ha procesado la tarea: '{task}'"
               
    def run_demo(self):
        """Ejecuta una demostración de las capacidades del orquestador."""
        logger.info("🎬 Ejecutando demostración...")
        
        demo_tasks = [
            ("Analiza este código Python y encuentra errores", "code_analyzer"),
            ("Resume el artículo sobre IA local", "text_summarizer"),
            ("Busca información sobre Ollama en internet", "web_researcher"),
            ("Extrae texto de este PDF", "document_reader")
        ]
        
        for task, specialty in demo_tasks:
            result = self.assign_task(task, specialty)
            print(f"\n{result}")
            
        logger.info("🏁 Demostración completada.")

def main():
    """Punto de entrada principal."""
    try:
        orchestrator = AgentOrchestrator()
        orchestrator.run_demo()
    except KeyboardInterrupt:
        logger.info("\n⛔ Orquestador detenido por el usuario.")
    except Exception as e:
        logger.error(f"💥 Error fatal: {e}")
        raise

if __name__ == "__main__":
    main()