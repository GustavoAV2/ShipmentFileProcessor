from log import logger
from watchdog.events import FileSystemEventHandler
from src.actions.shipment_integration_actions import ShipmentIntegrationActions


class FileEventProcessor(FileSystemEventHandler):
    def __init__(self):
        self.shipment_action = ShipmentIntegrationActions()

    def on_created(self, event):
        # Ação a ser executada quando um novo arquivo for criado
        logger.info(f"Novo arquivo criado: {event.src_path}")
        try:
            self.process_file(event.src_path)
        except Exception as e:
            logger.error(f"Erro ao processar o arquivo: {event.src_path}\n{str(e)}")

    def process_file(self, file_path):
        logger.info(f"Processando arquivo: {file_path}")
        try:
            self.shipment_action.integrate_file(file_path)
        except Exception as e:
            logger.error(f"Erro ao processar o arquivo: {file_path}\n{str(e)}")
