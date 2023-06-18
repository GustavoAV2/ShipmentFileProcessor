import requests
from log import logger


class ShipmentIntegration:
    def __init__(self):
        self.url = "http://localhost:5000/"
        self.token = ""
        self.client_id = ""
        self.client_secret = ""

    def _request_authorize_token(self):
        if self.token:
            return self.token
        try:
            payload = {"client_id": self.client_id, "client_secret": self.client_secret}
            response = requests.post(self.url + 'oauth/token', data=payload)
            return response.json()
        except Exception as ex:
            return {}

    def request_post_file(self, file):
        self.token = self._request_authorize_token()
        try:
            url = self.url + "process_shipment_file"
            logger.info("Requisitando: " + url)
            response = requests.post(url,
                                     headers={"Authorization": f"Bearer {self.token}"},
                                     files=file)
            return response
        except Exception as ex:
            return {}

