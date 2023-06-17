from log import logger
from watchdog.events import FileSystemEventHandler


class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Ação a ser executada quando um novo arquivo for criado
        logger.info(f"Novo arquivo criado: {event.src_path}")
        try:
            self.process_file(event.src_path)
        except Exception as e:
            logger.error(f"Erro ao processar o arquivo: {event.src_path}\n{str(e)}")

    @staticmethod
    def process_file(file_path):
        logger.info(f"Processando arquivo: {file_path}")
        try:
            pass
        except Exception as e:
            logger.error(f"Erro ao processar o arquivo: {file_path}\n{str(e)}")
