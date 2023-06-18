from src.log import logger
from src.client.shipment_integration_client import ShipmentIntegration


class ShipmentIntegrationActions:
    def __init__(self):
        self.client = ShipmentIntegration()

    def integrate_file(self, file_path):
        logger.info('Lendo arquivo...')
        data = {'file': open(file_path, 'rb')}
        logger.info('Enviando para API de Integração de Remessa!')
        response = self.client.request_post_file(data)
        logger.info(f'Requisição executada!')
        logger.info(f'Status code: {response.status_code}')
        logger.info(f'Response: {response.json()}')
